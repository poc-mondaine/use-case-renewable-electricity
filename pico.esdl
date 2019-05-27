<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="GemeenteHengelo">
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
  <instance>
    <area scope="MUNICIPALITY" id="GM0164" name="Hengelo">
      <KPIs description="KPIs" id="kpis">
        <kpi xsi:type="esdl:DoubleKPI" id="5b03afb2-70f7-4271-aa6d-2ac567ffee2c" name="KPI CO2-emissions" value="-0.00039110592849433967">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="%" id="percent"/>
        </kpi>
        <kpi xsi:type="esdl:DoubleKPI" id="9f5691c2-75a9-4af2-baff-edb57ffcdc72" name="KPI Total costs" value="0.40275764603710956">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Meur" physicalQuantity="COST" multiplier="MEGA" id="meur"/>
        </kpi>
      </KPIs>
      <potential xsi:type="esdl:SearchAreaWind" fullLoadHours="2000"/>
    </area>
  </instance>
</esdl:EnergySystem>
