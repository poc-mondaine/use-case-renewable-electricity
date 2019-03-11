
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


def get_object_by_id(es, id):
    return es.get_by_id(id)



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



    # Add energy system information to the energy system if it is not there yet
    # Energy System information can be used to globally define the quantity and units of this system,
    # instead of defining them manually per KPI in each area: this fosters reuse (but is not necessary)
    q_and_u = None
    if get_object_by_id(es, 'energy_system_information') is None:
        esi = es.esdl.EnergySystemInformation(id='energy_system_information')
        es.es.energySystemInformation = esi
        q_and_u = es.esdl.QuantityAndUnits(id='quantity_and_units')
        esi.quantityAndUnits = q_and_u;
    else:
        q_and_u = get_object_by_id(es, 'quantity_and_units')

    # Example: add percentage as quantity and unit to the energy system information
    if get_object_by_id(es, 'percent') is None:
        unit = es.esdl.QuantityAndUnitType(id='percent', description='%', unit=es.esdl.UnitEnum.from_string('PERCENT'))
        q_and_u.quantityAndUnit.append(unit)
        percentage_renewables = es.esdl.KPI(name='Percentage Renewables', value=12.0)

    # using allInstances() on a ESDL class gets you all the instances currently available in the resource
    # this is builtin pyEcore functionality
    all_kpi = es.esdl.KPI.allInstances()
    print("KPIs defined in the full EnergySystem")
    for kpi in all_kpi:
        print('\t- {}'.format(kpi))

    all_q_and_u = es.esdl.AbstractQuantityAndUnit.allInstances()
    print('Quantity and Units defined for this Energy System')
    for qu in all_q_and_u:
        print('\t- {}, parent={}'.format(qu, qu.eContainer().eClass.name))

    # use builtin allInstances() from pyEcore to get all the PVParcs defined in all the Areas and subareas
    all_pvparcs = es.esdl.PVParc.allInstances()
    print("PV Parcs:")
    for parc in all_pvparcs:
        print('\t- {}'.format(parc))

    # create a new windturbine
    turbine = es.esdl.WindTurbine(id=EnergySystemHandler.generate_uuid(),
                                  name='WindTurbine 4',
                                  power=2E6,
                                  fullLoadHours=2000,
                                  height=150.0,
                                  surfaceArea=100,
                                  prodType=es.esdl.RenewableTypeEnum.from_string('RENEWABLE'),
                                  type=es.esdl.WindTurbineTypeEnum.from_string('WIND_ON_LAND'))
    es.es.instance[0].area.asset.append(turbine)

    # example to get all assets of a specific type in all areas in the EnergySystem as a method of the Handler
    # this calls allInstances()
    print("WindTurbines:")
    generator = es.get_all_assets_of_type(es.esdl.WindTurbine)
    for wt in generator:
        print('\t- {}'.format(wt))
        wt.delete() # remove windturbine from the EnergySystem

    # get_kpi_by_id() does not work yet in current version of ESDL, so do it by name
    # co2_emission = get_kpi_by_id(es, 'co2emission')
    co2_emission = get_kpi_by_name(es, 'KPI CO2-emissions')
    co2_emission.value = 2005.0
    print('\n\n{} is now {} {}'.format(co2_emission.name, co2_emission.value,
                                   co2_emission.quantityAndUnit.reference.description))

    # print the energy system as string
    # when represented as a string we can easily send it via HTTP
    energySystem = es.get_as_string()
    print("\n\nHere comes the first 9 lines of the energy system as as a string value:\n")
    print(energySystem[:500])

    # save it to a file
    es.save('test.esdl')




if __name__ == '__main__':
    main()
