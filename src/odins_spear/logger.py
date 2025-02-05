import logging
from typing import Optional, Union


class Logger:
    __instance = None

    @staticmethod
    def get_instance(
        user: Optional[str] = None, custom_logger: Optional[logging.Logger] = None
    ) -> Union[logging.Logger, "Logger"]:
        """Get a logger instance - either a custom logger or the singleton Logger instance.

        Args:
            user (str): Username used when creating API object
            custom_logger (Optional[logging.Logger]): Custom logger instance

        Returns
            Union[logging.Logger, Logger]: Either the custom logger or singleton Logger instance
        """
        if custom_logger:
            if Logger.validate_logger(custom_logger):
                custom_logger._user = user
                return custom_logger
            else:
                raise ValueError(
                    "Custom logger must implement info, debug, warning, and error methods"
                )

        if Logger.__instance is None:
            Logger(user)
        return Logger.__instance

    def __init__(self, user: str) -> None:
        """Logger class logs API calls made using Odin's Spear.
        Details logged are: Date/Time, Name (Odin's Spear), User, response code, endpoint.

        NOTE: This object is a singleton and can't be instantiated more than once.

        Args:
            user (str): Username used when creating API object.
        """
        if Logger.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")

        self._user = user
        self._logger_obj = logging.getLogger("OS")
        self._logger_obj.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(user)s - %(endpoint)s - %(http_method)s"
        )
        handler.setFormatter(formatter)
        self._logger_obj.addHandler(handler)

        Logger.__instance = self

    def info(self, msg, **kwargs):
        self._logger_obj.info(msg, extra={"user": self._user, **kwargs})

    def debug(self, msg, *args, **kwargs):
        self._logger_obj.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger_obj.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger_obj.error(msg, *args, **kwargs)

    @staticmethod
    def validate_logger(logger: logging.Logger) -> bool:
        """Validates that a logger has the required attributes and methods.

        Args:
            logger (logging.Logger): Logger object to validate

        Returns:
            bool: True if logger meets requirements, False otherwise
        """
        required_methods = ["info", "debug", "warning", "error"]
        return all(hasattr(logger, method) for method in required_methods)
