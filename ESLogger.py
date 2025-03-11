import logging
import time
import uuid

from elasticsearch import Elasticsearch


class ESLogger(logging.Logger):
    def __init__(
        self,
        name="OS",
        level=logging.INFO,
        cloud_id=None,
        api_key=None,
        index=str,
        username=str,
    ):
        """
        A custom logger that sends logs directly to Elasticsearch and ensures
        the correct function/module name is captured.
        """
        super().__init__(name, level)

        if not cloud_id or not api_key:
            raise ValueError(
                "cloud_id and api_key are required for Elasticsearch logging."
            )

        self.username = username
        self.uuid = str(uuid.uuid4())
        self.es = Elasticsearch(cloud_id=cloud_id, api_key=api_key)
        self.index = index

        # used to push logs to terminal
        self.console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            "timestamp: %(asctime)s, level: %(levelname)s, module: %(module)s, function: %(funcName)s, message: %(message)s"
        )
        self.console_handler.setFormatter(console_formatter)

    def handle(self, record: logging.LogRecord):
        """
        Custom handling of log records to send them to Elasticsearch while ensuring
        the correct function/module name is captured.
        """
        if not self.isEnabledFor(record.levelno):
            return

        # console
        self.console_handler.handle(record)

        # elastic
        try:
            doc = {
                "@timestamp": time.strftime(
                    "%Y-%m-%dT%H:%M:%S", time.localtime(record.created)
                ),
                "message": record.getMessage(),
                "log": {
                    "level": record.levelname,
                    "logger": record.name,  # Corrected logger name
                    "origin": {
                        "file": {
                            "name": record.pathname,  # Full file path
                            "line": record.lineno,
                        },
                        "function": record.funcName,  # Correct function name
                    },
                    "custom": {"guid": self.uuid},
                    "user": {"name": self.username},
                },
            }
            self.es.index(index=self.index, document=doc)
        except Exception:
            self.handleError(record)

    def _log(
        self,
        level,
        msg,
        args,
        exc_info=None,
        extra=None,
        stack_info=False,
        stacklevel=2,
    ):
        """
        Override `_log` to increase `stacklevel` so that logging captures
        the real caller.
        """
        super()._log(
            level, msg, args, exc_info, extra, stack_info, stacklevel=stacklevel
        )
