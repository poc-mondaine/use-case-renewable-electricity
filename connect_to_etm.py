from pyecore.resources import ResourceSet, URI
from pyecore.utils import DynamicEPackage
from pyecore.resources.resource import HttpURI
from xmlresource import XMLResource


# ETM modules
from ETM_API import ETM_API, SessionWithUrlBase

# ESDL modules
from energy_system_handler import EnergySystemHandler


def connect_to_etm(scenario_id):
    # Create base url, note that beta engine is not as fast as production engine
    base_url = 'https://beta-engine.energytransitionmodel.com/api/v3'
    session = SessionWithUrlBase(base_url)

    return ETM_API(session,scenario_id)


def get_number_of_assets(es, asset_name):
    number_of_assets = es.count_number_of_assets(asset_name)

    return number_of_assets


def get_asset_attribute(es, asset_name, attribute):
    asset_data = es.get_asset_attribute(asset_name, attribute)

    return asset_data


def update_energy_system_asset(es, asset_name, attribute):
    es.update_asset(asset_name, attribute)

    return


def update_energy_system_kpi(es, kpi_name, attribute, value):
    es.update_kpi(kpi_name, attribute, value)

    return


def main():

    # Load the energy system by its name
    name = 'Static_model_test.esdl'
    es = EnergySystemHandler(name)

    # Get number of PV parcs in the energy system
    number_of_PV_parcs = get_number_of_assets(es, "PV parc")

    # Get number of panels for the asset named "PV parc"
    number_of_panels = get_asset_attribute(es, "PV parc", "numberOfPanels")

    # Connect to the ETM API for a specific scenario
    scenario_id = "1015160" # Keep using same ID, instead of creating many new ones
    etm = connect_to_etm(scenario_id)

    print("ETM scenario_id: {}\n".format(etm.scenario_id))

    # Determine the metrics (KPIs and relevant slider queries)
    metrics = [
        "dashboard_co2_emissions_versus_start_year",
        "dashboard_total_costs",
        "solar_park_installed_capacity"
    ]

    # Change the user values (slider settings) based on the energy system (from PICO)
    user_values = {
        "number_of_energy_power_solar_pv_solar_radiation": number_of_PV_parcs,
        "number_of_energy_power_wind_turbine_coastal": 1000.0,
        "number_of_energy_power_wind_turbine_inland": 4000.0,
        "number_of_energy_power_wind_turbine_offshore": 21000.0,
    }

    # Change the user inputs (i.e., set sliders)
    etm.change_inputs(user_values, metrics)

    # Get and print the updated metrics
    metrics = etm.current_metrics
    print(metrics)
    print()

    # Get the updated KPI values
    kpi_costs_value = metrics.loc['dashboard_total_costs', 'future']
    kpi_co2_value = metrics.loc['dashboard_co2_emissions_versus_start_year', 'future']

    # Update the energy system KPIs with the new values
    update_energy_system_kpi(es, "KPI CO2-emissions", "value", kpi_co2_value)
    update_energy_system_kpi(es, "KPI Total costs", "value", kpi_costs_value)

    # Query the (possibly) updated solar pv capacity
    solar_pv_capacity = metrics.loc['solar_park_installed_capacity', 'future']

    # Change the user values (slider settings) based on ETM user changes
    # user_values = {
    #     "number_of_energy_power_solar_pv_solar_radiation": solar_pv_capacity / 20.0,
    # }


if __name__ == '__main__':
    main()
