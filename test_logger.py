from logger_service import logger

logger.info("Testing Elasticsearch logging")
logger.warning("This is a test warning")
logger.error("This is a test error")

print("Test logs sent to Elasticsearch!")