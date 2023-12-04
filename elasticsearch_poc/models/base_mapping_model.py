import abc
from typing import Any

from pydantic import BaseModel


class BaseMappingSchema(BaseModel, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def get_elastic_schema_mapping(cls) -> dict[str, Any]:
        raise NotImplementedError
