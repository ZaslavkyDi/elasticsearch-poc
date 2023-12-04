from pydantic_settings import BaseSettings, SettingsConfigDict


class ElasticSearchSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="elastic_")

    host: str = "localhost"
    port: int = 9200
    user: str = "elastic"
    password: str = "<your_strong_password>"

    @property
    def https_url(self) -> str:
        return f"https://{self.host}:{self.port}"

    @property
    def dev_http_ca_crt_path(self) -> str:
        return "../dev_http_ca.crt"
