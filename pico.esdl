<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="GemeenteHengelo">
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
  <instance>
    <area scope="MUNICIPALITY" id="GM0164" name="Hengelo">
      <KPIs description="KPIs" id="kpis">
        <kpi xsi:type="esdl:DoubleKPI" value="-0.0654541875300918" id="32722da2-82ad-4770-81ca-523aabc1b461" name="CO2-emissies">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" id="percent" description="%"/>
        </kpi>
        <kpi xsi:type="esdl:DoubleKPI" value="0.4210004700782711" id="6a38567f-c29d-46d9-8206-5c5415be8f38" name="Totale kosten">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" physicalQuantity="COST" id="meur" multiplier="MEGA" description="Meur"/>
        </kpi>
      </KPIs>
      <potential xsi:type="esdl:SearchAreaWind" area="6928000.0" fullLoadHours="2000"/>
    </area>
  </instance>
</esdl:EnergySystem>
