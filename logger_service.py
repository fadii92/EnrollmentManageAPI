
import logging
from datetime import datetime, timezone
from elasticsearch_config import es


class ElasticsearchHandler(logging.Handler):

    def emit(self, record):
        try:
            log_data = {
                "@timestamp": datetime.now(timezone.utc).isoformat(),
                "level": record.levelname,
                "service": "demo-dao",
                "module": record.module,
                "operation": record.funcName,
                "message": self.format(record),
            }

            es.index(
                index="demo-dao-logs",
                document=log_data
            )

        except Exception:
            self.handleError(record)


logger = logging.getLogger("demo-dao")
logger.setLevel(logging.INFO)

if not any(
    isinstance(handler, ElasticsearchHandler)
    for handler in logger.handlers
):
    handler = ElasticsearchHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
