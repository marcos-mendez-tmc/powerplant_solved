from fastapi import FastAPI
from app.PowerPlant.Infrastructure.api.routes import routes

app = FastAPI(
    title="Powerplant Production Plan API",
    description="Calculates the optimal production distribution among power plants based on cost.",
    version="1.0.0"
)

app.include_router(routes.router, prefix="")
