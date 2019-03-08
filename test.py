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


def get_number_of_assets(es, asset_type):
    number_of_assets = es.count_number_of_assets(asset_type)

    return number_of_assets


def get_assets_of_type(es, asset_type):
    assets = es.get_assets_of_type(asset_type)
    return assets


def get_asset_attribute(es, asset_name, attribute):
    asset_data = es.get_asset_attribute(asset_name, attribute)

    return asset_data


def update_energy_system_asset(es, asset_name, attribute):
    es.update_asset(asset_name, attribute)

    return


def update_energy_system_kpi(es, kpi_name, attribute, value):
    es.update_kpi(kpi_name, attribute, value)

    return



def get_kpi_by_id(es, id):
    return es.get_kpi_by_id(id)


def get_kpi_by_name(es, name):
    return es.get_kpi_by_name(name)



def main():

    # Load the energy system by its name
    name = 'Static_model_test.esdl'
    es = EnergySystemHandler(name)

    # Get number of PV parcs in the energy system
    number_of_PV_parcs = get_number_of_assets(es, es.esdl.PVParc)
    print('Number of PV parcs {}'.format(number_of_PV_parcs))

    pv_parc_list = get_assets_of_type(es, es.esdl.PVParc)
    wind_turbine_list = get_assets_of_type(es, es.esdl.WindTurbine)
    print('# PV parcs: {}, list={}'.format(len(pv_parc_list), pv_parc_list))
    print('# WindTurbines={}, list={}'.format(len(wind_turbine_list), wind_turbine_list))

    total_panels_in_all_pv_parcs = sum(map(lambda pvparc: pvparc.numberOfPanels, pv_parc_list))
    print('Total number of panels = {}'.format(total_panels_in_all_pv_parcs))

    # does not work yet in current version of ESDL, so do it by name
    #co2_emission = get_kpi_by_id(es, 'co2emission')
    co2_emission = get_kpi_by_name(es, 'KPI CO2-emissions')
    print(co2_emission)
    co2_emission.value = 2000.0
    es.save()

if __name__ == '__main__':
    main()
