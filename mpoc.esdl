<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance name="test instance" aggrType="PER_COMMODITY">
    <area id="PV20" name="Groningen">
      <potential xsi:type="esdl:SearchAreaWind" fullLoadHours="1920" area="200000000.0" name="Search Area Wind" id="a9c30d40-1f29-4848-857c-fea6c9269acf"/>
      <potential xsi:type="esdl:SearchAreaSolar" fullLoadHours="867" name="Search Area Solar" id="c2acb751-31a0-44f7-8068-99f318f99add" area="200000000.0"/>
      <asset xsi:type="esdl:PVParc" commissioningDate="2019-04-09T16:00:51.849049" name="PV parc" numberOfPanels="10">
        <port xsi:type="esdl:OutPort" id="OutPort1" connectedTo="InPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:WindTurbine" power="2000000.0" name="WindTurbine 4" id="a8dd4b98-ad89-47a6-8c44-e3c54789f491" surfaceArea="100" height="150.0" type="WIND_ON_LAND" fullLoadHours="2000"/>
      <KPIs description="KPIs">
        <kpi value="-0.15711043565376404" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" multiplier="MEGA" id="mton" description="Mton (CO2-emissions)" physicalQuantity="EMISSION"/>
        </kpi>
        <kpi value="4.055390314791163" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" multiplier="MEGA" id="meur" description="Mln euros (total costs)" physicalQuantity="COST"/>
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
