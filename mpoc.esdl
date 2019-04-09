<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance name="test instance" aggrType="PER_COMMODITY">
    <area name="test area">
      <asset xsi:type="esdl:PVParc" numberOfPanels="10" name="PV parc" commissioningDate="2019-04-09T13:17:03.126482">
        <port xsi:type="esdl:OutPort" connectedTo="InPort1" id="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:WindTurbine" name="WindTurbine 4" id="b61aced2-ee09-4743-b1be-ad751cd090b1" height="150.0" surfaceArea="100" fullLoadHours="2000" type="WIND_ON_LAND" power="2000000.0"/>
      <KPIs description="KPIs">
        <kpi value="-0.2727422468666646" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="EMISSION" multiplier="MEGA" description="Mton (CO2-emissions)" id="mton"/>
        </kpi>
        <kpi value="76.51888652588265" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="COST" multiplier="MEGA" description="Mln euros (total costs)" id="meur"/>
        </kpi>
      </KPIs>
    </area>
  </instance>
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units">
      <quantityAndUnit unit="PERCENT" description="%" id="percent"/>
    </quantityAndUnits>
  </energySystemInformation>
</esdl:EnergySystem>
