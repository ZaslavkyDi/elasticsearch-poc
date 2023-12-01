from elasticsearch import Elasticsearch


class ElasticSearchClient:
    def __init__(self) -> None:
        self.client = Elasticsearch()
