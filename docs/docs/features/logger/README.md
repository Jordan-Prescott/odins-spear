# Logger

The `Logger` object provides detailed logging for all API calls made using Odin's Spear.

### Default Behavior
- If no logger is passed during the `API` initialization, a default `Logger` object is created.
- Details logged include:
  - **Date/Time**: The timestamp of the API call.
  - **Name**: "Odin's Spear" as the application name.
  - **User**: The username of the developer.
  - **Response Code**: The HTTP response status code.
  - **Endpoint**: The API endpoint accessed.

### External Logger Integration
Users can pass their own logger when initializing the `API`. This allows integration with custom logging systems like `loguru`, `logging`, or `Sentry`.

### File and Syslog Handlers
By default, logs are sent to `os.log`, but this can be customized using the following methods:
- `set_up_file_handler()`: Configure logging to a file.
- `set_up_syslog_handler()`: Configure logging to an external syslog server.

---

## Usage

### Default Logger
If you do not pass a logger:
```python
from odins_spear import API

# Initialize API with default logger
my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# Use default logger handlers
my_api.logger.set_up_file_handler()
my_api.logger.set_up_syslog_handler()
```

---

### Custom Logger
To use your own logger:
```python
import logging
from odins_spear import API

# Create a custom logger
custom_logger = logging.getLogger("custom_logger")
custom_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
custom_logger.addHandler(handler)

# Initialize API with custom logger
my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1", logger=custom_logger)
my_api.authenticate()
```

---

### Notes
- Integrating a custom logger ensures compatibility with your application's logging setup.
- Using the default logger provides a quick, pre-configured solution for capturing API call details.
