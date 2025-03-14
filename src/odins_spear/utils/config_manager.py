import os
import json
import copy

from pprint import pprint as pp


class ConfigManager:
    config_dir = "odins_spear/utils/configs/"
    available_configs = [
        "auto_attendant",
        "call_center",
        "device",
        "group",
        "hunt_group",
        "service_provider",
        "trunk_group",
        "user",
    ]

    def __init__(self):
        """
        ConfigManager loads and caches template configs for popular Broadworks entities.

        This class gives the end user access to these templates so they have utilise them
        when making api call.

        Complete list of template configs (name formatted how user needs to reference):
        - auto_attendant
        - call_center
        - device
        - group
        - hunt_group
        - service_provider
        - trunk_group
        - user
        """
        self._configs = {}
        self._load_configs()

    def _load_configs(self):
        """Load all JSON configuration files from the given directory."""
        for filename in os.listdir(self.config_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(self.config_dir, filename)
                try:
                    with open(filepath, "r") as f:
                        config_data = json.load(f)
                    config_key = os.path.splitext(filename)[0]
                    self._configs[config_key] = config_data
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

    def reload(self):
        """Clear the cache and reload all configuration files from disk."""
        self._configs = {}
        self._load_configs()

    def list_configs(self):
        """Return a list of available configuration names."""
        return self.available_configs

    def get_config(self, config_name: str):
        """Returns the full configuration of specified config type.

        Args:
            config_name (str, optional): Name of config to fetch.

        Raises:
            KeyError: Raised is config name is not found in supported configs.

        Returns:
            dict: Configuration specified.

        """

        if config_name not in self.available_configs:
            raise KeyError(f"Config '{config_name}' not found.")

        return self._configs[config_name]

    def get_value(self, config_name: str, key_path: str):
        """Gets specifec value from configuration. Dot notion is used to target
        the value needed.

        Args:
            config_name (str): Configuration with needed value.
            key_path (str): Dot notation path to value for example 'serviceProviderId.name'

        Raises:
            KeyError: Raised if config_name is not in supported configurations.
            KeyError: Raised if target value is not found in configuration.

        Returns:
            object: Value from configuarion.
        """

        if config_name not in self.available_configs:
            raise KeyError(f"Config '{config_name}' not found.")

        config = self.get_config(config_name)
        keys = key_path.split(".")
        value = config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                raise KeyError(
                    f"Key path '{key_path}' not found in config '{config_name}'."
                )
        return value

    def copy_config(self, config_name):
        """Creates a complete copy of configuration.

        Args:
            config_name (str, optional): Name of config to copy.

        Raises:
            KeyError: Config name not found.

        Returns:
            dict: Configuration of specified config requested.

        """
        if config_name not in self.available_configs:
            KeyError(f"Config '{config_name}' not found.")

        if config_name in self._configs:
            return copy.deepcopy(self._configs[config_name])

    def view_config(self, config_name: str):
        """Prints template configuration in a human friendly way to digest it.

        Args:
            config_name (str): Name of supported configuration to view.

        Raises:
            KeyError: Raised of config_name is not found in supported configurations.

        Returns:
            str: Formatted configuration.
        """

        if config_name not in self.available_configs:
            KeyError(f"Config '{config_name}' not found.")

        return pp(self._configs[config_name])
