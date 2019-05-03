<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance xsi:type="esdl:Instance" aggrType="PER_COMMODITY" name="test instance">
    <area xsi:type="esdl:Area" name="Groningen" id="PV20">
      <KPIs xsi:type="esdl:KPIs" description="KPIs">
        <kpi xsi:type="esdl:KPI" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" multiplier="MEGA" description="Mton (CO2-emissions)" id="mton" physicalQuantity="EMISSION"/>
        </kpi>
        <kpi xsi:type="esdl:KPI" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" multiplier="MEGA" description="Mln euros (total costs)" id="meur" physicalQuantity="COST"/>
        </kpi>
      </KPIs>
      <asset xsi:type="esdl:PVParc" name="PV parc" numberOfPanels="10" commissioningDate="2019-05-03T11:30:10.647240">
        <port xsi:type="esdl:OutPort" id="OutPort1" connectedTo="InPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:WindTurbine" height="150.0" surfaceArea="100" id="acdfca73-6399-4b47-9e08-437a80266cb9" name="WindTurbine 4" power="2000000.0" type="WIND_ON_LAND" fullLoadHours="2000"/>
      <potential xsi:type="esdl:SearchAreaWind" area="200000000.0" fullLoadHours="1920" id="122e5be4-ccdb-498f-9618-fe81ce2ff2bf" name="Search Area Wind"/>
      <potential xsi:type="esdl:SearchAreaSolar" fullLoadHours="867" id="2bf62514-b336-408e-8a58-2ea946f33323" area="200000000.0" name="Search Area Solar"/>
    </area>
  </instance>
</esdl:EnergySystem>
