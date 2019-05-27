<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="GemeenteAmeland">
  <instance>
    <area scope="MUNICIPALITY" id="GM0060" name="Ameland">
      <KPIs id="kpis" description="KPIs">
        <kpi xsi:type="esdl:DoubleKPI" value="-0.19233584491328337" id="eddb05ef-0db4-4735-baad-b9716516aa5f" name="KPI CO2-emissions reduction">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="EMISSION" unit="PERCENT" description="%" id="percent"/>
        </kpi>
        <kpi xsi:type="esdl:DoubleKPI" value="0.008190580527726931" id="c996833d-6ad0-4bec-804f-1c5b7d73a6cc" name="KPI Total costs">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="COST" unit="EURO" id="meur" multiplier="MEGA" description="Meur"/>
        </kpi>
      </KPIs>
      <potential xsi:type="esdl:SearchAreaWind" fullLoadHours="2000" area="649500.0"/>
    </area>
  </instance>
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
</esdl:EnergySystem>
