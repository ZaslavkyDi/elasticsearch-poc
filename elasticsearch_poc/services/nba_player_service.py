import json
from collections.abc import Iterable
from typing import Any

from elastic_transport import ObjectApiResponse

from elasticsearch_poc.elastic.client import ElasticSearchClient
from elasticsearch_poc.elastic.index_names import IndexName
from elasticsearch_poc.models.nba_player import NbaPlayerModel


class NbaPlayerService:
    def __init__(self, elastic_client: ElasticSearchClient) -> None:
        self._elastic_client = elastic_client

    def initialize_documents(self, file_path: str) -> Iterable[ObjectApiResponse]:
        players_data: list[dict[str, Any]] = self._load_data_from_json_file(file_path)

        for i, player in enumerate(players_data):
            player_model = NbaPlayerModel.model_validate(player)  # test mapping

            yield self._elastic_client.upsert_doc(
                index_name=IndexName.nba_players,
                doc=player_model,
                doc_id=i,
            )

    @staticmethod
    def _load_data_from_json_file(json_file_path: str) -> list[dict[str, Any]] | dict[str, Any]:
        if not json_file_path.endswith(".json"):
            raise ValueError(f"Method read only .json files. Given file: [{json_file_path}]")

        with open(json_file_path) as f:
            data: str = f.read()

        return json.loads(data)
