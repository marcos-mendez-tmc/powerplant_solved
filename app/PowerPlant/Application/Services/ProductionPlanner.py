from typing import List
from app.PowerPlant.Domain.Entities.PowerPlant import PowerPlant
from app.PowerPlant.Domain.Factories.PowerPlantFactory import PowerPlantFactory


class ProductionPlanner:
    def __init__(self, payload: dict):
        self.load = payload["load"]
        self.fuels = payload["fuels"]
        self.powerplant_data = payload["powerplants"]
        self.plants: List[PowerPlant] = []

    def plan(self) -> List[dict]:
        self._instantiate_plants()
        self._calculate_costs_and_limits()
        return self._dispatch_production()

    def _instantiate_plants(self):
        for data in self.powerplant_data:
            plant = PowerPlantFactory.create(data)
            self.plants.append(plant)

    def _calculate_costs_and_limits(self):
        for plant in self.plants:
            plant.calculate_cost(self.fuels)
            plant.calculate_max_power(self.fuels)

        self.plants.sort(key=lambda p: p.cost_per_mwh)

    def _dispatch_production(self) -> List[dict]:
        remaining_load = round(self.load, 1)
        result = []

        for plant in self.plants:
            if remaining_load <= 0:
                result.append({"name": plant.name, "p": 0.0})
                continue

            pmin = plant.pmin
            pmax = plant.actual_pmax

            if remaining_load < pmin:
                result.append({"name": plant.name, "p": 0.0})
            else:
                production = round(min(pmax, max(pmin, remaining_load)), 1)
                result.append({"name": plant.name, "p": production})
                remaining_load = round(remaining_load - production, 1)

        total = round(sum(r["p"] for r in result), 1)
        if total != self.load:
            diff = round(self.load - total, 1)
            for r in reversed(result):
                if r["p"] > 0:
                    r["p"] = round(r["p"] + diff, 1)
                    break

        return result
