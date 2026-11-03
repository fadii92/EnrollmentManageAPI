
from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger(__name__)

es = Elasticsearch(
    "http://127.0.0.1:9200",
    request_timeout=10
)


def get_elasticsearch_client():
    return es


def check_elasticsearch_connection():
    try:
        if es.ping():
            logger.info("Connected to Elasticsearch successfully")
            return True

        logger.error("Elasticsearch connection failed")
        return False

    except Exception:
        logger.exception("Elasticsearch connection error")
        return False
