<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance name="test instance" aggrType="PER_COMMODITY">
    <area name="test area">
      <asset xsi:type="esdl:PVParc" commissioningDate="2019-03-06T15:04:39.459637" id="pv_parc_1" name="PV parc" numberOfPanels="10">
        <port xsi:type="esdl:OutPort" connectedTo="InPort1" id="OutPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="e_demand_1" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <KPIs description="KPIs">
        <kpi value="2000.0" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Mton (CO2-emissions)" physicalQuantity="EMISSION" multiplier="MEGA" id="mton"/>
        </kpi>
        <kpi value="77.28504945438456" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Mln euros (total costs)" physicalQuantity="COST" multiplier="MEGA" id="meur"/>
        </kpi>
      </KPIs>
    </area>
  </instance>
</esdl:EnergySystem>
