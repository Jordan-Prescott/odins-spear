import logging
import re


class SensitiveDataFilter(logging.Filter):
    """Filter to mask sensitive data in logs."""

    SENSITIVE_FIELDS = {"password", "token", "api_key", "secret"}  # Add more if needed

    def filter(self, record):
        """Replaces sensitive fields in log messages with '*****'."""
        if isinstance(record.msg, dict):
            # If message is a dictionary (structured logging)
            for field in self.SENSITIVE_FIELDS:
                if field in record.msg:
                    record.msg[field] = "*****"

        elif isinstance(record.msg, str):
            # If message is a string, use regex to mask sensitive values
            for field in self.SENSITIVE_FIELDS:
                record.msg = re.sub(
                    rf'("{field}":\s*")([^"]+)', r"\1*****", record.msg
                )  # JSON-like
                record.msg = re.sub(
                    rf"({field}=\S+)", rf"{field}=*****", record.msg
                )  # Key-value format

        return True  # Allow log to proceed
