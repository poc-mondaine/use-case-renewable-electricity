<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance name="test instance" aggrType="PER_COMMODITY">
    <area name="test area">
      <asset xsi:type="esdl:PVParc" numberOfPanels="10" name="PV parc" commissioningDate="2019-03-12T16:48:21.071250">
        <port xsi:type="esdl:OutPort" id="OutPort1" connectedTo="InPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:WindTurbine" height="150.0" id="e3e1710a-1ece-44d2-8ad1-5b79ed5c666b" type="WIND_ON_LAND" power="2000000.0" surfaceArea="100" name="WindTurbine 4" fullLoadHours="2000"/>
      <KPIs description="KPIs">
        <kpi value="-0.27275086433850615" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Mton (CO2-emissions)" id="mton" multiplier="MEGA" physicalQuantity="EMISSION"/>
        </kpi>
        <kpi value="76.53071716808613" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Mln euros (total costs)" id="meur" multiplier="MEGA" physicalQuantity="COST"/>
        </kpi>
      </KPIs>
    </area>
  </instance>
</esdl:EnergySystem>
