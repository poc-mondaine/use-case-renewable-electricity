<esdl:WindTurbine
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:esdl="http://www.tno.nl/esdl"
    xsi:schemaLocation="http://www.tno.nl/esdl ../../esdl/model/esdl.ecore"
    id="WTxxxx"
    name="WindTurbine aan de kust"
    description=""
    surfaceArea="200000"
    technicalLifetime="25.0"
    installationDuration="12.0"
    fullLoadHours="2550"
    power="3000000.0"
    rotorDiameter="100.0"
    height="150.0"
    type="WIND_ON_COAST">
  <costInformation>
    <investmentCosts
        xsi:type="esdl:SingleValue"
        name="Initial investment (excl CCS)"
        value="1391.99">
      <profileQuantityAndUnit
          xsi:type="esdl:QuantityAndUnitType"
          physicalQuantity="COST"
          multiplier="KILO"
          unit="EURO"
          perMultiplier="MEGA"
          perUnit="WATT"
          description="kEUR / MWe"/>
    </investmentCosts>
    <fixedOperationalAndMaintenanceCosts
        xsi:type="esdl:SingleValue"
        name="Fixed operation and maintenance costs (per year)"
        value="49.19">
      <profileQuantityAndUnit
          xsi:type="esdl:QuantityAndUnitType"
          physicalQuantity="COST"
          multiplier="KILO"
          unit="EURO"
          perMultiplier="MEGA"
          perUnit="WATT"
          description="kEUR / MWe / year"
          perTimeUnit="YEAR"/>
    </fixedOperationalAndMaintenanceCosts>
  </costInformation>
</esdl:WindTurbine>
