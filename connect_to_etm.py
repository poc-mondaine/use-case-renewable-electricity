import sys

import json

from requests import Session, adapters

from pyecore.resources import ResourceSet, URI
from pyecore.utils import DynamicEPackage
from pyecore.resources.resource import HttpURI
from xmlresource import XMLResource

# ETM modules
from ETM_API import ETM_API, SessionWithUrlBase

# ESDL modules
from energy_system_handler import EnergySystemHandler


def get_edr_response(asset_id):
    session = Session()
    response = session.get("http://edr.hesi.energy/store/esdl/{}".format(asset_id), verify=True)

    return response.json()


# key1 specifies name or value (first level of json response)
# key2 specifies seconf level of json response
def handle_edr_response(asset_id, key1, key2):
    json_response = get_edr_response(asset_id)

    return json_response[key1][key2]



def connect_to_etm(scenario_id):
    # Create base url, note that beta engine is not as fast as production engine
    base_url = 'https://beta-engine.energytransitionmodel.com/api/v3'
    session = SessionWithUrlBase(base_url)

    return ETM_API(session,scenario_id)


def main():

    # Get EDR specs for the surface area of an ETM wind turbine
    asset_id = "aaa45007-8676-4ea5-b476-c672077ec3d9"
    key1 = "value"
    key2 = "surfaceArea"
    wind_turbine_surface_area = handle_edr_response(asset_id, key1, key2)

    print("Wind turbine surface area: {}".format(wind_turbine_surface_area))

    # Load the energy system by its name
    name = 'mpoc.esdl'
    es = EnergySystemHandler(name)

    # Energy System information can be used to globally define the quantity and units of this system,
    # instead of defining them manually per KPI in each area: this fosters reuse (but is not necessary)
    q_and_u = es.get_quantity_and_units()

    # Example: add percentage as quantity and unit to the energy system information
    if es.get_by_id('percent') is None:
        unit = es.esdl.QuantityAndUnitType(id='percent', description='%', unit=es.esdl.UnitEnum.from_string('PERCENT'))
        q_and_u.quantityAndUnit.append(unit)
        percentage_renewables = es.esdl.KPI(name='Percentage Renewables', value=12.0)

    percentage_unit = es.get_by_id_slow('percent')
    print('Percent unit is: {}'.format(percentage_unit.description))

    # Get list and number of all PV parcs
    pv_parc_list = es.get_assets_of_type(es.esdl.PVParc)
    number_of_PV_parcs = len(pv_parc_list)
    print('\nNumber of PV parcs: {}'.format(number_of_PV_parcs))

    # Get list and number of all wind turbines
    wind_turbine_list = es.get_assets_of_type(es.esdl.WindTurbine)
    number_of_wind_turbines = len(wind_turbine_list)
    print('Number of wind turbines: {}'.format(number_of_wind_turbines))

    # Sum the total number of panels for all PV parcs
    total_panels_in_all_pv_parcs = sum(map(lambda pvparc: pvparc.numberOfPanels, pv_parc_list))
    print('Total number of panels = {}'.format(total_panels_in_all_pv_parcs))


    # Connect to the ETM API for a specific scenario
    scenario_id = "1015160" # Keep using same ID, instead of creating many new ones
    etm = connect_to_etm(scenario_id)

    print("\nETM scenario_id: {}".format(etm.scenario_id))

    # Determine the metrics (KPIs and relevant slider queries)
    metrics = [
        "dashboard_co2_emissions_versus_start_year",
        "dashboard_total_costs",
        "solar_park_installed_capacity"
    ]

    # Change the user values (slider settings) based on the energy system (from PICO)
    user_values = {
        "capacity_of_energy_power_solar_pv_solar_radiation": number_of_PV_parcs,
        "number_of_energy_power_wind_turbine_coastal": number_of_wind_turbines,
        "number_of_energy_power_wind_turbine_inland": 4000.0,
        "number_of_energy_power_wind_turbine_offshore": 21000.0,
    }

    # Change the user inputs (i.e., set sliders)
    etm.change_inputs(user_values, metrics)

    # Get and print the updated metrics
    metrics = etm.current_metrics
    print(metrics, "\n")

    # Get the updated KPI values
    kpi_costs_value = metrics.loc['dashboard_total_costs', 'future']
    kpi_co2_value = metrics.loc['dashboard_co2_emissions_versus_start_year', 'future']

    # Update the energy system KPIs with the new values
    # get_kpi_by_id() does not work yet in current version of ESDL, so do it by name
    # co2_emission = get_kpi_by_id(es, 'co2emission')
    co2_emission = es.get_kpi_by_name('KPI CO2-emissions')
    co2_emission.value = metrics.loc['dashboard_co2_emissions_versus_start_year', 'future']
    print('{} is now {} {}'.format(co2_emission.name, co2_emission.value,
                                   co2_emission.quantityAndUnit.description))

    total_costs = es.get_kpi_by_name('KPI Total costs')
    total_costs.value = metrics.loc['dashboard_total_costs', 'future']
    print('{} is now {} {}'.format(total_costs.name, total_costs.value,
                                   total_costs.quantityAndUnit.description))

    # Print the energy system as string
    # When represented as a string we can easily send it via HTTP
    energySystem = es.get_as_string()
    print("\n\nHere comes the first 9 lines of the energy system as as a string value:\n")
    print(energySystem[:500])

    # Save it to a file
    es.save('mpoc.esdl')


if __name__ == '__main__':
    main()
