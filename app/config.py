from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://postgres:password@db:5432/task_management"
    
    # Redis
    redis_url: str = "redis://localhost:6379"
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE: int

    
    # Application
    debug: bool = True
    log_level: str = "INFO"
    
    # File Upload
    MAX_FILE_SIZE: int
    MAX_FILE_PER_TASK: int
    UPLOAD_DIR: str = "uploads"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
