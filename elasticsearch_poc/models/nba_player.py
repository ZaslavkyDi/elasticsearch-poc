import datetime
from typing import Any

from elasticsearch_poc.models.base_mapping_model import BaseMappingSchema


class NbaPlayerModel(BaseMappingSchema):
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    position: str
    team: str
    avg_scoring: float
    avg_rebound: float
    avg_assist: float
    country: str

    @classmethod
    def get_elastic_schema_mapping(cls) -> dict[str, Any]:
        return {
            "first_name": {"type": "text"},
            "last_name": {"type": "text"},
            "date_of_birth": {"type": "date"},
            "position": {"type": "keyword"},
            "team": {"type": "keyword"},
            "avg_scoring": {"type": "float"},
            "avg_rebound": {"type": "float"},
            "avg_assist": {"type": "float"},
            "country": {"type": "keyword"},
        }
