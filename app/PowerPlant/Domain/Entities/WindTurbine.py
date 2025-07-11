from app.PowerPlant.Domain.Entities.PowerPlant import PowerPlant


class WindTurbine(PowerPlant):
    def calculate_cost(self, fuels: dict) -> float:
        self.cost_per_mwh = 0.0
        return self.cost_per_mwh

    def calculate_max_power(self, fuels: dict) -> float:
        wind_percentage = fuels.get("wind(%)", 0)
        self.actual_pmax = round(self.pmax * wind_percentage / 100, 1)
        return self.actual_pmax
