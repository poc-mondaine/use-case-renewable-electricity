from pyecore.resources import ResourceSet, URI
from pyecore.utils import DynamicEPackage
from pyecore.resources.resource import HttpURI
from xmlresource import XMLResource


class EnergySystemHandler:
    """Class to handle (load, read, and update) an ESDL Energy System"""

    def __init__(self, name):
        self.name = name
        self.es, self.resource = self.load_energy_system(name)
        print('Energy system \"{}\" is loaded!\n'.format(name))


    def load_energy_system(self, name):
        # create a resourceSet that hold the contents of the esdl.ecore model and the instances we use/create
        rset = ResourceSet()

        # Assign files with the .esdl extension to the XMLResource instead of default XMI
        rset.resource_factory['esdl'] = lambda uri: XMLResource(uri)

        # Read the lastest esdl.ecore from github
        resource = rset.get_resource(HttpURI('https://raw.githubusercontent.com/EnergyTransition/ESDL/master/esdl/model/esdl.ecore'))

        esdl_model = resource.contents[0]
        # print('Namespace: {}'.format(esdl_model.nsURI))
        rset.metamodel_registry[esdl_model.nsURI] = esdl_model

        # Create a dynamic model from the loaded esdl.ecore model, which we can use to build Energy Systems
        esdl = DynamicEPackage(esdl_model)
        resource = rset.get_resource(URI('Static_model_test.esdl'))
        es = resource.contents[0]
        # At this point, the model instance is loaded!

        return es, resource


    def count_number_of_assets(self, asset_name):
        number_of_assets = 0

        for current_asset in self.es.instance[0].area.asset:

            if current_asset.name == asset_name:
                number_of_assets += 1

        return number_of_assets


    def get_asset_attribute(self, asset_name, attribute):
        asset_data = []

        for current_asset in self.es.instance[0].area.asset:

            if current_asset.name == asset_name:
                asset_data.append({
                    'name': current_asset.name,  # name
                    'attribute': {
                        'key': attribute,
                        'value': getattr(current_asset, attribute)
                    }
                })

        return asset_data


    def update_asset(self, asset_name, attribute):
        for current_asset in self.es.instance[0].area.asset:

            if current_asset.name == asset_name:
                setattr(current_asset, attribute)

        return


    def update_kpi(self, kpi_name, attribute, value):
        for current_kpi in self.es.instance[0].area.KPIs.kpi:

            if current_kpi.name == kpi_name:
                setattr(current_kpi, attribute, value)

        self.resource.save()

        return
