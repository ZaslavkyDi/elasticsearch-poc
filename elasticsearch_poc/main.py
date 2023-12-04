import elasticsearch

from elasticsearch_poc.elastic.client import ElasticSearchClient
from elasticsearch_poc.elastic.index_names import IndexName
from elasticsearch_poc.models.nba_player import NbaPlayerModel
from elasticsearch_poc.services.nba_player_service import NbaPlayerService


def run_elastic_client() -> None:
    elastic_nba_client = ElasticSearchClient(index_name=IndexName.nba_players)
    created_index_resp = elastic_nba_client.create_index_if_not_exist(
        schema_mapping=NbaPlayerModel.get_elastic_schema_mapping(),
    )
    print(created_index_resp)

    response = elastic_nba_client.upsert_doc(
        doc={
            "first_name": "Nikola",
            "last_name": "Jokic",
            "date_of_birth": "1995-02-19",
            "position": "C",
            "team": "Nuggets",
            "avg_scoring": 25.8,
            "avg_rebound": 10.7,
            "avg_assist": 8.5,
            "country": "Serbia",
        },
        doc_id=0,
    )
    print(f"{response=}")

    response2 = elastic_nba_client.upsert_doc(
        doc={
            "first_name": "Nikola",
            "last_name": "Jokic",
            "date_of_birth": "1995-02-19",
            "position": "C",
            "team": "Nuggets",
            "avg_scoring": 25.8,
            "avg_rebound": 10.7,
            "avg_assist": 8.5,
            "country": "Serbia",
        },
    )
    print(f"{response2=}")

    response3 = elastic_nba_client.upsert_doc(
        doc_id=1,
        doc={
            "first_name": "Nikola",
            "last_name": "Tesla",
            "date_of_birth": "1995-02-19",
            "position": "C",
            "team": "Nuggets",
            "avg_scoring": 25.8,
            "avg_rebound": 10.7,
            "avg_assist": 8.5,
            "country": "Serbia",
        },
    )
    print(f"{response3=}")

    response4 = elastic_nba_client.delete_doc_by_id(doc_id=0)
    print(f"{response4=}")

    try:
        # delete not existing index
        elastic_nba_client.delete_doc_by_id(doc_id=1333333)
    except elasticsearch.NotFoundError:
        pass



def run_nba_player_service() -> None:
    service = NbaPlayerService(
        elastic_client=ElasticSearchClient()
    )
    for r in service.initialize_documents(file_path="../resources/list_of_nba_players.json"):
        print(f"{r=}")


def main() -> None:
    run_elastic_client()


if __name__ == "__main__":
    main()
