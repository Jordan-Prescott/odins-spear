# Custom Logger

The **ESLogger** is a custom Python logger designed to simultaneously send log records to Elasticsearch for FourteenIP's needs as well as print them to the terminal for the end user. 

It extends Python’s built-in `logging.Logger` to capture accurate caller information (file, function, and line number) and to support flexible logging output.

---

## Overview

The **ESLogger** is built to:
- **Send logs to Elasticsearch:** Every log message is indexed in Elasticsearch using the provided cloud credentials.
- **Print logs to the terminal:** A built-in console handler outputs logs in a human-friendly format.
- **Capture correct caller information:** Overrides the default logging behavior so that the file, function, and line number reported are from the actual logging call site.

---

## Features

- **Dual Logging Output:**  
  - **Elasticsearch:** Logs are structured and sent to a specified Elasticsearch index.
  - **Terminal:** Logs are output to the terminal with a configurable format.
- **Caller Context Accuracy:**  
  The logger overrides the internal `_log()` method with an increased `stacklevel` to ensure that the origin (file, function, and line) of the log is captured correctly.
- **Custom Fields:**  
  The log document sent to Elasticsearch includes a unique GUID (generated on instantiation) and user information.

---

## Configuration Options

When instantiating an **ESLogger**, the following parameters must be provided:

- **name** (`str`):  
  - *Description:* The name of the logger.  
  - *Default:* `"OS"`

- **level** (`int`):  
  - *Description:* The base logging level for the logger (as defined in Python’s `logging` module).  
  - *Default:* `logging.INFO`

- **cloud_id** (`str`):  
  - *Description:* The Elasticsearch Cloud ID required to connect to your Elasticsearch deployment.  
  - *Required:* Yes

- **api_key** (`tuple`):  
  - *Description:* A tuple containing the API key and API key ID for Elasticsearch authentication.  
  - *Required:* Yes

- **index** (`str`):  
  - *Description:* The Elasticsearch index to which log documents will be sent.
  
- **username** (`str`):  
  - *Description:* The username to be included in the log document under the `user` field.

*Note:* If `cloud_id` or `api_key` are not provided, the logger will raise a `ValueError`.

---

## How It Works

1. **Initialization:**  
   The logger is initialized with the provided Elasticsearch connection parameters and creates:
   - An Elasticsearch client using `cloud_id` and `api_key`.
   - A unique GUID (`uuid`) to be included with every log.
   - A console (terminal) handler with a specified formatter.

2. **Handling Log Records:**  
   The overridden `handle()` method processes each log record in two steps:
   - **Console Output:** The record is forwarded to the `StreamHandler` to print the log to the terminal.
   - **Elasticsearch Output:** A structured document is built using fields such as:
     - `@timestamp`: The log timestamp.
     - `message`: The log message.
     - `log`: A nested object containing log level, logger name, and origin (file name, line number, and function name).
     - `custom`: Contains the unique GUID.
     - `user`: Contains the username.
     
     This document is then indexed in Elasticsearch.
     
3. **Caller Context:**  
   The `_log()` method is overridden with an increased `stacklevel` (set to 2) so that the logging framework correctly identifies the real calling context rather than the logger’s internal methods.

---

## How to Use

### ESLogger Class

```python
# filename es_logger.py

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
```

### Use ESLogger with Odin's Spear

```python
from odins_spear import API
from es_logger import ESLogger  # Adjust the import path as needed

# Instantiate the custom logger with your Elasticsearch credentials
my_logger = ESLogger(
    cloud_id="YOUR_CLOUD_ID",
    api_key=("YOUR_API_KEY", "YOUR_API_KEY_ID"),
    index="odins_spear",
    username="test.user"
)

my_api = API(
    base_url="API URL",
    username="YOUR ODIN USERNAME",
    password="YOUR ODIN PASSWORD",
    logger=my_logger
)

```

## Terminal Output
```bash
timestamp: 2025-03-11 15:45:30, level: INFO, module: <module>, function: example_function, message: This is an example log.
```