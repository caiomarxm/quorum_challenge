from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.development", extra="ignore")

    BILLS_CSV_FILE_PATH: str
    LEGISLATORS_CSV_FILE_PATH: str
    VOTES_FILE_PATH: str
    VOTE_RESULTS_CSV_FILE_PATH: str


settings = Settings()
