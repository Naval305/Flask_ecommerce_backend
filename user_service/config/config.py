import os

from dotenv import load_dotenv


load_dotenv()

#rabbitmq
rabbitmq_host = os.getenv("RABBITMQ_HOST")
rabbitmq_port = os.getenv("RABBITMQ_PORT")
rabbitmq_user = os.getenv("RABBITMQ_USER")
rabbitmq_password = os.getenv("RABBITMQ_PASSWORD")

rabbitmq_token_exchange = os.getenv("RABBITMQ_TOKEN_EXCHANGE")
rabbitmq_token_queue = os.getenv("RABBITMQ_TOKEN_QUEUE")
rabbitmq_token_routing_key = os.getenv("RABBITMQ_TOKEN_ROUTING_KEY")

rabbitmq_feedback_exchange = os.getenv("RABBITMQ_FEEDBACK_EXCHANGE")
rabbitmq_feedback_queue = os.getenv("RABBITMQ_FEEDBACK_QUEUE")
rabbitmq_feedback_routing_key = os.getenv("RABBITMQ_FEEDBACK_ROUTING_KEY")

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_TITLE = "Flask API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_RAPIDOC_PATH = "/rapidoc"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('PROD_DB_USER')}:{os.getenv('PROD_DB_PASSWORD')}@{os.getenv('PROD_DB_HOST')}/{os.getenv('PROD_DB_NAME')}"


if os.getenv("FLASK_ENV") == "development":
    app_config = DevelopmentConfig
else:
    app_config = ProductionConfig
