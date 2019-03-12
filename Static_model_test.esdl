<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="mpoc">
  <instance aggrType="PER_COMMODITY" name="test instance">
    <area name="test area">
      <KPIs description="KPIs">
        <kpi name="KPI CO2-emissions" value="2002.0">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitReference" reference="mton"/>
        </kpi>
        <kpi name="KPI Total costs" value="77.28504945438456">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitReference" reference="meur"/>
        </kpi>
      </KPIs>
      <asset xsi:type="esdl:PVParc" commissioningDate="2019-03-06T15:04:39.459637" name="PV parc" id="pv_parc_1" numberOfPanels="10">
        <port xsi:type="esdl:OutPort" id="OutPort1" connectedTo="InPort1">
          <profile xsi:type="esdl:DateTimeProfile">
            <element to="2019-03-11T11:30:41.558907" from="2019-03-11T11:30:41.558907"/>
          </profile>
        </port>
      </asset>
      <asset xsi:type="esdl:ElectricityDemand" id="e_demand_1" name="E demand">
        <port xsi:type="esdl:InPort" id="InPort1" connectedTo="OutPort1"/>
      </asset>
    </area>
  </instance>
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units">
      <quantityAndUnit unit="PERCENT" description="%" id="percent"/>
      <quantityAndUnit description="Mton (CO2-emissions)" physicalQuantity="EMISSION" multiplier="MEGA" id="mton"/>
      <quantityAndUnit description="Mln euros (total costs)" physicalQuantity="COST" multiplier="MEGA" id="meur"/>
    </quantityAndUnits>
  </energySystemInformation>
</esdl:EnergySystem>
