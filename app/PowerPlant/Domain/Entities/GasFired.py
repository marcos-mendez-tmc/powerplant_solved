from app.PowerPlant.Domain.Entities.PowerPlant import PowerPlant


class GasFired(PowerPlant):
    def calculate_cost(self, fuels: dict) -> float:
        gas_price = fuels.get("gas(euro/MWh)", 0)
        self.cost_per_mwh = round(gas_price / self.efficiency, 2)
        return self.cost_per_mwh

    def calculate_max_power(self, fuels: dict) -> float:
        self.actual_pmax = self.pmax
        return self.actual_pmax
