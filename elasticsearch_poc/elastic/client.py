from typing import Any

from elastic_transport import ObjectApiResponse
from elasticsearch import Elasticsearch, exceptions
from pydantic import BaseModel

from elasticsearch_poc.config import get_elastic_settings
from elasticsearch_poc.elastic.index_names import IndexName


class ElasticSearchClient:
    def __init__(self, index_name: IndexName) -> None:
        self.index_name = index_name
        self._connection = Elasticsearch(
            hosts=get_elastic_settings().https_url,
            ca_certs=get_elastic_settings().dev_http_ca_crt_path,
            basic_auth=(get_elastic_settings().user, get_elastic_settings().password),
        )

    def print_connection_info(self) -> None:
        print(self._connection.info())

    def create_index_if_not_exist(
        self, schema_mapping: dict[str, Any]
    ) -> ObjectApiResponse | None:
        body: dict[str, Any] = {
            "mappings": {
                "properties": schema_mapping,
            }
        }

        result: ObjectApiResponse | None = None
        try:
            result = self._connection.indices.create(
                index=self.index_name.value,
                body=body,
            )
        except exceptions.RequestError as ex:
            if ex.error == "resource_already_exists_exception":
                pass  # Index already exists. Ignore.
            else:  # Other exception - raise it
                raise ex

        return result

    def upsert_doc(
        self,
        doc: BaseModel | dict[str, Any],
        doc_id: str | int | None = None,
    ) -> ObjectApiResponse:
        if isinstance(doc, BaseModel):
            doc = doc.model_dump()

        return self._connection.index(
            index=self.index_name.value,
            document=doc,
            id=doc_id,
        )

    def update_doc(
        self,
        doc: BaseModel | dict[str, Any],
        doc_id: str | int,
    ) -> ObjectApiResponse:
        if isinstance(doc, BaseModel):
            doc = doc.model_dump()

        return self._connection.update(
            index=self.index_name.value,
            document=doc,
            id=doc_id,
        )

    def delete_doc_by_id(
        self,
        doc_id: str | int
    ) -> ObjectApiResponse:
        return self._connection.delete(
            index=self.index_name.value,
            id=doc_id,
        )
