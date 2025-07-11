from abc import ABC, abstractmethod
from typing import Optional


class PowerPlant(ABC):
    def __init__(self, name: str, efficiency: float, pmin: float, pmax: float):
        self.name = name
        self.efficiency = efficiency
        self.pmin = pmin
        self.pmax = pmax
        self.actual_pmax = pmax 
        self.cost_per_mwh: Optional[float] = None

    @abstractmethod
    def calculate_cost(self, fuels: dict) -> float:
        pass

    @abstractmethod
    def calculate_max_power(self, fuels: dict) -> float:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, cost={self.cost_per_mwh}, pmin={self.pmin}, pmax={self.actual_pmax})"
