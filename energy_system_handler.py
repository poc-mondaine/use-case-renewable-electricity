from pyecore.resources import ResourceSet, URI
from pyecore.utils import DynamicEPackage
from pyecore.resources.resource import HttpURI
from xmlresource import XMLResource


class EnergySystemHandler:
    """Class to handle (load, read, and update) an ESDL Energy System"""

    def __init__(self, name):
        self.name = name
        self.es, self.resource, self.esdl = self.load_energy_system(name)
        print('Energy system \"{}\" is loaded!\n'.format(name))

    @staticmethod
    def attr_to_dict(esdl_object):
        d = dict()
        d['esdlType'] = esdl_object.eClass.name
        for attr in dir(esdl_object):
            attr_value = esdl_object.eGet(attr)
            if attr_value is not None:
                d[attr] = attr_value
        return d


    def load_energy_system(self, name):
        # create a resourceSet that hold the contents of the esdl.ecore model and the instances we use/create
        rset = ResourceSet()

        # Assign files with the .esdl extension to the XMLResource instead of default XMI
        rset.resource_factory['esdl'] = lambda uri: XMLResource(uri)

        # Read the lastest esdl.ecore from github
        esdl_model_resource = rset.get_resource(HttpURI('https://raw.githubusercontent.com/EnergyTransition/ESDL/master/esdl/model/esdl.ecore'))

        esdl_model = esdl_model_resource.contents[0]
        # print('Namespace: {}'.format(esdl_model.nsURI))
        rset.metamodel_registry[esdl_model.nsURI] = esdl_model

        # Create a dynamic model from the loaded esdl.ecore model, which we can use to build Energy Systems
        esdl = DynamicEPackage(esdl_model)

        # have a nice __repr__ for some ESDL classes when printing ESDL objects (includes all Assets and EnergyAssets)
        esdl.Item.python_class.__repr__ = lambda x: '{}: ({})'.format(x.name, EnergySystemHandler.attr_to_dict(x))
        esdl.Carrier.python_class.__repr__ = lambda x: '{}: ({})'.format(x.name, EnergySystemHandler.attr_to_dict(x))
        esdl.Geometry.python_class.__repr__ = lambda x: '{}: ({})'.format(x.name, EnergySystemHandler.attr_to_dict(x))
        esdl.QuantityAndUnitType.python_class.__repr__ = lambda x: '{}: ({})'.format(x.id, EnergySystemHandler.attr_to_dict(x))
        esdl.KPI.python_class.__repr__ = lambda x: '{}: ({})'.format(x.name, EnergySystemHandler.attr_to_dict(x))

        resource = rset.get_resource(URI('Static_model_test.esdl'))
        es = resource.contents[0]
        # At this point, the model instance is loaded!

        # also return the esdl reference, so we can create esdl classes
        return es, resource, esdl

    # create a readable list of the attributes of an ESDL class

    def count_number_of_assets(self, esdl_type):
        number_of_assets = 0

        for current_asset in self.es.instance[0].area.asset:
            if isinstance(current_asset, esdl_type):
                number_of_assets += 1

        return number_of_assets


    def get_assets_of_type(self, esdl_type):
        assets = []

        for current_asset in self.es.instance[0].area.asset:
            if isinstance(current_asset, esdl_type):
                assets.append(current_asset)
        return assets

    def get_by_id(self, id):
        self.resource

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


    def get_kpi_by_id(self, id):
        for kpi in self.es.instance[0].area.KPIs.kpi:
            if kpi.id == id:
                return kpi


    def get_kpi_by_name(self, name):
        for kpi in self.es.instance[0].area.KPIs.kpi:
            if kpi.name == name:
                return kpi


    def update_kpi(self, kpi_name, attribute, value):
        for current_kpi in self.es.instance[0].area.KPIs.kpi:

            if current_kpi.name == kpi_name:
                setattr(current_kpi, attribute, value)

        self.resource.save()

        return

    def save(self):
        self.resource.save()
