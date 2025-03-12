import requests
import json

from ratelimit import limits, sleep_and_retry

from .exceptions import OSApiResponseError
from .utils.formatters import sanitise_data


class Requester:
    __instance = None  # Class variable to hold the singleton instance

    @staticmethod
    def get_instance(base_url=None, rate_limit=None, logger=None):
        if Requester.__instance is None:
            Requester(base_url, rate_limit, logger)
        return Requester.__instance

    def __init__(self, base_url, rate_limit, logger):
        """
        Initialize the Requester with default values.

        NOTE: This object is a singleton and can't be instantiated more than once.
        """
        if Requester.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.base_url = base_url
            self.rate_limit = rate_limit
            self.headers = {
                "Authorization": "",
                "Content-Type": "application/json",
            }
            self.logger = logger

            self.logger.info(
                f"Requester initialized with base_url: {self.base_url}, rate_limit: {self.rate_limit}"
            )

            Requester.__instance = self

    def get(self, endpoint, data=None, params=None):
        return self._request(requests.get, endpoint, data, params)

    def post(self, endpoint, data=None):
        return self._request(requests.post, endpoint, data)

    def put(self, endpoint, data=None):
        return self._request(requests.put, endpoint, data)

    def delete(self, endpoint, data=None, params=None):
        return self._request(requests.delete, endpoint, data, params)

    def _request(self, method, endpoint, data=None, params=None):
        """Handles an API request with or without rate limiting."""

        self.logger.info(
            f"Initiating API request, method: {method.__name__.upper()}, endpoint: {endpoint}"
        )

        if self.rate_limit:
            return self._rate_limited_request(method, endpoint, data, params)

        # Logging request details
        request_payload = json.dumps(data) if data is not None else None
        self.logger.debug(
            f"Sending request, method: {method.__name__.upper()},"
            f"endpoint: {self.base_url + endpoint}, params: {params}, data: {sanitise_data(data) if data else 'None'}"
        )

        response = method(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=request_payload,
            params=params or {},
        )

        return self._handle_response(response, method.__name__, endpoint)

    @sleep_and_retry
    @limits(calls=5, period=1)
    def _rate_limited_request(self, method, endpoint, data=None, params=None):
        """Handles an API request with rate limiting."""

        self.logger.warning(
            f"Rate limit active. Request may be delayed, method: {method.__name__.upper()}, endpoint: {endpoint}"
        )

        request_payload = json.dumps(data) if data is not None else None
        self.logger.debug(
            f"Sending rate-limited request, method: {method.__name__.upper()},"
            f"endpoint: {self.base_url + endpoint}, params: {params}, data: {sanitise_data(data) if data else 'None'}"
        )

        response = method(
            url=self.base_url + endpoint,
            headers=self.headers,
            data=request_payload,
            params=params or {},
        )

        return self._handle_response(response, method.__name__, endpoint)

    def _handle_response(self, response, method_name, endpoint):
        """Handles response logging and error handling."""

        # Log response status
        if response.status_code >= 200 and response.status_code < 300:
            self.logger.info(
                f"API Call Success, method: {method_name.upper()}, endpoint: {endpoint}, status_code: {response.status_code}"
            )
            self.logger.debug(f"response_data: {sanitise_data(response.json())}")

            return response.json()

        # Log API errors
        else:
            self.logger.error(
                f"API Error, method: {method_name.upper()}, endpoint: {endpoint}, status_code: {response.status_code}, response_text: {response.text}"
            )
            raise OSApiResponseError(response)
