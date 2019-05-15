<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="ProvincieGroningen">
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
  <instance>
    <area id="PV20" name="Groningen" scope="PROVINCE">
      <KPIs description="KPIs" id="kpis">
        <kpi xsi:type="esdl:DoubleKPI" name="KPI CO2-emissions" value="-0.427726175301844" id="733238ed-6d4c-4b00-8b57-2d11fad55e16">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="percent" description="%"/>
        </kpi>
        <kpi xsi:type="esdl:DoubleKPI" name="KPI Total costs" value="4.632566320836999" id="c8f10242-b8d9-45ec-b631-32c576b7b39c">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="meur" multiplier="MEGA" physicalQuantity="COST" description="Meur"/>
        </kpi>
      </KPIs>
      <potential xsi:type="esdl:SearchAreaWind" fullLoadHours="2000" area="881371500.0"/>
    </area>
  </instance>
</esdl:EnergySystem>
