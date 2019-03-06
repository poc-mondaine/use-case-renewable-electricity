"""Definition of meta model 'esdl'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'esdl'
nsURI = 'http://www.tno.nl/esdl'
nsPrefix = 'esdl'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
CommodityEnum = EEnum('CommodityEnum', literals=[
                      'UNDEFINED', 'ELECTRICITY', 'GAS', 'HEAT', 'H2', 'BIOGAS', 'CO2', 'ENERGY'])

AreaScopeEnum = EEnum('AreaScopeEnum', literals=['UNDEFINED', 'BUILDING', 'STREET', 'ZIPCODE', 'NEIGHBOURHOOD',
                                                 'DISTRICT', 'VILLAGE', 'CITY', 'MUNICIPALITY', 'REGION', 'PROVINCE', 'STATE', 'COUNTRY', 'CONTINENT'])

ProfileTypeEnum = EEnum('ProfileTypeEnum', literals=['UNDEFINED', 'SOLARIRRADIANCE_IN_W_PER_M2', 'WINDSPEED_IN_M_PER_S', 'STATEOFCHARGE_IN_WS', 'ENERGY_IN_WH', 'ENERGY_IN_KWH', 'ENERGY_IN_MWH', 'ENERGY_IN_GWH', 'ENERGY_IN_J', 'ENERGY_IN_KJ', 'ENERGY_IN_MJ', 'ENERGY_IN_GJ', 'ENERGY_IN_TJ',
                                                     'ENERGY_IN_PJ', 'TEMPERATURE_IN_C', 'TEMPERATURE_IN_K', 'POWER_IN_W', 'POWER_IN_KW', 'POWER_IN_MW', 'POWER_IN_GW', 'POWER_IN_TW', 'MONEY_IN_EUR', 'MONEY_IN_KEUR', 'MONEY_IN_MEUR', 'PERCENTAGE', 'MONEY_IN_EUR_PER_KW', 'MONEY_IN_EUR_PER_KWH', 'VOLUME_IN_M3', 'VOLUME_IN_LITERS'])

DurationUnitEnum = EEnum('DurationUnitEnum', literals=[
                         'SECOND', 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'])

BuildingTypeEnum = EEnum('BuildingTypeEnum', literals=['UNDEFINED', 'RESIDENTIAL', 'GATHERING', 'PRISON', 'HEALTHCARE',
                                                       'INDUSTRY', 'OFFICE', 'EDUCATION', 'SPORTS', 'SHOPPING', 'HOTEL', 'GREENHOUSE', 'UTILITY', 'OTHER'])

ConsTypeEnum = EEnum('ConsTypeEnum', literals=['PRIMARY', 'FINAL'])

SourceTypeEnum = EEnum('SourceTypeEnum', literals=[
                       'UNDEFINED', 'AIR', 'SUB_SURFACE', 'AQUIFER', 'SURFACE_WATER', 'HEAT_NETWORK'])

AggrTypeEnum = EEnum('AggrTypeEnum', literals=[
                     'UNDEFINED', 'NOT_AGGREGATED', 'PER_COMMODITY', 'TOTAL_ENERGY', 'TOTAL_CAPABILITY', 'PER_CAPIBILITY'])

AreaTypeEnum = EEnum('AreaTypeEnum', literals=['UNDEFINED', 'ROAD', 'RAILWAY', 'TERRAIN',
                                               'RURAL_AREA', 'BUILT', 'WATER', 'SEA', 'RIVER', 'CANAL', 'LAKE', 'LAND', 'PARCEL'])

HeatDemandTypeEnum = EEnum('HeatDemandTypeEnum', literals=[
                           'UNDEFINED', 'SPACE_HEATING', 'HOT_TAPWATER', 'SH_AND_HTW', 'OTHER'])

HousingTypeEnum = EEnum('HousingTypeEnum', literals=[
                        'UNDEFINED', 'OWNER_OCCUPIED_PROPERTY', 'PRIVATE_RENTAL', 'HOUSING_ASSOCIATION'])

RoofTypeEnum = EEnum('RoofTypeEnum', literals=[
                     'UNDEFINED', 'FLATROOF', 'SLANTEDROOF', 'COMBINATION'])

EnergyLabelEnum = EEnum('EnergyLabelEnum', literals=['UNDEFINED', 'LABEL_G', 'LABEL_F', 'LABEL_E',
                                                     'LABEL_D', 'LABEL_C', 'LABEL_B', 'LABEL_A', 'LABEL_AP', 'LABEL_APP', 'LABEL_APPP', 'LABEL_APPPP'])

ResidentialBuildingTypeEnum = EEnum('ResidentialBuildingTypeEnum', literals=['UNDEFINED', 'VRIJSTAANDE_WONING', 'TWEE_ONDER_EEN_KAP_WONING', 'RIJWONING',
                                                                             'MAISONNETTEWONING', 'GALERIJWONING', 'PORTIEKWONING', 'FLATWONING', 'TUSSENWONING', 'HOEKWONING', 'GALERIJCOMPLEX', 'APPARTEMENTENCOMPLEX'])

PowerPlantFuelEnum = EEnum('PowerPlantFuelEnum', literals=[
                           'UNDEFINED', 'COAL', 'BLAST_FURNACE_GAS', 'NATURAL_GAS', 'URANIUM', 'HYDROGEN'])

SectorEnum = EEnum('SectorEnum', literals=[
                   'UNDEFINED', 'GEBOUWDE_OMGEVING', 'ZAKELIJKE_DIENSTVERLENING', 'INDUSTRIE', 'AGRO_TUINBOUW'])

RenewableTypeEnum = EEnum('RenewableTypeEnum', literals=['UNDEFINED', 'RENEWABLE', 'FOSSIL'])

StateOfMatterEnum = EEnum('StateOfMatterEnum', literals=['UNDEFINED', 'SOLID', 'LIQUID', 'GASEOUS'])

CostUnitEnum = EEnum('CostUnitEnum', literals=[
                     'UNDEFINED', 'MONEY_IN_EUR', 'MONEY_IN_KEUR', 'MONEY_IN_MEUR', 'MONEY_IN_EUR_PER_KW', 'MONEY_IN_EUR_PER_KWH'])

GeothermalSourceTypeEnum = EEnum('GeothermalSourceTypeEnum', literals=[
                                 'UNDEFINED', 'HEAT', 'ELECTRICITY'])

CHPTypeEnum = EEnum('CHPTypeEnum', literals=['UNDEFINED', 'STEG', 'GAS_TURBINE', 'GAS_MOTOR'])

GlasTypeEnum = EEnum('GlasTypeEnum', literals=[
                     'UNDEFINED', 'ENKEL_GLAS', 'DUBBEL_GLAS', 'HR_GLAS', 'HRP_GLAS', 'HRPP_GLAS', 'HRPPP_GLAS'])

VentilationTypeEnum = EEnum('VentilationTypeEnum', literals=[
                            'UNDEFINED', 'NATURAL', 'MECHANIC_IN', 'MECHANIC_OUT', 'MECHANIC_INOUT', 'BALANCED', 'BALANCED_WITH_HEATRECUPERATION'])

GasHeaterTypeEnum = EEnum('GasHeaterTypeEnum', literals=[
                          'UNDEFINED', 'CR', 'VR', 'HR100', 'HR104', 'HR107', 'HRE', 'HRWW'])

InhabitantsTypeEnum = EEnum('InhabitantsTypeEnum', literals=[
                            'UNDEFINED', 'ALLEENSTAAND', 'TWEEVERDIENERS', 'GEZIN_MET_KINDEREN', 'BEJAARD_ECHTPAAR'])

AdditionalHeatingSourceTypeEnum = EEnum(
    'AdditionalHeatingSourceTypeEnum', literals=['NONE', 'ELECTRIC', 'GAS'])

GeothermalPotentialEnum = EEnum('GeothermalPotentialEnum', literals=['UNKNOWN', 'POSSIBLE', 'GOOD'])

GeothermalPowerEnum = EEnum('GeothermalPowerEnum', literals=[
                            'UNKNOWN', 'POSSIBLE_GT5MWTH', 'GOOD_GT5MWTH', 'GOOD_GT7P5MWTH', 'GOOD_GT10MWTH'])

ResidualHeatSourceTypeEnum = EEnum('ResidualHeatSourceTypeEnum', literals=[
                                   'UNDEFINED', 'INDUSTRIAL', 'DATACENTER', 'COOLING_HOUSE', 'OTHER'])

MobilityFuelTypeEnum = EEnum('MobilityFuelTypeEnum', literals=[
                             'UNDEFINED', 'PETROL', 'DIESEL', 'HYDROGEN', 'LPG', 'BIOFUEL', 'ELECTRICITY', 'OIL', 'LNG', 'KEROSENE'])

VehicleTypeEnum = EEnum('VehicleTypeEnum', literals=['UNDEFINED', 'CAR', 'TRUCK', 'VAN', 'BUS', 'METRO', 'TRAM', 'TRAIN', 'PASSENGER_TRAIN',
                                                     'FREIGHT_TRAIN', 'SCOOTER', 'MOTOR_CYCLE', 'NONROAD_VEHICLE', 'AGRARIAN_VEHICLE', 'BARGE', 'INTERNATIONAL_SHIPPING', 'AIRCRAFT', 'OTHER', 'TOTAL'])

MultiplierEnum = EEnum('MultiplierEnum', literals=[
                       'NONE', 'KILO', 'MEGA', 'GIGA', 'TERRA', 'PETA', 'MILLI', 'MICRO', 'NANO', 'PICO'])

PhysicalQuantityEnum = EEnum('PhysicalQuantityEnum', literals=['UNDEFINED', 'ENERGY', 'POWER', 'VOLTAGE', 'PRESSURE', 'TEMPERATURE',
                                                               'EMISSION', 'COST', 'TIME', 'LENGTH', 'DISTANCE', 'IRRADIANCE', 'SPEED', 'STATE_OF_CHARGE', 'VOLUME', 'AREA'])

UnitEnum = EEnum('UnitEnum', literals=['NONE', 'JOULE', 'WATTHOUR', 'WATT', 'VOLT', 'BAR', 'PSI', 'DEGREES_CELSIUS', 'KELVIN', 'GRAM', 'EURO', 'DOLLAR', 'SECOND',
                                       'MINUTE', 'QUARTER', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR', 'METRE', 'SQUARE_METRE', 'CUBIC_METRE', 'LITRE', 'WATTSECOND', 'ARE', 'HECTARE', 'PERCENT'])

TimeUnit = EEnum('TimeUnit', literals=['NONE', 'SECOND',
                                       'MINUTE', 'QUARTER', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'])

GasConversionTypeEnum = EEnum('GasConversionTypeEnum', literals=['UNDEFINED', 'SMR', 'ATR'])

PVInstallationTypeEnum = EEnum('PVInstallationTypeEnum', literals=[
                               'UNDEFINED', 'ROOFTOP_PV', 'BUILDING_INTEGRATED_PV', 'WINDOW', 'ROAD', 'FIELD', 'WATER'])

WindTurbineTypeEnum = EEnum('WindTurbineTypeEnum', literals=[
                            'UNDEFINED', 'WIND_ON_LAND', 'WIND_AT_SEA', 'WIND_ON_COAST', 'WIND_ON_BUILDING'])

WaterToPowerTypeEnum = EEnum('WaterToPowerTypeEnum', literals=[
                             'UNDEFINED', 'HYDRO_POWER', 'WAVE_POWER', 'TIDAL_POWER', 'OSMOTIC_POWER'])

SolarCollectorTypeEnum = EEnum('SolarCollectorTypeEnum', literals=[
                               'UNDEFINED', 'ROOFTOP', 'BUILDING_INTEGRATED_SC', 'ROAD', 'FIELD', 'WATER'])

HeatRadiationDeviceTypeEnum = EEnum('HeatRadiationDeviceTypeEnum', literals=[
                                    'UNDEFINED', 'HT_RADIATOR', 'LT_RADIATOR', 'FLOOR_HEATING', 'WALL_HEATING', 'INFRARED_PANEL'])

CoolingDeviceType = EEnum('CoolingDeviceType', literals=[
                          'UNDEFINED', 'FLOOR_COOLING', 'AIR_CONDITIONING'])

RoomHeaterTypeEnum = EEnum('RoomHeaterTypeEnum', literals=[
                           'UNDEFINED', 'GAS_STOVE', 'WOOD_STOVE', 'ELECTRIC', 'INFRARED_PANEL'])

BiomassHeaterTypeEnum = EEnum('BiomassHeaterTypeEnum', literals=[
                              'UNDEFINED', 'FULLY_AUTOMATD', 'SEMI_AUTOMATED', 'PELLET_FIRED', 'CHP'])

UTESPotentialTypeEnum = EEnum('UTESPotentialTypeEnum', literals=[
                              'UNDEFINED', 'HEAT_OPEN', 'HEAT_CLOSED', 'COLD_OPEN', 'COLD_CLOSED'])

UTESTypeEnum = EEnum('UTESTypeEnum', literals=[
                     'UNDEFINED', 'AQUIFER_TES', 'BOREHOLE_TES', 'CAVERN_TES', 'OTHER'])

InterpolationMethodEnum = EEnum('InterpolationMethodEnum', literals=[
                                'UNDEFINED', 'NONE', 'LINEAR', 'CUBIC', 'NEAREST', 'PREVIOUS', 'NEXT', 'OTHER'])


class EnergySystem(EObject, metaclass=MetaEClass):
    """This is the entry class to describe an EnergySystem in ESDL"""
    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    geographicalScope = EAttribute(eType=EString, derived=False, changeable=True)
    sector = EAttribute(eType=SectorEnum, derived=False, changeable=True, upper=-1)
    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    measures = EReference(ordered=True, unique=True, containment=True)
    instance = EReference(ordered=True, unique=True, containment=True, upper=-1)
    energySystemInformation = EReference(ordered=True, unique=True, containment=True)
    parties = EReference(ordered=True, unique=True, containment=True)
    services = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, description=None, geographicalScope=None, sector=None, measures=None, instance=None, energySystemInformation=None, parties=None, services=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if geographicalScope is not None:
            self.geographicalScope = geographicalScope

        if sector:
            self.sector.extend(sector)

        if id is not None:
            self.id = id

        if measures is not None:
            self.measures = measures

        if instance:
            self.instance.extend(instance)

        if energySystemInformation is not None:
            self.energySystemInformation = energySystemInformation

        if parties is not None:
            self.parties = parties

        if services is not None:
            self.services = services


class Area(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    scope = EAttribute(eType=AreaScopeEnum, derived=False, changeable=True,
                       default_value=AreaScopeEnum.UNDEFINED)
    type = EAttribute(eType=AreaTypeEnum, derived=False, changeable=True)
    geometryReference = EAttribute(eType=EString, derived=False, changeable=True)
    buildingDensity = EAttribute(eType=EDouble, derived=False, changeable=True)
    location = EReference(ordered=True, unique=True, containment=True)
    contour = EReference(ordered=True, unique=True, containment=True)
    socialProperties = EReference(ordered=True, unique=True, containment=True)
    economicProperties = EReference(ordered=True, unique=True, containment=True)
    asset = EReference(ordered=True, unique=True, containment=True, upper=-1)
    area = EReference(ordered=True, unique=True, containment=True, upper=-1)
    containingArea = EReference(ordered=True, unique=True, containment=False)
    isOwnedBy = EReference(ordered=True, unique=True, containment=False)
    mobilityProperties = EReference(ordered=True, unique=True, containment=True)
    KPIs = EReference(ordered=True, unique=True, containment=True)
    potential = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, id=None, name=None, scope=None, type=None, location=None, contour=None, socialProperties=None, economicProperties=None, asset=None, area=None, containingArea=None, isOwnedBy=None, geometryReference=None, mobilityProperties=None, buildingDensity=None, KPIs=None, potential=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if scope is not None:
            self.scope = scope

        if type is not None:
            self.type = type

        if geometryReference is not None:
            self.geometryReference = geometryReference

        if buildingDensity is not None:
            self.buildingDensity = buildingDensity

        if location is not None:
            self.location = location

        if contour is not None:
            self.contour = contour

        if socialProperties is not None:
            self.socialProperties = socialProperties

        if economicProperties is not None:
            self.economicProperties = economicProperties

        if asset:
            self.asset.extend(asset)

        if area:
            self.area.extend(area)

        if containingArea is not None:
            self.containingArea = containingArea

        if isOwnedBy is not None:
            self.isOwnedBy = isOwnedBy

        if mobilityProperties is not None:
            self.mobilityProperties = mobilityProperties

        if KPIs is not None:
            self.KPIs = KPIs

        if potential:
            self.potential.extend(potential)


@abstract
class Port(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    maxPower = EAttribute(eType=EDouble, derived=False, changeable=True)
    simultaneousPower = EAttribute(eType=EDouble, derived=False, changeable=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    energyasset = EReference(ordered=True, unique=True, containment=False)
    profile = EReference(ordered=True, unique=True, containment=True)
    carrier = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, id=None, maxPower=None, energyasset=None, profile=None, carrier=None, simultaneousPower=None, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if maxPower is not None:
            self.maxPower = maxPower

        if simultaneousPower is not None:
            self.simultaneousPower = simultaneousPower

        if name is not None:
            self.name = name

        if energyasset is not None:
            self.energyasset = energyasset

        if profile is not None:
            self.profile = profile

        if carrier is not None:
            self.carrier = carrier


class EconomicProperties(EObject, metaclass=MetaEClass):

    averageIncome = EAttribute(eType=EDouble, derived=False, changeable=True)
    averageWOZvalue = EAttribute(eType=EDouble, derived=False, changeable=True)
    percentageOwnerOccupiedProperties = EAttribute(eType=EDouble, derived=False, changeable=True)
    percentageHousingAssociation = EAttribute(eType=EDouble, derived=False, changeable=True)
    percentagePrivateRental = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, averageIncome=None, averageWOZvalue=None, percentageOwnerOccupiedProperties=None, percentageHousingAssociation=None, percentagePrivateRental=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if averageIncome is not None:
            self.averageIncome = averageIncome

        if averageWOZvalue is not None:
            self.averageWOZvalue = averageWOZvalue

        if percentageOwnerOccupiedProperties is not None:
            self.percentageOwnerOccupiedProperties = percentageOwnerOccupiedProperties

        if percentageHousingAssociation is not None:
            self.percentageHousingAssociation = percentageHousingAssociation

        if percentagePrivateRental is not None:
            self.percentagePrivateRental = percentagePrivateRental


class SocialProperties(EObject, metaclass=MetaEClass):

    socialCohesion = EAttribute(eType=EDouble, derived=False, changeable=True)
    populationDensity = EAttribute(eType=EInt, derived=False, changeable=True)
    numberOfInhabitants = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, socialCohesion=None, populationDensity=None, numberOfInhabitants=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if socialCohesion is not None:
            self.socialCohesion = socialCohesion

        if populationDensity is not None:
            self.populationDensity = populationDensity

        if numberOfInhabitants is not None:
            self.numberOfInhabitants = numberOfInhabitants


@abstract
class Item(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    shortName = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    originalIdInSource = EAttribute(eType=EString, derived=False, changeable=True)
    isOwnedBy = EReference(ordered=True, unique=True, containment=False)
    dataSource = EReference(ordered=True, unique=True, containment=True)
    sector = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, id=None, name=None, shortName=None, isOwnedBy=None, description=None, originalIdInSource=None, dataSource=None, sector=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if shortName is not None:
            self.shortName = shortName

        if description is not None:
            self.description = description

        if originalIdInSource is not None:
            self.originalIdInSource = originalIdInSource

        if isOwnedBy is not None:
            self.isOwnedBy = isOwnedBy

        if dataSource is not None:
            self.dataSource = dataSource

        if sector is not None:
            self.sector = sector


class Measures(EObject, metaclass=MetaEClass):

    asset = EReference(ordered=True, unique=True, containment=True, upper=-1)
    measuresCollection = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, asset=None, measuresCollection=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if asset:
            self.asset.extend(asset)

        if measuresCollection:
            self.measuresCollection.extend(measuresCollection)


class Instance(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    detailLevel = EAttribute(eType=AreaScopeEnum, derived=False,
                             changeable=True, default_value=AreaScopeEnum.UNDEFINED)
    aggrType = EAttribute(eType=AggrTypeEnum, derived=False, changeable=True)
    area = EReference(ordered=True, unique=True, containment=True)
    date = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, id=None, name=None, description=None, detailLevel=None, aggrType=None, area=None, date=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if detailLevel is not None:
            self.detailLevel = detailLevel

        if aggrType is not None:
            self.aggrType = aggrType

        if area is not None:
            self.area = area

        if date is not None:
            self.date = date


class Carriers(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    carrier = EReference(ordered=True, unique=True, containment=True, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, carrier=None, dataSource=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if carrier:
            self.carrier.extend(carrier)

        if dataSource is not None:
            self.dataSource = dataSource


class EnergySystemInformation(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    carriers = EReference(ordered=True, unique=True, containment=True)
    profiles = EReference(ordered=True, unique=True, containment=True)
    dataSources = EReference(ordered=True, unique=True, containment=True)
    mobilityFuelInformation = EReference(ordered=True, unique=True, containment=True)
    quantityAndUnits = EReference(ordered=True, unique=True, containment=True)
    sectors = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, carriers=None, profiles=None, dataSources=None, mobilityFuelInformation=None, quantityAndUnits=None, sectors=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if carriers is not None:
            self.carriers = carriers

        if profiles is not None:
            self.profiles = profiles

        if dataSources is not None:
            self.dataSources = dataSources

        if mobilityFuelInformation is not None:
            self.mobilityFuelInformation = mobilityFuelInformation

        if quantityAndUnits is not None:
            self.quantityAndUnits = quantityAndUnits

        if sectors is not None:
            self.sectors = sectors


@abstract
class GenericProfile(EObject, metaclass=MetaEClass):
    """All profiles should describe these fields: a name and a ProfileType. There are two different profile types: static, with static values stored in the ESDL model itself. And External, which allows you to refer to an externally defined profile (e.g. in an Energy Information System or a timeseries database)"""
    name = EAttribute(eType=EString, derived=False, changeable=True)
    profileType = EAttribute(eType=ProfileTypeEnum, derived=False,
                             changeable=True, default_value=ProfileTypeEnum.UNDEFINED)
    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    interpolationMethod = EAttribute(eType=InterpolationMethodEnum, derived=False,
                                     changeable=True, default_value=InterpolationMethodEnum.UNDEFINED)
    dataSource = EReference(ordered=True, unique=True, containment=True)
    profileQuantityAndUnit = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, profileType=None, id=None, dataSource=None, profileQuantityAndUnit=None, interpolationMethod=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if profileType is not None:
            self.profileType = profileType

        if id is not None:
            self.id = id

        if interpolationMethod is not None:
            self.interpolationMethod = interpolationMethod

        if dataSource is not None:
            self.dataSource = dataSource

        if profileQuantityAndUnit is not None:
            self.profileQuantityAndUnit = profileQuantityAndUnit

    def getProfile(self, from_=None, to=None, aggregationPrecision=None):

        raise NotImplementedError('operation getProfile(...) not yet implemented')

    def setProfile(self, profileElementList=None):

        raise NotImplementedError('operation setProfile(...) not yet implemented')


class ProfileElement(EObject, metaclass=MetaEClass):
    """ProfileElement describes a single profile element describing a range and a value which is valid for this range. From-field is inclusive, To-field is exclusive, allowing you to describe ranges such as 1-1-2017T00:00:00.000 to 1-1-2018T00:00:00.000 instead of 31-12-2017T23:59:59:999. The to-field may be ommitted, meaning this value is valid for all time after the specified to-datetime.
Examples: The heat demand of a municipality in 2013 is 20 PJ. The range you define is then from 1-1-2013T to 1-1-2014T and the value 20 and ProfileType ENERGY_IN_PJ"""
    from_ = EAttribute(eType=EDate, derived=False, changeable=True)
    to = EAttribute(eType=EDate, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, from_=None, to=None, value=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if from_ is not None:
            self.from_ = from_

        if to is not None:
            self.to = to

        if value is not None:
            self.value = value


@abstract
class GenericDistribution(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Percentile(EObject, metaclass=MetaEClass):

    percentile = EAttribute(eType=EInt, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, percentile=None, value=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if percentile is not None:
            self.percentile = percentile

        if value is not None:
            self.value = value


class CostInformation(EObject, metaclass=MetaEClass):

    investmentCosts = EReference(ordered=True, unique=True, containment=True)
    installationCosts = EReference(ordered=True, unique=True, containment=True)
    fixedOperationalAndMaintenanceCosts = EReference(ordered=True, unique=True, containment=True)
    marginalCosts = EReference(ordered=True, unique=True, containment=True)
    variableOperationalAndMaintenanceCosts = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, investmentCosts=None, installationCosts=None, fixedOperationalAndMaintenanceCosts=None, marginalCosts=None, variableOperationalAndMaintenanceCosts=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if investmentCosts is not None:
            self.investmentCosts = investmentCosts

        if installationCosts is not None:
            self.installationCosts = installationCosts

        if fixedOperationalAndMaintenanceCosts is not None:
            self.fixedOperationalAndMaintenanceCosts = fixedOperationalAndMaintenanceCosts

        if marginalCosts is not None:
            self.marginalCosts = marginalCosts

        if variableOperationalAndMaintenanceCosts is not None:
            self.variableOperationalAndMaintenanceCosts = variableOperationalAndMaintenanceCosts


class StringPerc(EObject, metaclass=MetaEClass):

    label = EAttribute(eType=EString, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, label=None, percentage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if label is not None:
            self.label = label

        if percentage is not None:
            self.percentage = percentage


class EnergyLabelPerc(EObject, metaclass=MetaEClass):

    energyLabel = EAttribute(eType=EnergyLabelEnum, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, energyLabel=None, percentage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if energyLabel is not None:
            self.energyLabel = energyLabel

        if percentage is not None:
            self.percentage = percentage


class FromToPerc(EObject, metaclass=MetaEClass):

    from_ = EAttribute(eType=EDouble, derived=False, changeable=True)
    to = EAttribute(eType=EDouble, derived=False, changeable=True)
    percentage = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, from_=None, to=None, percentage=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if from_ is not None:
            self.from_ = from_

        if to is not None:
            self.to = to

        if percentage is not None:
            self.percentage = percentage


class PItemStat(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=EDouble, derived=False, changeable=True)
    sigma = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, value=None, sigma=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if sigma is not None:
            self.sigma = sigma


@abstract
class AbstractVariance(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Party(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    shortName = EAttribute(eType=EString, derived=False, changeable=True)
    owns = EReference(ordered=True, unique=True, containment=False, upper=-1)
    ownsArea = EReference(ordered=True, unique=True, containment=False, upper=-1)
    sector = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, owns=None, id=None, name=None, shortName=None, ownsArea=None, sector=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if shortName is not None:
            self.shortName = shortName

        if owns:
            self.owns.extend(owns)

        if ownsArea:
            self.ownsArea.extend(ownsArea)

        if sector is not None:
            self.sector = sector


@abstract
class Geometry(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class Carrier(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    cost = EReference(ordered=True, unique=True, containment=True)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, id=None, cost=None, dataSource=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if id is not None:
            self.id = id

        if cost is not None:
            self.cost = cost

        if dataSource is not None:
            self.dataSource = dataSource


class Duration(EObject, metaclass=MetaEClass):

    value = EAttribute(eType=ELong, derived=False, changeable=True)
    durationUnit = EAttribute(eType=DurationUnitEnum, derived=False,
                              changeable=True, default_value=DurationUnitEnum.SECOND)

    def __init__(self, *, value=None, durationUnit=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if value is not None:
            self.value = value

        if durationUnit is not None:
            self.durationUnit = durationUnit


class Profiles(EObject, metaclass=MetaEClass):

    profile = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, profile=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if profile:
            self.profile.extend(profile)


class Parties(EObject, metaclass=MetaEClass):

    party = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, party=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if party:
            self.party.extend(party)


class DataSources(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    dataSource = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, dataSource=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if dataSource:
            self.dataSource.extend(dataSource)


class SubPolygon(EObject, metaclass=MetaEClass):

    point = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, point=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if point:
            self.point.extend(point)


class MobilityFuelInformation(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    vehicleFuelEfficiency = EReference(ordered=True, unique=True, containment=True, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, vehicleFuelEfficiency=None, dataSource=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if vehicleFuelEfficiency:
            self.vehicleFuelEfficiency.extend(vehicleFuelEfficiency)

        if dataSource is not None:
            self.dataSource = dataSource


class VehicleFuelEfficiency(EObject, metaclass=MetaEClass):

    vehicleType = EAttribute(eType=VehicleTypeEnum, derived=False, changeable=True)
    fuel = EAttribute(eType=MobilityFuelTypeEnum, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, vehicleType=None, fuel=None, efficiency=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if vehicleType is not None:
            self.vehicleType = vehicleType

        if fuel is not None:
            self.fuel = fuel

        if efficiency is not None:
            self.efficiency = efficiency


class MobilityProperties(EObject, metaclass=MetaEClass):

    numberOfVehicles = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, numberOfVehicles=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if numberOfVehicles is not None:
            self.numberOfVehicles = numberOfVehicles


class NumberOfVehicles(EObject, metaclass=MetaEClass):

    vehicleCount = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, vehicleCount=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if vehicleCount:
            self.vehicleCount.extend(vehicleCount)


class VehicleCount(EObject, metaclass=MetaEClass):

    type = EAttribute(eType=VehicleTypeEnum, derived=False, changeable=True)
    count = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, type=None, count=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if type is not None:
            self.type = type

        if count is not None:
            self.count = count


class Services(EObject, metaclass=MetaEClass):

    service = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, service=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if service:
            self.service.extend(service)


@abstract
class AbstractDataSource(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class KPIs(EObject, metaclass=MetaEClass):

    description = EAttribute(eType=EString, derived=False, changeable=True)
    kpi = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, kpi=None, description=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if description is not None:
            self.description = description

        if kpi:
            self.kpi.extend(kpi)


class KPI(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, derived=False, changeable=True)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, value=None, quantityAndUnit=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if value is not None:
            self.value = value

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit


class QuantityAndUnits(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, quantityAndUnit=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if quantityAndUnit:
            self.quantityAndUnit.extend(quantityAndUnit)


@abstract
class AbstractQuantityAndUnit(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class Parameters(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    parameterUnit = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, parameterUnit=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if parameterUnit is not None:
            self.parameterUnit = parameterUnit


class MeasuresCollection(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    asset = EReference(ordered=True, unique=True, containment=True, upper=-1)
    costInformation = EReference(ordered=True, unique=True, containment=True)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, id=None, name=None, asset=None, costInformation=None, description=None, dataSource=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if asset:
            self.asset.extend(asset)

        if costInformation is not None:
            self.costInformation = costInformation

        if dataSource is not None:
            self.dataSource = dataSource


class Sectors(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    sector = EReference(ordered=True, unique=True, containment=True, upper=-1)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, sector=None, dataSource=None, id=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if sector:
            self.sector.extend(sector)

        if dataSource is not None:
            self.dataSource = dataSource


class Sector(EObject, metaclass=MetaEClass):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    code = EAttribute(eType=EString, derived=False, changeable=True)
    dataSource = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, id=None, name=None, description=None, dataSource=None, code=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if code is not None:
            self.code = code

        if dataSource is not None:
            self.dataSource = dataSource


@abstract
class AbstractInstanceDate(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class InPort(Port):

    connectedTo = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, connectedTo=None, **kwargs):

        super().__init__(**kwargs)

        if connectedTo:
            self.connectedTo.extend(connectedTo)


class OutPort(Port):

    connectedTo = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, connectedTo=None, **kwargs):

        super().__init__(**kwargs)

        if connectedTo:
            self.connectedTo.extend(connectedTo)


@abstract
class Asset(Item):

    surfaceArea = EAttribute(eType=EInt, derived=False, changeable=True)
    commissioningDate = EAttribute(eType=EDate, derived=False, changeable=True)
    decommissioningDate = EAttribute(eType=EDate, derived=False, changeable=True)
    owner = EAttribute(eType=EString, derived=False, changeable=True)
    technicalLifetime = EAttribute(eType=EDouble, derived=False, changeable=True)
    aggregated = EAttribute(eType=EBoolean, derived=False, changeable=True)
    aggregationCount = EAttribute(eType=EInt, derived=False, changeable=True, default_value=1)
    installationDuration = EAttribute(eType=EDouble, derived=False, changeable=True)
    area = EReference(ordered=True, unique=True, containment=False)
    containingBuilding = EReference(ordered=True, unique=True, containment=False)
    geometry = EReference(ordered=True, unique=True, containment=True)
    costInformation = EReference(ordered=True, unique=True, containment=True)
    KPIs = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, surfaceArea=None, commissioningDate=None, decommissioningDate=None, owner=None, area=None, containingBuilding=None, geometry=None, costInformation=None, technicalLifetime=None, aggregated=None, aggregationCount=None, installationDuration=None, KPIs=None, **kwargs):

        super().__init__(**kwargs)

        if surfaceArea is not None:
            self.surfaceArea = surfaceArea

        if commissioningDate is not None:
            self.commissioningDate = commissioningDate

        if decommissioningDate is not None:
            self.decommissioningDate = decommissioningDate

        if owner is not None:
            self.owner = owner

        if technicalLifetime is not None:
            self.technicalLifetime = technicalLifetime

        if aggregated is not None:
            self.aggregated = aggregated

        if aggregationCount is not None:
            self.aggregationCount = aggregationCount

        if installationDuration is not None:
            self.installationDuration = installationDuration

        if area is not None:
            self.area = area

        if containingBuilding is not None:
            self.containingBuilding = containingBuilding

        if geometry is not None:
            self.geometry = geometry

        if costInformation is not None:
            self.costInformation = costInformation

        if KPIs is not None:
            self.KPIs = KPIs


class Point(Geometry):

    lat = EAttribute(eType=EDouble, derived=False, changeable=True)
    lon = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, lat=None, lon=None, **kwargs):

        super().__init__(**kwargs)

        if lat is not None:
            self.lat = lat

        if lon is not None:
            self.lon = lon


class Polygon(Geometry):

    exterior = EReference(ordered=True, unique=True, containment=True)
    interior = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, exterior=None, interior=None, **kwargs):

        super().__init__(**kwargs)

        if exterior is not None:
            self.exterior = exterior

        if interior:
            self.interior.extend(interior)


@abstract
class Service(Item):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Potential(Item):

    geometryReference = EAttribute(eType=EString, derived=False, changeable=True)
    aggregated = EAttribute(eType=EBoolean, derived=False, changeable=True, default_value=False)
    aggregationCount = EAttribute(eType=EInt, derived=False, changeable=True, default_value=1)
    geometry = EReference(ordered=True, unique=True, containment=True)
    quantityAndUnit = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, geometry=None, geometryReference=None, quantityAndUnit=None, aggregated=None, aggregationCount=None, **kwargs):

        super().__init__(**kwargs)

        if geometryReference is not None:
            self.geometryReference = geometryReference

        if aggregated is not None:
            self.aggregated = aggregated

        if aggregationCount is not None:
            self.aggregationCount = aggregationCount

        if geometry is not None:
            self.geometry = geometry

        if quantityAndUnit is not None:
            self.quantityAndUnit = quantityAndUnit


class EnergyCarrier(Carrier):

    energyContent = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    emission = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    energyCarrierType = EAttribute(eType=RenewableTypeEnum, derived=False, changeable=True)
    stateOfMatter = EAttribute(eType=StateOfMatterEnum, derived=False, changeable=True)
    energyContentUnit = EReference(ordered=True, unique=True, containment=True)
    emissionUnit = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, energyContent=None, emission=None, energyCarrierType=None, stateOfMatter=None, energyContentUnit=None, emissionUnit=None, **kwargs):

        super().__init__(**kwargs)

        if energyContent is not None:
            self.energyContent = energyContent

        if emission is not None:
            self.emission = emission

        if energyCarrierType is not None:
            self.energyCarrierType = energyCarrierType

        if stateOfMatter is not None:
            self.stateOfMatter = stateOfMatter

        if energyContentUnit is not None:
            self.energyContentUnit = energyContentUnit

        if emissionUnit is not None:
            self.emissionUnit = emissionUnit


@abstract
class StaticProfile(GenericProfile):
    """Stores the profile in the ESDL model itself, in contrast with an external profile, which refers to an external source for a profile"""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ExternalProfile(GenericProfile):
    """ExternalProfile allows to refer to an externally defined profile. Common uses are a profile defined in a (timeseries) database such as InfluxDB.
It allows you to specify a multiplier to scale the supplied external profile by a certain factor (e.g. when using NEDU profiles). Default the multiplier is '1'."""
    multiplier = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=1.0)

    def __init__(self, *, multiplier=None, **kwargs):

        super().__init__(**kwargs)

        if multiplier is not None:
            self.multiplier = multiplier


class PercentileDistribution(GenericDistribution):

    percentile = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, percentile=None, **kwargs):

        super().__init__(**kwargs)

        if percentile:
            self.percentile.extend(percentile)


@abstract
class LabelDistribution(GenericDistribution):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SymetricVariance(AbstractVariance):

    sigma = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, sigma=None, **kwargs):

        super().__init__(**kwargs)

        if sigma is not None:
            self.sigma = sigma


class AssymetricVariance(AbstractVariance):

    sigmaMin = EAttribute(eType=EDouble, derived=False, changeable=True)
    sigmaPlus = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, sigmaMin=None, sigmaPlus=None, **kwargs):

        super().__init__(**kwargs)

        if sigmaMin is not None:
            self.sigmaMin = sigmaMin

        if sigmaPlus is not None:
            self.sigmaPlus = sigmaPlus


class DoubleAssymetricVariance(AbstractVariance):

    plus34perc = EAttribute(eType=EDouble, derived=False, changeable=True)
    plus48perc = EAttribute(eType=EDouble, derived=False, changeable=True)
    min34perc = EAttribute(eType=EDouble, derived=False, changeable=True)
    min48perc = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, plus34perc=None, plus48perc=None, min34perc=None, min48perc=None, **kwargs):

        super().__init__(**kwargs)

        if plus34perc is not None:
            self.plus34perc = plus34perc

        if plus48perc is not None:
            self.plus48perc = plus48perc

        if min34perc is not None:
            self.min34perc = min34perc

        if min48perc is not None:
            self.min48perc = min48perc


class Line(Geometry):

    point = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, point=None, **kwargs):

        super().__init__(**kwargs)

        if point:
            self.point.extend(point)


@abstract
class Commodity(Carrier):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DataSource(AbstractDataSource):

    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    reference = EAttribute(eType=EString, derived=False, changeable=True)
    attribution = EAttribute(eType=EString, derived=False, changeable=True)
    releaseDate = EAttribute(eType=EDate, derived=False, changeable=True)
    version = EAttribute(eType=EString, derived=False, changeable=True)
    licence = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, id=None, name=None, description=None, reference=None, attribution=None, releaseDate=None, version=None, licence=None, **kwargs):

        super().__init__(**kwargs)

        if id is not None:
            self.id = id

        if name is not None:
            self.name = name

        if description is not None:
            self.description = description

        if reference is not None:
            self.reference = reference

        if attribution is not None:
            self.attribution = attribution

        if releaseDate is not None:
            self.releaseDate = releaseDate

        if version is not None:
            self.version = version

        if licence is not None:
            self.licence = licence


class MultiPolygon(Geometry):

    polygon = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, polygon=None, **kwargs):

        super().__init__(**kwargs)

        if polygon:
            self.polygon.extend(polygon)


class QuantityAndUnitType(AbstractQuantityAndUnit):

    physicalQuantity = EAttribute(eType=PhysicalQuantityEnum, derived=False, changeable=True)
    multiplier = EAttribute(eType=MultiplierEnum, derived=False, changeable=True)
    unit = EAttribute(eType=UnitEnum, derived=False, changeable=True)
    perMultiplier = EAttribute(eType=MultiplierEnum, derived=False, changeable=True)
    perUnit = EAttribute(eType=UnitEnum, derived=False, changeable=True)
    description = EAttribute(eType=EString, derived=False, changeable=True)
    perTimeUnit = EAttribute(eType=TimeUnit, derived=False, changeable=True)
    id = EAttribute(eType=EString, derived=False, changeable=True, iD=True)

    def __init__(self, *, physicalQuantity=None, multiplier=None, unit=None, perMultiplier=None, perUnit=None, description=None, perTimeUnit=None, id=None, **kwargs):

        super().__init__(**kwargs)

        if physicalQuantity is not None:
            self.physicalQuantity = physicalQuantity

        if multiplier is not None:
            self.multiplier = multiplier

        if unit is not None:
            self.unit = unit

        if perMultiplier is not None:
            self.perMultiplier = perMultiplier

        if perUnit is not None:
            self.perUnit = perUnit

        if description is not None:
            self.description = description

        if perTimeUnit is not None:
            self.perTimeUnit = perTimeUnit

        if id is not None:
            self.id = id


class DataSourceReference(AbstractDataSource):

    reference = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class QuantityAndUnitReference(AbstractQuantityAndUnit):

    reference = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, reference=None, **kwargs):

        super().__init__(**kwargs)

        if reference is not None:
            self.reference = reference


class StringParameter(Parameters):

    value = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class DoubleParameter(Parameters):

    value = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class IntegerParameter(Parameters):

    value = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BooleanParameter(Parameters):

    value = EAttribute(eType=EBoolean, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class MultiLine(Geometry):

    line = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, line=None, **kwargs):

        super().__init__(**kwargs)

        if line:
            self.line.extend(line)


class InstanceDate(AbstractInstanceDate):

    date = EAttribute(eType=EDate, derived=False, changeable=True)

    def __init__(self, *, date=None, **kwargs):

        super().__init__(**kwargs)

        if date is not None:
            self.date = date


class InstancePeriod(AbstractInstanceDate):

    fromDate = EAttribute(eType=EDate, derived=False, changeable=True)
    toDate = EAttribute(eType=EDate, derived=False, changeable=True)

    def __init__(self, *, fromDate=None, toDate=None, **kwargs):

        super().__init__(**kwargs)

        if fromDate is not None:
            self.fromDate = fromDate

        if toDate is not None:
            self.toDate = toDate


class WKT(Geometry):
    """Well-Known Text (see https://en.wikipedia.org/wiki/Well-known_text)"""
    value = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class WKB(Geometry):
    """Well-Known Binary (See https://en.wikipedia.org/wiki/Well-known_text#Well-known_binary)"""
    value = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


@abstract
class EnergyAsset(Asset):

    port = EReference(ordered=True, unique=True, containment=True, upper=-1)
    controlStrategy = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, port=None, controlStrategy=None, **kwargs):

        super().__init__(**kwargs)

        if port:
            self.port.extend(port)

        if controlStrategy is not None:
            self.controlStrategy = controlStrategy


class Insulation(Asset):

    thermalInsulation = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, thermalInsulation=None, **kwargs):

        super().__init__(**kwargs)

        if thermalInsulation is not None:
            self.thermalInsulation = thermalInsulation


class LegalArea(Potential):

    purpose = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, purpose=None, **kwargs):

        super().__init__(**kwargs)

        if purpose is not None:
            self.purpose = purpose


@abstract
class EnergyService(Service):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractBuilding(Asset):

    energyLabel = EAttribute(eType=EnergyLabelEnum, derived=False, changeable=True)
    energyIndex = EAttribute(eType=EDouble, derived=False, changeable=True)
    asset = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, energyLabel=None, asset=None, energyIndex=None, **kwargs):

        super().__init__(**kwargs)

        if energyLabel is not None:
            self.energyLabel = energyLabel

        if energyIndex is not None:
            self.energyIndex = energyIndex

        if asset:
            self.asset.extend(asset)


class WindPotential(Potential):

    value = EAttribute(eType=EDouble, derived=False, changeable=True)
    height = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, value=None, height=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if height is not None:
            self.height = height


class DateTimeProfile(StaticProfile):
    """Describes a profile using one or more Profile elements. Each element defines a from- and a to-datetime and a value which is valid for this range. The to-field may be ommitted, meaning this value is valid for all time after the to-date."""
    element = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, element=None, **kwargs):

        super().__init__(**kwargs)

        if element:
            self.element.extend(element)


class SingleValue(StaticProfile):
    """A profile used to define a single value. This should be used when no information is present about the time. E.g. the price of a PV panel as currently known
When a model queries for a value from a certain date (and to a certain date), that information will be ignored and it will always return this value."""
    value = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class StringLabelDistribution(LabelDistribution):

    stringPerc = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, stringPerc=None, **kwargs):

        super().__init__(**kwargs)

        if stringPerc:
            self.stringPerc.extend(stringPerc)


class EnergyLabelDistribution(LabelDistribution):

    labelPerc = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, labelPerc=None, **kwargs):

        super().__init__(**kwargs)

        if labelPerc:
            self.labelPerc.extend(labelPerc)


class FromToDistribution(LabelDistribution):

    fromToPerc = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, fromToPerc=None, **kwargs):

        super().__init__(**kwargs)

        if fromToPerc:
            self.fromToPerc.extend(fromToPerc)


class URIProfile(ExternalProfile):
    """Describes a reference to a profile in an information system using a URI (e.g. a URI to a profile in Energy Information System (EIS))"""
    URI = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, URI=None, **kwargs):

        super().__init__(**kwargs)

        if URI is not None:
            self.URI = URI


@abstract
class DatabaseProfile(ExternalProfile):
    """Describes the fields of a generic database-based profile"""
    host = EAttribute(eType=EString, derived=False, changeable=True)
    port = EAttribute(eType=EInt, derived=False, changeable=True)
    database = EAttribute(eType=EString, derived=False, changeable=True)
    filters = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, host=None, port=None, database=None, filters=None, **kwargs):

        super().__init__(**kwargs)

        if host is not None:
            self.host = host

        if port is not None:
            self.port = port

        if database is not None:
            self.database = database

        if filters is not None:
            self.filters = filters


class GasCommodity(Commodity):

    pressure = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, pressure=None, **kwargs):

        super().__init__(**kwargs)

        if pressure is not None:
            self.pressure = pressure


class HeatCommodity(Commodity):

    supplyTemperature = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    returnTemperature = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, supplyTemperature=None, returnTemperature=None, **kwargs):

        super().__init__(**kwargs)

        if supplyTemperature is not None:
            self.supplyTemperature = supplyTemperature

        if returnTemperature is not None:
            self.returnTemperature = returnTemperature


class ElectricityCommodity(Commodity):

    voltage = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, voltage=None, **kwargs):

        super().__init__(**kwargs)

        if voltage is not None:
            self.voltage = voltage


class Range(StaticProfile):

    minValue = EAttribute(eType=EDouble, derived=False, changeable=True)
    maxValue = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, minValue=None, maxValue=None, **kwargs):

        super().__init__(**kwargs)

        if minValue is not None:
            self.minValue = minValue

        if maxValue is not None:
            self.maxValue = maxValue


class SolarPotential(Potential):

    value = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    SolarPotentialType = EAttribute(eType=PVInstallationTypeEnum, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, value=None, SolarPotentialType=None, fullLoadHours=None, area=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if SolarPotentialType is not None:
            self.SolarPotentialType = SolarPotentialType

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area


class ProfileReference(StaticProfile):

    multiplier = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=1.0)
    reference = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, multiplier=None, reference=None, **kwargs):

        super().__init__(**kwargs)

        if multiplier is not None:
            self.multiplier = multiplier

        if reference is not None:
            self.reference = reference


class ResidualHeatSourcePotential(Potential):

    value = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    type = EAttribute(eType=ResidualHeatSourceTypeEnum, derived=False, changeable=True)
    associatedConversionAsset = EReference(ordered=True, unique=True, containment=False)
    residualHeatSource = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, value=None, type=None, associatedConversionAsset=None, residualHeatSource=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if type is not None:
            self.type = type

        if associatedConversionAsset is not None:
            self.associatedConversionAsset = associatedConversionAsset

        if residualHeatSource is not None:
            self.residualHeatSource = residualHeatSource


class EnergyCommodity(Commodity):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractGTPotential(Potential):

    geothermalSource = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, geothermalSource=None, **kwargs):

        super().__init__(**kwargs)

        if geothermalSource:
            self.geothermalSource.extend(geothermalSource)


class UTESPotential(Potential):

    value = EAttribute(eType=EDouble, derived=False, changeable=True)
    type = EAttribute(eType=UTESPotentialTypeEnum, derived=False, changeable=True)
    UTES = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, value=None, type=None, UTES=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if type is not None:
            self.type = type

        if UTES:
            self.UTES.extend(UTES)


class BiomassPotential(Potential):

    value = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class Glass(Asset):

    uWindow = EAttribute(eType=EDouble, derived=False, changeable=True)
    glasType = EAttribute(eType=GlasTypeEnum, derived=False, changeable=True,
                          default_value=GlasTypeEnum.UNDEFINED)

    def __init__(self, *, uWindow=None, glasType=None, **kwargs):

        super().__init__(**kwargs)

        if uWindow is not None:
            self.uWindow = uWindow

        if glasType is not None:
            self.glasType = glasType


class SearchAreaWind(Potential):

    fullLoadHours = EAttribute(eType=EInt, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, fullLoadHours=None, area=None, **kwargs):

        super().__init__(**kwargs)

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area


class SearchAreaSolar(Potential):

    fullLoadHours = EAttribute(eType=EInt, derived=False, changeable=True)
    area = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, fullLoadHours=None, area=None, **kwargs):

        super().__init__(**kwargs)

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if area is not None:
            self.area = area


@abstract
class Producer(EnergyAsset):

    prodType = EAttribute(eType=RenewableTypeEnum, derived=False,
                          changeable=True, default_value=RenewableTypeEnum.RENEWABLE)
    operationalHours = EAttribute(eType=EInt, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, derived=False, changeable=True)
    power = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, prodType=None, operationalHours=None, fullLoadHours=None, power=None, **kwargs):

        super().__init__(**kwargs)

        if prodType is not None:
            self.prodType = prodType

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if power is not None:
            self.power = power


@abstract
class Consumer(EnergyAsset):

    consType = EAttribute(eType=ConsTypeEnum, derived=False, changeable=True,
                          default_value=ConsTypeEnum.PRIMARY)
    power = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, consType=None, power=None, **kwargs):

        super().__init__(**kwargs)

        if consType is not None:
            self.consType = consType

        if power is not None:
            self.power = power


@abstract
class Storage(EnergyAsset):

    capacity = EAttribute(eType=EDouble, derived=False, changeable=True)
    chargeEfficiency = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    dischargeEfficiency = EAttribute(eType=EDouble, derived=False,
                                     changeable=True, default_value=0.0)
    selfDischargeRate = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    fillLevel = EAttribute(eType=EDouble, derived=False, changeable=True)
    maxChargeRate = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    maxDischargeRate = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    profile = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, capacity=None, chargeEfficiency=None, profile=None, dischargeEfficiency=None, selfDischargeRate=None, fillLevel=None, maxChargeRate=None, maxDischargeRate=None, **kwargs):

        super().__init__(**kwargs)

        if capacity is not None:
            self.capacity = capacity

        if chargeEfficiency is not None:
            self.chargeEfficiency = chargeEfficiency

        if dischargeEfficiency is not None:
            self.dischargeEfficiency = dischargeEfficiency

        if selfDischargeRate is not None:
            self.selfDischargeRate = selfDischargeRate

        if fillLevel is not None:
            self.fillLevel = fillLevel

        if maxChargeRate is not None:
            self.maxChargeRate = maxChargeRate

        if maxDischargeRate is not None:
            self.maxDischargeRate = maxDischargeRate

        if profile is not None:
            self.profile = profile


@abstract
class Conversion(EnergyAsset):
    """Conversion Capability"""
    efficiency = EAttribute(eType=EDouble, derived=False, changeable=True)
    operationalHours = EAttribute(eType=EInt, derived=False, changeable=True)
    fullLoadHours = EAttribute(eType=EInt, derived=False, changeable=True)
    power = EAttribute(eType=EDouble, derived=False, changeable=True)
    residualHeatSourcePotential = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, efficiency=None, operationalHours=None, fullLoadHours=None, power=None, residualHeatSourcePotential=None, **kwargs):

        super().__init__(**kwargs)

        if efficiency is not None:
            self.efficiency = efficiency

        if operationalHours is not None:
            self.operationalHours = operationalHours

        if fullLoadHours is not None:
            self.fullLoadHours = fullLoadHours

        if power is not None:
            self.power = power

        if residualHeatSourcePotential is not None:
            self.residualHeatSourcePotential = residualHeatSourcePotential


@abstract
class Transport(EnergyAsset):

    capacity = EAttribute(eType=EDouble, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, capacity=None, efficiency=None, **kwargs):

        super().__init__(**kwargs)

        if capacity is not None:
            self.capacity = capacity

        if efficiency is not None:
            self.efficiency = efficiency


class BuildingUnit(AbstractBuilding):

    type = EAttribute(eType=BuildingTypeEnum, derived=False, changeable=True)
    housingType = EAttribute(eType=HousingTypeEnum, derived=False, changeable=True)
    numberOfInhabitants = EAttribute(eType=EInt, derived=False, changeable=True)
    inhabitantsType = EAttribute(eType=InhabitantsTypeEnum, derived=False, changeable=True)
    floorArea = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, type=None, housingType=None, numberOfInhabitants=None, inhabitantsType=None, floorArea=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if housingType is not None:
            self.housingType = housingType

        if numberOfInhabitants is not None:
            self.numberOfInhabitants = numberOfInhabitants

        if inhabitantsType is not None:
            self.inhabitantsType = inhabitantsType

        if floorArea is not None:
            self.floorArea = floorArea


class Building(AbstractBuilding):

    buildingYear = EAttribute(eType=EInt, derived=False, changeable=True)
    residentialBuildingType = EAttribute(
        eType=ResidentialBuildingTypeEnum, derived=False, changeable=True)
    floorArea = EAttribute(eType=EDouble, derived=False, changeable=True)
    numberOfFloors = EAttribute(eType=EInt, derived=False, changeable=True)
    slantedRoofArea = EAttribute(eType=EDouble, derived=False, changeable=True)
    flatRoofArea = EAttribute(eType=EDouble, derived=False, changeable=True)
    roofType = EAttribute(eType=RoofTypeEnum, derived=False, changeable=True)
    wallArea = EAttribute(eType=EDouble, derived=False, changeable=True)
    windowArea = EAttribute(eType=EDouble, derived=False, changeable=True)
    perimeter = EAttribute(eType=EDouble, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, derived=False, changeable=True)
    rcFloor = EAttribute(eType=EDouble, derived=False, changeable=True)
    rcWall = EAttribute(eType=EDouble, derived=False, changeable=True)
    rcRoof = EAttribute(eType=EDouble, derived=False, changeable=True)
    uWindow = EAttribute(eType=EDouble, derived=False, changeable=True)
    orientation = EAttribute(eType=EInt, derived=False, changeable=True)
    glasType = EAttribute(eType=GlasTypeEnum, derived=False, changeable=True)
    ventilationType = EAttribute(eType=VentilationTypeEnum, derived=False, changeable=True)

    def __init__(self, *, buildingYear=None, residentialBuildingType=None, floorArea=None, numberOfFloors=None, slantedRoofArea=None, flatRoofArea=None, roofType=None, wallArea=None, windowArea=None, perimeter=None, height=None, rcFloor=None, rcWall=None, rcRoof=None, uWindow=None, orientation=None, glasType=None, ventilationType=None, **kwargs):

        super().__init__(**kwargs)

        if buildingYear is not None:
            self.buildingYear = buildingYear

        if residentialBuildingType is not None:
            self.residentialBuildingType = residentialBuildingType

        if floorArea is not None:
            self.floorArea = floorArea

        if numberOfFloors is not None:
            self.numberOfFloors = numberOfFloors

        if slantedRoofArea is not None:
            self.slantedRoofArea = slantedRoofArea

        if flatRoofArea is not None:
            self.flatRoofArea = flatRoofArea

        if roofType is not None:
            self.roofType = roofType

        if wallArea is not None:
            self.wallArea = wallArea

        if windowArea is not None:
            self.windowArea = windowArea

        if perimeter is not None:
            self.perimeter = perimeter

        if height is not None:
            self.height = height

        if rcFloor is not None:
            self.rcFloor = rcFloor

        if rcWall is not None:
            self.rcWall = rcWall

        if rcRoof is not None:
            self.rcRoof = rcRoof

        if uWindow is not None:
            self.uWindow = uWindow

        if orientation is not None:
            self.orientation = orientation

        if glasType is not None:
            self.glasType = glasType

        if ventilationType is not None:
            self.ventilationType = ventilationType


class GeothermalPotential(AbstractGTPotential):

    temperature = EAttribute(eType=EInt, derived=False, changeable=True)
    depth = EAttribute(eType=EInt, derived=False, changeable=True)
    potential = EAttribute(eType=GeothermalPotentialEnum, derived=False, changeable=True)
    powerPerDoublet = EAttribute(eType=GeothermalPowerEnum, derived=False,
                                 changeable=True, default_value=GeothermalPowerEnum.UNKNOWN)

    def __init__(self, *, temperature=None, depth=None, potential=None, powerPerDoublet=None, **kwargs):

        super().__init__(**kwargs)

        if temperature is not None:
            self.temperature = temperature

        if depth is not None:
            self.depth = depth

        if potential is not None:
            self.potential = potential

        if powerPerDoublet is not None:
            self.powerPerDoublet = powerPerDoublet


class DemandResponseService(EnergyService):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatorService(EnergyService):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatedBuilding(AbstractBuilding):

    numberOfBuildings = EAttribute(eType=EInt, derived=False, changeable=True)
    residentialBuildingType = EAttribute(eType=ResidentialBuildingTypeEnum, derived=False,
                                         changeable=True, default_value=ResidentialBuildingTypeEnum.UNDEFINED)
    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)
    energyLabelDistribution = EReference(ordered=True, unique=True, containment=True)
    buildingYearDistribution = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, aggregationOf=None, numberOfBuildings=None, energyLabelDistribution=None, buildingYearDistribution=None, residentialBuildingType=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfBuildings is not None:
            self.numberOfBuildings = numberOfBuildings

        if residentialBuildingType is not None:
            self.residentialBuildingType = residentialBuildingType

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)

        if energyLabelDistribution is not None:
            self.energyLabelDistribution = energyLabelDistribution

        if buildingYearDistribution is not None:
            self.buildingYearDistribution = buildingYearDistribution


class InfluxDBProfile(DatabaseProfile):
    """Describes a profile based on a measurement and field as part of an InfluxDB timeseries query"""
    measurement = EAttribute(eType=EString, derived=False, changeable=True)
    field = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, measurement=None, field=None, **kwargs):

        super().__init__(**kwargs)

        if measurement is not None:
            self.measurement = measurement

        if field is not None:
            self.field = field


@abstract
class ControlStrategy(EnergyService):

    energyAsset = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, energyAsset=None, **kwargs):

        super().__init__(**kwargs)

        if energyAsset is not None:
            self.energyAsset = energyAsset


class EnergyMarket(EnergyService):

    asset = EReference(ordered=True, unique=True, containment=False, upper=-1)
    carrier = EReference(ordered=True, unique=True, containment=False)
    parameters = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, asset=None, carrier=None, parameters=None, **kwargs):

        super().__init__(**kwargs)

        if asset:
            self.asset.extend(asset)

        if carrier is not None:
            self.carrier = carrier

        if parameters:
            self.parameters.extend(parameters)


class GeothermalEnergyPotential(AbstractGTPotential):

    depth = EAttribute(eType=EInt, derived=False, changeable=True)
    value = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)

    def __init__(self, *, depth=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if depth is not None:
            self.depth = depth

        if value is not None:
            self.value = value


class WindTurbine(Producer):

    rotorDiameter = EAttribute(eType=EDouble, derived=False, changeable=True)
    height = EAttribute(eType=EDouble, derived=False, changeable=True)
    type = EAttribute(eType=WindTurbineTypeEnum, derived=False, changeable=True)

    def __init__(self, *, rotorDiameter=None, height=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if rotorDiameter is not None:
            self.rotorDiameter = rotorDiameter

        if height is not None:
            self.height = height

        if type is not None:
            self.type = type


class PVPanel(Producer):

    panelEfficiency = EAttribute(eType=EDouble, derived=False, changeable=True)
    inverterEfficiency = EAttribute(eType=EDouble, derived=False, changeable=True)
    angle = EAttribute(eType=EInt, derived=False, changeable=True)
    orientation = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, panelEfficiency=None, inverterEfficiency=None, angle=None, orientation=None, **kwargs):

        super().__init__(**kwargs)

        if panelEfficiency is not None:
            self.panelEfficiency = panelEfficiency

        if inverterEfficiency is not None:
            self.inverterEfficiency = inverterEfficiency

        if angle is not None:
            self.angle = angle

        if orientation is not None:
            self.orientation = orientation


class Battery(Storage):

    maxChargeDischargeCycles = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, maxChargeDischargeCycles=None, **kwargs):

        super().__init__(**kwargs)

        if maxChargeDischargeCycles is not None:
            self.maxChargeDischargeCycles = maxChargeDischargeCycles


class AggregatedConsumer(Consumer):

    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class AggregatedProducer(Producer):

    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class GenericConsumer(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericProducer(Producer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericStorage(Storage):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericTransport(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GenericConversion(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AggregatedTransport(Transport):

    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class AggregatedConversion(Conversion):

    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class AggregatedStorage(Storage):

    aggregationOf = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, aggregationOf=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationOf:
            self.aggregationOf.extend(aggregationOf)


class HeatStorage(Storage):

    minStorageTemperature = EAttribute(eType=EDouble, derived=False, changeable=True)
    maxStorageTemperature = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, minStorageTemperature=None, maxStorageTemperature=None, **kwargs):

        super().__init__(**kwargs)

        if minStorageTemperature is not None:
            self.minStorageTemperature = minStorageTemperature

        if maxStorageTemperature is not None:
            self.maxStorageTemperature = maxStorageTemperature


class GasHeater(Conversion):

    minimumBurnRate = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    type = EAttribute(eType=GasHeaterTypeEnum, derived=False, changeable=True)

    def __init__(self, *, minimumBurnRate=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if minimumBurnRate is not None:
            self.minimumBurnRate = minimumBurnRate

        if type is not None:
            self.type = type


class SourceProducer(Producer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SinkConsumer(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GeothermalSource(Producer):

    wellDepth = EAttribute(eType=EDouble, derived=False, changeable=True)
    geothermalSourceType = EAttribute(eType=GeothermalSourceTypeEnum,
                                      derived=False, changeable=True)
    COP = EAttribute(eType=EDouble, derived=False, changeable=True)
    aquiferTemperature = EAttribute(eType=EDouble, derived=False, changeable=True)
    flowRate = EAttribute(eType=EDouble, derived=False, changeable=True)
    pumpPower = EAttribute(eType=EDouble, derived=False, changeable=True)
    geothermalPotential = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, wellDepth=None, geothermalSourceType=None, COP=None, aquiferTemperature=None, flowRate=None, pumpPower=None, geothermalPotential=None, **kwargs):

        super().__init__(**kwargs)

        if wellDepth is not None:
            self.wellDepth = wellDepth

        if geothermalSourceType is not None:
            self.geothermalSourceType = geothermalSourceType

        if COP is not None:
            self.COP = COP

        if aquiferTemperature is not None:
            self.aquiferTemperature = aquiferTemperature

        if flowRate is not None:
            self.flowRate = flowRate

        if pumpPower is not None:
            self.pumpPower = pumpPower

        if geothermalPotential is not None:
            self.geothermalPotential = geothermalPotential


@abstract
class CoGeneration(Conversion):

    heatEfficiency = EAttribute(eType=EDouble, derived=False, changeable=True, default_value=0.0)
    electricalEfficiency = EAttribute(eType=EDouble, derived=False,
                                      changeable=True, default_value=0.0)
    HERatio = EAttribute(eType=EDouble, derived=False, changeable=True)
    fuelType = EAttribute(eType=PowerPlantFuelEnum, derived=False, changeable=True)
    leadCommodity = EAttribute(eType=CommodityEnum, derived=False, changeable=True)
    energyCarrier = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, heatEfficiency=None, electricalEfficiency=None, energyCarrier=None, HERatio=None, fuelType=None, leadCommodity=None, **kwargs):

        super().__init__(**kwargs)

        if heatEfficiency is not None:
            self.heatEfficiency = heatEfficiency

        if electricalEfficiency is not None:
            self.electricalEfficiency = electricalEfficiency

        if HERatio is not None:
            self.HERatio = HERatio

        if fuelType is not None:
            self.fuelType = fuelType

        if leadCommodity is not None:
            self.leadCommodity = leadCommodity

        if energyCarrier is not None:
            self.energyCarrier = energyCarrier


class HeatPump(Conversion):

    source = EAttribute(eType=SourceTypeEnum, derived=False, changeable=True)
    stages = EAttribute(eType=EInt, derived=False, changeable=True, default_value=1)
    COP = EAttribute(eType=EDouble, derived=False, changeable=True)
    additionalHeatingSourceType = EAttribute(
        eType=AdditionalHeatingSourceTypeEnum, derived=False, changeable=True)

    def __init__(self, *, source=None, stages=None, COP=None, additionalHeatingSourceType=None, **kwargs):

        super().__init__(**kwargs)

        if source is not None:
            self.source = source

        if stages is not None:
            self.stages = stages

        if COP is not None:
            self.COP = COP

        if additionalHeatingSourceType is not None:
            self.additionalHeatingSourceType = additionalHeatingSourceType


class HeatingDemand(Consumer):

    type = EAttribute(eType=HeatDemandTypeEnum, derived=False, changeable=True)
    deviceType = EAttribute(eType=HeatRadiationDeviceTypeEnum, derived=False, changeable=True)

    def __init__(self, *, type=None, deviceType=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if deviceType is not None:
            self.deviceType = deviceType


class ElectricityDemand(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GasDemand(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PowerPlant(Conversion):

    fuel = EAttribute(eType=PowerPlantFuelEnum, derived=False, changeable=True)
    maxLoad = EAttribute(eType=EInt, derived=False, changeable=True)
    minLoad = EAttribute(eType=EInt, derived=False, changeable=True)
    effMaxLoad = EAttribute(eType=EDouble, derived=False, changeable=True)
    effMinLoad = EAttribute(eType=EDouble, derived=False, changeable=True)
    energyCarrier = EReference(ordered=True, unique=True, containment=False)
    mustRun = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, fuel=None, maxLoad=None, minLoad=None, effMaxLoad=None, effMinLoad=None, energyCarrier=None, mustRun=None, **kwargs):

        super().__init__(**kwargs)

        if fuel is not None:
            self.fuel = fuel

        if maxLoad is not None:
            self.maxLoad = maxLoad

        if minLoad is not None:
            self.minLoad = minLoad

        if effMaxLoad is not None:
            self.effMaxLoad = effMaxLoad

        if effMinLoad is not None:
            self.effMinLoad = effMinLoad

        if energyCarrier is not None:
            self.energyCarrier = energyCarrier

        if mustRun is not None:
            self.mustRun = mustRun


class EVChargingStation(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Losses(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PowerToX(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CCS(Storage):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class XToPower(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CoolingDemand(Consumer):

    deviceType = EAttribute(eType=CoolingDeviceType, derived=False, changeable=True)

    def __init__(self, *, deviceType=None, **kwargs):

        super().__init__(**kwargs)

        if deviceType is not None:
            self.deviceType = deviceType


class Airco(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EnergyDemand(Consumer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SolarCollector(Producer):

    type = EAttribute(eType=SolarCollectorTypeEnum, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class ResidualHeatSource(Producer):

    type = EAttribute(eType=ResidualHeatSourceTypeEnum, derived=False, changeable=True)
    residualHeatSourcePotential = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, type=None, residualHeatSourcePotential=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if residualHeatSourcePotential is not None:
            self.residualHeatSourcePotential = residualHeatSourcePotential


class FermentationPlant(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class MobilityDemand(Consumer):

    type = EAttribute(eType=VehicleTypeEnum, derived=False, changeable=True, upper=-1)
    fuelType = EAttribute(eType=MobilityFuelTypeEnum, derived=False, changeable=True)
    distance = EAttribute(eType=EInt, derived=False, changeable=True)
    efficiency = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, type=None, fuelType=None, distance=None, efficiency=None, **kwargs):

        super().__init__(**kwargs)

        if type:
            self.type.extend(type)

        if fuelType is not None:
            self.fuelType = fuelType

        if distance is not None:
            self.distance = distance

        if efficiency is not None:
            self.efficiency = efficiency


class GasStorage(Storage):

    minStoragePressure = EAttribute(eType=EDouble, derived=False, changeable=True)
    maxStoragePressure = EAttribute(eType=EDouble, derived=False,
                                    changeable=True, default_value=0.0)

    def __init__(self, *, minStoragePressure=None, maxStoragePressure=None, **kwargs):

        super().__init__(**kwargs)

        if minStoragePressure is not None:
            self.minStoragePressure = minStoragePressure

        if maxStoragePressure is not None:
            self.maxStoragePressure = maxStoragePressure


class DrivenByDemand(ControlStrategy):

    outPort = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, outPort=None, **kwargs):

        super().__init__(**kwargs)

        if outPort is not None:
            self.outPort = outPort


class GasConversion(Conversion):

    type = EAttribute(eType=GasConversionTypeEnum, derived=False, changeable=True)
    outputPressure = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, type=None, outputPressure=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if outputPressure is not None:
            self.outputPressure = outputPressure


class DrivenBySupply(ControlStrategy):

    inPort = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, inPort=None, **kwargs):

        super().__init__(**kwargs)

        if inPort is not None:
            self.inPort = inPort


class DrivenByProfile(ControlStrategy):

    profile = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, profile=None, **kwargs):

        super().__init__(**kwargs)

        if profile is not None:
            self.profile = profile


class WaterToPower(Producer):

    type = EAttribute(eType=WaterToPowerTypeEnum, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class EnergyNetwork(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractConductor(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractSwitch(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractTransformer(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractConnection(Transport):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RoomHeater(Conversion):

    type = EAttribute(eType=RoomHeaterTypeEnum, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class BiomassHeater(Conversion):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class StorageStrategy(ControlStrategy):

    marginalChargeCosts = EReference(ordered=True, unique=True, containment=True)
    marginalDischargeCosts = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, marginalChargeCosts=None, marginalDischargeCosts=None, **kwargs):

        super().__init__(**kwargs)

        if marginalChargeCosts is not None:
            self.marginalChargeCosts = marginalChargeCosts

        if marginalDischargeCosts is not None:
            self.marginalDischargeCosts = marginalDischargeCosts


class CurtailmentStrategy(ControlStrategy):

    maxPower = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, maxPower=None, **kwargs):

        super().__init__(**kwargs)

        if maxPower is not None:
            self.maxPower = maxPower


class ElectricityNetwork(EnergyNetwork):

    voltage = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, voltage=None, **kwargs):

        super().__init__(**kwargs)

        if voltage is not None:
            self.voltage = voltage


class ElectricityCable(AbstractConductor):

    length = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, length=None, **kwargs):

        super().__init__(**kwargs)

        if length is not None:
            self.length = length


class HeatNetwork(EnergyNetwork):

    temperature = EAttribute(eType=EDouble, derived=False, changeable=True)
    temperatureMin = EAttribute(eType=EDouble, derived=False, changeable=True)
    temperatureMax = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, temperature=None, temperatureMin=None, temperatureMax=None, **kwargs):

        super().__init__(**kwargs)

        if temperature is not None:
            self.temperature = temperature

        if temperatureMin is not None:
            self.temperatureMin = temperatureMin

        if temperatureMax is not None:
            self.temperatureMax = temperatureMax


class GasNetwork(EnergyNetwork):

    pressure = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, pressure=None, **kwargs):

        super().__init__(**kwargs)

        if pressure is not None:
            self.pressure = pressure


class Pipe(AbstractConductor):

    diameter = EAttribute(eType=EDouble, derived=False, changeable=True)
    length = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, diameter=None, length=None, **kwargs):

        super().__init__(**kwargs)

        if diameter is not None:
            self.diameter = diameter

        if length is not None:
            self.length = length


class Transformer(AbstractTransformer):

    voltagePrimary = EAttribute(eType=EDouble, derived=False, changeable=True)
    voltageSecundary = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, voltagePrimary=None, voltageSecundary=None, **kwargs):

        super().__init__(**kwargs)

        if voltagePrimary is not None:
            self.voltagePrimary = voltagePrimary

        if voltageSecundary is not None:
            self.voltageSecundary = voltageSecundary


class HeatExchange(AbstractTransformer):

    LossDeltaT = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, LossDeltaT=None, **kwargs):

        super().__init__(**kwargs)

        if LossDeltaT is not None:
            self.LossDeltaT = LossDeltaT


class EConnection(AbstractConnection):

    EANCode = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, EANCode=None, **kwargs):

        super().__init__(**kwargs)

        if EANCode is not None:
            self.EANCode = EANCode


class HConnection(AbstractConnection):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class GConnection(AbstractConnection):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FuelCell(CoGeneration):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class WindParc(WindTurbine):

    numberOfTurbines = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, numberOfTurbines=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfTurbines is not None:
            self.numberOfTurbines = numberOfTurbines


class PVParc(PVPanel):

    numberOfPanels = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, numberOfPanels=None, **kwargs):

        super().__init__(**kwargs)

        if numberOfPanels is not None:
            self.numberOfPanels = numberOfPanels


class Pump(AbstractTransformer):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Valve(AbstractSwitch):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CHP(CoGeneration):

    CHPType = EAttribute(eType=CHPTypeEnum, derived=False, changeable=True)

    def __init__(self, *, CHPType=None, **kwargs):

        super().__init__(**kwargs)

        if CHPType is not None:
            self.CHPType = CHPType


class Electrolyzer(PowerToX):

    outputPressure = EAttribute(eType=EDouble, derived=False, changeable=True)

    def __init__(self, *, outputPressure=None, **kwargs):

        super().__init__(**kwargs)

        if outputPressure is not None:
            self.outputPressure = outputPressure


class PVInstallation(PVPanel):

    type = EAttribute(eType=PVInstallationTypeEnum, derived=False, changeable=True)
    numberOfPanels = EAttribute(eType=EInt, derived=False, changeable=True)

    def __init__(self, *, type=None, numberOfPanels=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if numberOfPanels is not None:
            self.numberOfPanels = numberOfPanels


class CircuitBraker(AbstractSwitch):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class UTES(HeatStorage):

    type = EAttribute(eType=UTESPotentialTypeEnum, derived=False, changeable=True)
    UTESPotential = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, type=None, UTESPotential=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if UTESPotential is not None:
            self.UTESPotential = UTESPotential


class WaterBuffer(HeatStorage):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Joint(AbstractConductor):
    """A Joint is a means to connect AbstractConductors. This helps when these conductors have opposite Ports."""

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
