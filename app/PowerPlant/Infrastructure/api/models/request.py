from pydantic import BaseModel
from typing import List, Dict


class PowerPlantPayload(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float


class ProductionRequest(BaseModel):
    load: float
    fuels: Dict[str, float]
    powerplants: List[PowerPlantPayload]
