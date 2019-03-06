<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance aggrType="PER_COMMODITY" name="test instance">
    <area name="test area">
      <asset xsi:type="esdl:PVParc" commissioningDate="2019-03-06 15:04:39.459637" name="PV parc" numberOfPanels="10">
        <port xsi:type="esdl:OutPort" id="OutPort1" connectedTo="InPort1"/>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
      <KPIs description="KPIs">
        <kpi value="-0.2738493700251444" name="KPI CO2-emissions">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="EMISSION" id="mton" description="Mton (CO2-emissions)" multiplier="MEGA"/>
        </kpi>
        <kpi value="77.28504945438456" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="COST" id="meur" description="Mln euros (total costs)" multiplier="MEGA"/>
        </kpi>
      </KPIs>
    </area>
  </instance>
</esdl:EnergySystem>
