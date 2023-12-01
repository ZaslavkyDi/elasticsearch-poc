from functools import lru_cache

from elasticsearch_poc.config.settings import ElasticSearchSettings


@lru_cache
def get_elastic_settings() -> ElasticSearchSettings:
    return ElasticSearchSettings()
