import os
import sys

import json

import xml.etree.ElementTree as ET

import requests
from requests import Session, adapters

from pyecore.resources import ResourceSet, URI
from pyecore.utils import DynamicEPackage
from pyecore.resources.resource import HttpURI
from xmlresource import XMLResource

# ETM modules
from ETM_API import ETM_API, SessionWithUrlBase

# ESDL modules
from energy_system_handler import EnergySystemHandler


def request_pico_response(area):
    session = Session()

    params = {
        'bebouwingsafstand': '200',
        'restrictie': ['natuur','vliegveld','infrastructuur','turbines'],
        'preverentie': ['agrarisch']
    }

    headers = {
        'accept': 'application/esdl+xml'
    }

    # TODO: Include params in the GET request
    response = session.get("https://pico.geodan.nl/pico/api/v1/{}/windturbinegebied".format(area), headers=headers, verify=True)

    file = open("pico.esdl", "w")
    file.write(response.text)
    file.close()


# key1 specifies name or value (first level of json response)
# key2 specifies second level of json response
def get_edr_response(asset_id):
    session = Session()

    params = {
        'format': 'xml'
    }

    response = session.get("http://edr.hesi.energy/store/esdl/{}".format(asset_id), params=params, verify=True)

    file = open("edr.esdl", "w")
    file.write(response.text)
    file.close()


def connect_to_etm():
    # Create base url, note that beta engine is not as fast as production engine
    base_url = 'https://beta-engine.energytransitionmodel.com/api/v3'
    session = SessionWithUrlBase(base_url)

    return ETM_API(session)


def get_specs():
    # Get EDR specs for the surface area of an ETM wind turbine
    asset_id = "aaa45007-8676-4ea5-b476-c672077ec3d9"
    get_edr_response(asset_id)

    # Load the energy system by its name
    name = 'edr.esdl'
    edr = EnergySystemHandler(name)

    wind_turbine_surface_area = edr.es.surfaceArea
    wind_turbine_flh = edr.es.fullLoadHours
    wind_turbine_power = edr.es.power

    # Get EDR specs for the surface area of an ETM solar PV parc
    # pv_parc_surface_area = 300000
    # pv_parc_flh = 867

    print("Wind turbine surface area: {}".format(wind_turbine_surface_area))
    print("Wind turbine full load hours: {}".format(wind_turbine_flh))
    print("Wind turbine power: {}".format(wind_turbine_power))
    # print("PV parc surface area: {}".format(pv_parc_surface_area))
    # print("PV parc full load hours: {}".format(pv_parc_flh))

    return wind_turbine_surface_area, wind_turbine_flh, wind_turbine_power


def add_quantity_and_units(es):
    # Energy System information can be used to globally define the quantity and units of this system,
    # instead of defining them manually per KPI in each area: this fosters reuse (but is not necessary)
    q_and_u = es.get_quantity_and_units()

    # Add emission in mton as quantity and unit to the energy system information
    if es.get_by_id('percent') is None:
        unit = es.esdl.QuantityAndUnitType(id='percent', description='%')
        q_and_u.quantityAndUnit.append(unit)

    # Add emission in mton as quantity and unit to the energy system information
    if es.get_by_id('cost') is None:
        unit = es.esdl.QuantityAndUnitType(id='meur', physicalQuantity='COST', multiplier='MEGA', description='Meur')
        q_and_u.quantityAndUnit.append(unit)


def add_kpis(es):
    # Create CO2-emissions KPI
    kpi_co2 = es.esdl.DoubleKPI(
        id=es.generate_uuid(),
        name="KPI CO2-emissions",
        value=0.0,
        quantityAndUnit=es.get_by_id_slow('percent')
    )

    # Create costs KPI
    kpi_costs = es.esdl.DoubleKPI(
        id=es.generate_uuid(),
        name="KPI Total costs",
        value=0.0,
        quantityAndUnit=es.get_by_id_slow('meur')
    )

    es.add_kpis()
    es.add_kpi(kpi_co2)
    es.add_kpi(kpi_costs)


def update_kpis(es, metrics):
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


def main(args):
    # Get user input
    geo_level = args[0]
    geo_id = args[1]

    # Get relevant specs from the EDR
    wind_turbine_surface_area, wind_turbine_flh, wind_turbine_power = get_specs()

    # Request ESDL from PICO and store the response as 'pico.esdl'
    request_pico_response("{}/{}".format(geo_level, geo_id))

    # Load the energy system by its name
    name = 'pico.esdl'
    es = EnergySystemHandler(name)

    # Add Energy System Information, quantity and units, and KPIs
    es.add_energy_system_information()
    add_quantity_and_units(es)
    add_kpis(es)

    # Get area of SearchAreaWind and determine number of wind turbines
    search_area_wind_list = es.get_potentials_of_type(es.esdl.SearchAreaWind)
    number_of_wind_turbines = search_area_wind_list[0].area / wind_turbine_surface_area
    print('Number of wind turbines: {}'.format(number_of_wind_turbines))

    # Get area of SearchAreaSolar and determine number of solar PV parcs
    # search_area_solar_list = es.get_potentials_of_type(es.esdl.SearchAreaSolar)
    # number_of_pv_parcs = search_area_solar_list[0].area / pv_parc_surface_area
    # print('Number of PV parcs: {}'.format(number_of_pv_parcs))

    # Get area id and name
    area_id = es.es.instance[0].area.id
    area_name = es.es.instance[0].area.name
    print('\nArea ID: {}'.format(area_id))
    print('Area name: {}'.format(area_name))

    # Connect to the ETM API for a specific scenario
    # scenario_id = "1015160" # Keep using same ID, instead of creating many new ones
    etm = connect_to_etm()
    etm.create_new_scenario(area_name, "{}_{}".format(area_id,str.lower(area_name)), "2050")

    print("\nETM scenario_id: {}".format(etm.scenario_id))

    # Determine the metrics (KPIs and relevant slider queries)
    gqueries = [
        "dashboard_co2_emissions_versus_start_year",
        "dashboard_total_costs",
    ]

    # Change the user values (slider settings) based on the energy system (from PICO)
    user_values = {
        # "capacity_of_energy_power_solar_pv_solar_radiation": str(number_of_pv_parcs),
        "capacity_of_energy_power_wind_turbine_inland": str(number_of_wind_turbines * wind_turbine_power / 1000000.0)
    }

    # Change the user inputs (i.e., set sliders)
    etm.change_inputs(user_values, gqueries)

    # Get and print the updated metrics
    metrics = etm.current_metrics
    print(metrics, "\n")

    # Get the updated KPI values and update the ESDL KPIs in the energy system
    update_kpis(es, metrics)

    # Print the energy system as string
    # When represented as a string we can easily send it via HTTP
    energySystem = es.get_as_string()
    print("\n\nHere comes the first 9 lines of the energy system as as a string value:\n")
    print(energySystem[:500])

    # Save it to a file
    es.save('pico.esdl')


if __name__ == '__main__':
    main(sys.argv[1:])
