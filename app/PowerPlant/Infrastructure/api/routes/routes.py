from fastapi import APIRouter
from typing import List
from app.PowerPlant.Application.Services.ProductionPlanner import ProductionPlanner
from app.PowerPlant.Infrastructure.api.models.request import ProductionRequest
from app.PowerPlant.Infrastructure.api.models.response import PowerOutput

router = APIRouter()

@router.post("/productionplan", response_model=List[PowerOutput])
def production_plan(payload: ProductionRequest):
    planner = ProductionPlanner(payload.dict())
    result = planner.plan()
    return result
