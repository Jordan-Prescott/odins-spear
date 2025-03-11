import logging
from typing import Optional

from .requester import Requester
from .exceptions import (
    OSApiAuthenticationFail,
    OSSessionRefreshFail,
    OSFailedToLocateSession,
)

from .endpoints import *  # noqa: F403

import requests


class API:
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        rate_limit: bool = True,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """ Connection to Odin API, all interactions with the api are here.

        Args:
            base_url (str): Base url of your odin instance api.
            username (str): Username used when logging into odin account.
            password (str): Password used when logging into odin account stored as virtual environment.
            rate_limit (bool): Enables (True) or Disables (False) rate limiting to 5 calls per second. Defaults to True.
            logger (logger, optional): Pass in external logger, if not default logger will be assigned. 
            
        Vars: 
            authorised (bool): Boolean value to indicate if api is authorised.\
            token (str): Token string returned from odin api.
        """

        self.base_url = base_url
        self.username = username
        self._password = password
        self.rate_limit = rate_limit

        self.authorised = False
        self.token = ""

        self.logger = logger if logger else self._setup_logger()
        self.logger.info(
            f"API initialised, user: {self.username}, base_url: {self.base_url}, rate_limit: {self.rate_limit}"
        )

        self._requester = Requester.get_instance(
            self.base_url, self.rate_limit, self.logger
        )

        # # endpoints
        self.administrators = Administrators(logger=self.logger)
        self.alternate_numbers = AlternateNumbers(logger=self.logger)
        self.authentication = Authentication(logger=self.logger)
        self.auto_attendants = AutoAttendants(logger=self.logger)
        self.call_centers = CallCenters(logger=self.logger)
        self.call_forwarding_always = CallForwardingAlways(logger=self.logger)
        self.call_forwarding_busy = CallForwardingBusy(logger=self.logger)
        self.call_forwarding_no_answer = CallForwardingNoAnswer(logger=self.logger)
        self.call_forwarding_not_reachable = CallForwardingNotReachable(
            logger=self.logger
        )
        self.call_forwarding_selective = CallForwardingSelective(logger=self.logger)
        self.call_pickup = CallPickup(logger=self.logger)
        self.call_processing_policies = CallProcessingPolicies(logger=self.logger)
        self.call_records = CallRecords(logger=self.logger)
        self.devices = Devices(logger=self.logger)
        self.dns = DNs(logger=self.logger)
        self.groups = Groups(logger=self.logger)
        self.emergency_zones = EmergencyZones(logger=self.logger)
        self.do_not_disturb = DoNotDisturb(logger=self.logger)
        self.hunt_groups = HuntGroups(logger=self.logger)
        self.service_providers = ServiceProviders(logger=self.logger)
        self.services = Services(logger=self.logger)
        self.shared_call_appearance = SharedCallAppearance(logger=self.logger)
        self.schedules = Schedules(logger=self.logger)
        self.reports = Reports(logger=self.logger)
        self.regsitration = Registration(logger=self.logger)
        self.password_generate = PasswordGenerate(logger=self.logger)
        self.trunk_groups = TrunkGroups(logger=self.logger)
        self.users = Users(logger=self.logger)

    def authenticate(self) -> bool:
        """Authenticates session with username and password supplied by user.

        Raises:
            OSApiAuthenticationFail: Raised if authenticaion fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        endpoint = "/auth/token"

        payload = {"username": self.username, "password": self._password}

        try:
            response = self._requester.post(endpoint, data=payload)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSApiAuthenticationFail()

    def refresh_authorisation(self) -> bool:
        """Re-authenticates the session with the API. Used if API key is to expire.

        Raises:
            OSSessionRefreshFail: Raised if authentication fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        endpoint = "/auth/session"

        try:
            response = self._requester.put(endpoint)
            self._update_requester(response)
            return True
        except requests.exceptions.HTTPError:
            raise OSSessionRefreshFail()

    def get_auth_details(self):
        """Gets current session details.

        Raises:
            OSFailedToLocateSession: Raised when session details can't be found.
                Most likely because session has expired.

        Returns:
            Dict: Current session details.
        """

        endpoint = "/auth/session"

        try:
            return self._requester.get(endpoint)
        except requests.exceptions.HTTPError:
            raise OSFailedToLocateSession()

    def update_api(
        self,
        base_url: str = None,
        username: str = None,
        password: str = None,
        rate_limit: bool = None,
    ):
        """Updates the API with new details.

        Args:
            base_url (str, optional): Base url of your odin instance api. Defaults to None.
            username (str, optional): Username used when logging into odin account. Defaults to None.
            password (str, optional): Password used when logging into odin account stored as virtual environment. Defaults to None.
            rate_limit (bool, optional): Enables (True) or Disables (False) rate limiting to 5 calls per second. Defaults to None.
        """

        if base_url:
            self.logger.info(
                f"API base_url updated, old: {self.base_url}, new: {base_url}"
            )
            self.base_url = base_url
            self._requester.base_url = base_url
        if username:
            self.logger.info(
                f"API username updated, old: {self.username}, new: {username}"
            )
            self.username = username
            self._requester.logger = self.logger
        if password:
            self.logger.info("API password updated")
            self._password = password
        if rate_limit:
            self.logger.info(
                f"API rate_limit updated, old: {self.rate_limit}, new: {rate_limit}"
            )
            self.rate_limit = rate_limit
            self._requester.rate_limit = rate_limit

    def _update_requester(self, session_response: requests.models.Response):
        """When authenticating or re-auth update requester with token so it can make
        api calls

        Args:
            session_response (request): Requests mod response.
        """

        self.token = session_response["token"]
        self._requester.headers["Authorization"] = f"Bearer {self.token}"
        self.authorised = True
        self.logger.info("API session updated with new token")

    def _setup_logger(self):
        logger = logging.getLogger("OS")
        logger.setLevel(logging.ERROR)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "timestamp: %(asctime)s, level: %(levelname)s, module: %(module)s, function: %(funcName)s,  message: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def __str__(self) -> str:
        return (
            f"API - url: {self.base_url}, username: {self.username} "
            f"Authenticated: {self.authorised}"
        )
