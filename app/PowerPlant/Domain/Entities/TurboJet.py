from app.PowerPlant.Domain.Entities.PowerPlant import PowerPlant


class TurboJet(PowerPlant):
    def calculate_cost(self, fuels: dict) -> float:
        kerosine_price = fuels.get("kerosine(euro/MWh)", 0)
        self.cost_per_mwh = round(kerosine_price / self.efficiency, 2)
        return self.cost_per_mwh

    def calculate_max_power(self, fuels: dict) -> float:
        self.actual_pmax = self.pmax
        return self.actual_pmax
