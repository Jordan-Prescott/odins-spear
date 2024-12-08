import json
import os
from copy import deepcopy


class ConfigManager:
    def __init__(self, config_path="configs"):
        self.config_path = config_path
        self._default_configs = {}
        self._configs = {}

        self._load_configs()

    def _load_configs(self):
        for file_name in os.listdir(self.config_path):
            if file_name.endswith(".json"):
                entity_name = os.path.splitext(file_name)[0]
                with open(os.path.join(self.config_path, file_name), "r") as file:
                    self._default_configs[entity_name] = json.load(file)
                    self._configs[entity_name] = []

    def create_config(self, entity: str, config_name: str, custom_config: dict = None):
        if entity not in self._default_configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        config = deepcopy(custom_config or self._default_configs[entity])
        self._configs[entity].append({"name": config_name, "config": config})

    def get_config(self, entity: str, config_name: str):
        if entity not in self._configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        for instance in self._configs[entity]:
            if instance["name"] == config_name:
                return deepcopy(instance["config"])

        raise KeyError(
            f"Configuration instance '{config_name}' for entity '{entity}' does not exist."
        )

    def get_config_section(self, entity: str, config_name: str, section: str = None):
        if entity not in self._configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        for instance in self._configs[entity]:
            if instance["name"] == config_name:
                config = deepcopy(instance["config"])
                if section:
                    if section not in config:
                        raise KeyError(
                            f"Section '{section}' does not exist in configuration '{config_name}'."
                        )
                    return config[section]
                return config

        raise KeyError(
            f"Configuration instance '{config_name}' for entity '{entity}' does not exist."
        )

    def update_config(self, entity: str, config_name: str, updated_config: dict):
        if entity not in self._configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        for instance in self._configs[entity]:
            if instance["name"] == config_name:
                instance["config"] = deepcopy(updated_config)
                return

        raise KeyError(
            f"Configuration instance '{config_name}' for entity '{entity}' does not exist."
        )

    def delete_config(self, entity: str, config_name: str):
        if entity not in self._configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        self._configs[entity] = [
            instance
            for instance in self._configs[entity]
            if instance["name"] != config_name
        ]

    def list_configs(self, entity: str):
        if entity not in self._configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        return [instance["name"] for instance in self._configs[entity]]

    def reset_config(self, entity: str, config_name: str):
        if entity not in self._default_configs:
            raise KeyError(f"Entity '{entity}' does not exist.")

        for instance in self._configs[entity]:
            if instance["name"] == config_name:
                instance["config"] = deepcopy(self._default_configs[entity])
                return

        raise KeyError(
            f"Configuration instance '{config_name}' for entity '{entity}' does not exist."
        )

    def reset_all(self):
        for entity, instances in self._configs.items():
            for instance in instances:
                instance["config"] = deepcopy(self._default_configs[entity])
