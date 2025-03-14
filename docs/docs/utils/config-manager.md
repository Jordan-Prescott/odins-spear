# ConfigManager Documentation

## Overview

The `ConfigManager` class is designed to load and cache template configurations for popular Broadworks entities. These configuration templates are stored as JSON files in a specified directory. The class enables users to retrieve, view, update, and copy these templates in a flexible and intuitive manner. The primary goal is to provide users with a base configuration that they can modify as needed before using it to make API calls (e.g., to create or update users).

## Available Configurations

The following templates are supported and should be referenced using their corresponding names:

- `auto_attendant`
- `call_center`
- `device`
- `group`
- `hunt_group`
- `service_provider`
- `trunk_group`
- `user`

## Class Methods

### `__init__`
- **Purpose:**  
  Initialises the `ConfigManager` by setting the configuration directory and preloading all JSON configuration files into a cache.
- **Usage:**  
  Instantiate the class to automatically load available configurations.

### `_load_configs`
- **Purpose:**  
  A private method that reads all JSON files from the `config_dir` and caches them.
- **Details:**  
  Iterates over each file in the specified directory and attempts to load JSON data, mapping the filename (without the extension) to its configuration data.

### `reload`
- **Purpose:**  
  Clears the existing cache and reloads all configuration files from disk.
- **Usage:**  
  Use this method if the underlying configuration files have changed and you need to refresh the cache.

### `list_configs`
- **Purpose:**  
  Returns a list of available configuration names.
- **Usage:**  
  Useful for users to quickly see which configuration templates are available for customisation.

### `get_config`
- **Purpose:**  
  Retrieves the full configuration for a given config type.
- **Arguments:**  
  - `config_name` (str): The name of the configuration to fetch.
- **Returns:**  
  The configuration as a dictionary.
- **Exceptions:**  
  Raises a `KeyError` if the requested config is not among the supported templates.

### `get_value`
- **Purpose:**  
  Retrieves a nested value from a configuration using dot notation.
- **Arguments:**  
  - `config_name` (str): The configuration from which to retrieve the value.
  - `key_path` (str): A dot notation string indicating the path to the desired value (e.g., `"serviceProviderId.name"`).
- **Returns:**  
  The value found at the specified key path.
- **Exceptions:**  
  Raises a `KeyError` if either the configuration or the specified key path is not found.

### `copy_config`
- **Purpose:**  
  Returns a complete deep copy of a specified configuration. This ensures that modifications to the returned copy do not affect the original cached configuration.
- **Arguments:**  
  - `config_name` (str): The configuration to be copied.
- **Returns:**  
  A deep copy of the configuration as a dictionary.
- **Exceptions:**  
  Raises a `KeyError` if the configuration name is not found.

### `view_config`
- **Purpose:**  
  Prints the configuration in a human-friendly format using Python's `pprint` module.
- **Arguments:**  
  - `config_name` (str): The name of the configuration to be printed.
- **Returns:**  
  A formatted printout of the configuration.
- **Exceptions:**  
  Raises a `KeyError` if the configuration name is not valid.

## Example Usage

```python
from odins_spear.utils.config_manager import ConfigManager

# Instantiate the ConfigManager
cm = ConfigManager()

# List available configurations
print("Available Configs:", cm.list_configs())

# Retrieve a full configuration (e.g., 'user')
user_config = cm.get_config('user')

# Make a complete copy so modifications won't affect the original cached config
user_config_copy = cm.copy_config('user')

# Update specific values in the copy
user_config_copy['serviceInstanceProfile']['name'] = 'John Doe'
user_config_copy['serviceInstanceProfile']['language'] = 'English'

# Optionally, view the configuration in a formatted way
cm.view_config('user')

# Use the updated config in an API call - Below is an exmaple without com
api.users.post_user(
    service_provider="test_sp",
    group_id="test_gp",
    user_id="userId@example.com",
    first_name="John",
    last_name="Doe",
    extension="1234",
    web_auth_password="lalksnd223a",
    payload=user_config_copy
)
```
