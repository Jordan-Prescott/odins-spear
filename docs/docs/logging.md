# Logging in the Package

## Overview

This package includes built-in logging to provide users with detailed insights into how the package is behaving at runtime. The logging system is **integrated by default**, meaning users do not need to configure anything to start receiving logs. Logs include useful information such as timestamps, log levels, module names, function names, and messages indicating key events.

If a user **does not supply a custom logger**, the package will use a **default logger** that:
- **Logs only ERROR-level messages by default** (to prevent unnecessary noise).
- **Pushes logs to the terminal using a standard handler**.
- **Can be adjusted by setting a lower log level** if the user wants more visibility into package execution.

---

## Default Logging Behavior

### **Log Format**
By default, logs will be output to the terminal in the following format:

```bash
timestamp: 2025-03-11 15:45:30, level: INFO, module: <module>, function: example_function, message: This is an example log.
```

### **Default Log Level**
The package sets the default logging level to **ERROR**, which means only `error` and `critical` messages will be displayed. However, users can adjust this to any level they require to see more detailed logs.

#### Adjusting Logging Level
```python
from odins_spear import API

my_api = API(
    base_url="API URL",
    username="YOUR ODIN USERNAME",
    password="YOUR ODIN PASSWORD"
)

my_api.logger.setLevel("INFO") # set to INFO
my_api.logger.setLevel("WARNING") # set to WARNING
my_api.logger.setLevel("DEBUG") # set to DEBUG
```

#### Logging Levels
| Level     | Description |
|-----------|---------------------------------------------------------------|
| DEBUG     | Provides the most detailed logs, including function calls and internal state changes. |
| INFO      | Shows general package behavior, including successful API calls, connections, etc. |
| WARNING   | Highlights potential issues that do not cause failure. |
| ERROR     | Displays errors that prevent execution of a specific operation. (Default level) |
| CRITICAL  | Reports severe issues that may cause the package to stop functioning. |


