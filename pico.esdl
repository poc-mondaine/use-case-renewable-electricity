<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="ProvincieGroningen">
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
  <instance>
    <area id="PV20" name="Groningen" scope="PROVINCE">
      <potential xsi:type="esdl:SearchAreaWind" area="881371500.0" fullLoadHours="2000"/>
      <KPIs description="KPIs" id="kpis">
        <kpi name="KPI CO2-emissions" value="-0.252326043564164">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="%" id="percent"/>
        </kpi>
        <kpi name="KPI Total costs" value="6.583739726930397">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Meur" physicalQuantity="COST" multiplier="MEGA" id="meur"/>
        </kpi>
      </KPIs>
    </area>
  </instance>
</esdl:EnergySystem>
