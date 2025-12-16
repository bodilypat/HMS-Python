#app/core/config.py

class settings:
    PROJECT_NAME: str = "My FastAPI Application"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str ="sunshine_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    