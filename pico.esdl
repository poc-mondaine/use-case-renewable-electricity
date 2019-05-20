<?xml version='1.0' encoding='UTF-8'?>
<esdl:EnergySystem xmlns:esdl="http://www.tno.nl/esdl" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="GemeenteAchtkarspelen">
  <instance>
    <area id="GM0059" name="Achtkarspelen" scope="MUNICIPALITY">
      <KPIs description="KPIs" id="kpis">
        <kpi xsi:type="esdl:DoubleKPI" name="KPI CO2-emissions" value="-0.3041855076767689" id="320504fe-8ec2-4f61-9fda-e4ac33eb83dd">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="%" id="percent"/>
        </kpi>
        <kpi xsi:type="esdl:DoubleKPI" name="KPI Total costs" value="0.09818138828637057" id="2324ca31-17af-4b5a-bf4a-c107f84664d9">
          <quantityAndUnit xsi:type="esdl:QuantityAndUnitType" description="Meur" physicalQuantity="COST" multiplier="MEGA" id="meur"/>
        </kpi>
      </KPIs>
      <potential xsi:type="esdl:SearchAreaWind" fullLoadHours="2000" area="18835500.0"/>
    </area>
  </instance>
  <energySystemInformation id="energy_system_information">
    <quantityAndUnits id="quantity_and_units"/>
  </energySystemInformation>
</esdl:EnergySystem>
