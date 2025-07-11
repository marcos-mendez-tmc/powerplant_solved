from app.PowerPlant.Domain.Entities.GasFired import GasFired
from app.PowerPlant.Domain.Entities.TurboJet import TurboJet
from app.PowerPlant.Domain.Entities.WindTurbine import WindTurbine
from app.PowerPlant.Domain.Entities.PowerPlant import PowerPlant


class PowerPlantFactory:
    @staticmethod
    def create(plant_data: dict) -> PowerPlant:
        type_map = {
            "gasfired": GasFired,
            "turbojet": TurboJet,
            "windturbine": WindTurbine
        }

        plant_type = plant_data.get("type")
        plant_class = type_map.get(plant_type.lower())

        if not plant_class:
            raise ValueError(f"Unknown powerplant type: {plant_type}")

        return plant_class(
            name=plant_data["name"],
            pmin=plant_data["pmin"],
            pmax=plant_data["pmax"],
            efficiency=plant_data["efficiency"]
        )
