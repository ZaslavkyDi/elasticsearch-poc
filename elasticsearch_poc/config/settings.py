from pydantic_settings import BaseSettings, SettingsConfigDict


class ElasticSearchSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="elastic_")

    host: str = "localhost"
    port: int = 9200
    user: str = "elastic"
    password: str = "<your_strong_password>"

    @property
    def http_url(self) -> str:
        return f"http://{self.host}:{self.port}"
