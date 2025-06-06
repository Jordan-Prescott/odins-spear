import logging
from typing import Optional

from .requester import Requester
from .endpoints import *  # noqa: F403

from .exceptions import (
    OSApiAuthenticationFail,
    OSSessionRefreshFail,
    OSFailedToLocateSession,
)


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

        self.logger = logger if logger else self._setup_logger()
        self.logger.info(
            f"API initialised, user: {self.username}, base_url: {self.base_url}, rate_limit: {self.rate_limit}"
        )

        self._requester = Requester.get_instance(
            self.base_url, self.rate_limit, self.logger
        )

        # endpoints
        self.administrators = Administrators()  # noqa: F405
        self.alternate_numbers = AlternateNumbers()  # noqa: F405
        self.announcements = Announcements()  # noqa: F405
        self.authentication = Authentication()  # noqa: F405
        self.auto_attendants = AutoAttendants()  # noqa: F405
        self.call_centers = CallCenters()  # noqa: F405
        self.call_forwarding_always = CallForwardingAlways()  # noqa: F405
        self.call_forwarding_busy = CallForwardingBusy()  # noqa: F405
        self.call_forwarding_no_answer = CallForwardingNoAnswer()  # noqa: F405
        self.call_forwarding_not_reachable = CallForwardingNotReachable()  # noqa: F405
        self.call_forwarding_selective = CallForwardingSelective()  # noqa: F405
        self.call_pickup = CallPickup()  # noqa: F405
        self.call_processing_policies = CallProcessingPolicies()  # noqa: F405
        self.call_records = CallRecords()  # noqa: F405
        self.devices = Devices()  # noqa: F405
        self.dns = DNs()  # noqa: F405
        self.groups = Groups()  # noqa: F405
        self.emergency_zones = EmergencyZones()  # noqa: F405
        self.extensions = Extensions()  # noqa: F405
        self.do_not_disturb = DoNotDisturb()  # noqa: F405
        self.hunt_groups = HuntGroups()  # noqa: F405
        self.service_providers = ServiceProviders()  # noqa: F405
        self.services = Services()  # noqa: F405
        self.session = Session()  # noqa: F405
        self.shared_call_appearance = SharedCallAppearance()  # noqa: F405
        self.schedules = Schedules()  # noqa: F405
        self.reports = Reports()  # noqa: F405
        self.regsitration = Registration()  # noqa: F405
        self.password_generate = PasswordGenerate()  # noqa: F405
        self.trunk_groups = TrunkGroups()  # noqa: F405
        self.users = Users()  # noqa: F405

        # authenticate newly instantiated object
        self._authenticate()

    def refresh_authorisation(self) -> bool:
        """Re-authenticates the session with the API. Can used if API key is due to expire.

        Raises:
            OSSessionRefreshFail: Raised if authentication fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        try:
            response = self.session.put_session()
            self._update_requester(response)
            return True
        except Exception:
            raise OSSessionRefreshFail()

    def get_auth_details(self):
        """Gets current session details.

        Raises:
            OSFailedToLocateSession: Raised when session details can't be found.
                Most likely because session has expired.

        Returns:
            Dict: Current session details.
        """

        try:
            return self.session.get_session()
        except Exception:
            raise OSFailedToLocateSession()

    def update_api(
        self,
        base_url: str = None,
        username: str = None,
        password: str = None,
        rate_limit: bool = None,
        logger: object = None,
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
        if password:
            self.logger.info("API password updated")
            self._password = password
        if rate_limit:
            self.logger.info(
                f"API rate_limit updated, old: {self.rate_limit}, new: {rate_limit}"
            )
            self.rate_limit = rate_limit
            self._requester.rate_limit = rate_limit
        if logger:
            self.logger = logger
            self._requester.logger = logger
            self.logger.info("Logger updated")

    def _authenticate(self) -> bool:
        """Authenticates session with username and password supplied by user.

        Raises:
            OSApiAuthenticationFail: Raised if authenticaion fails.

        Returns:
            Bool: Returns True to indicate authentication was successful.
        """

        try:
            response = self.session.post_session(self.username, self._password)
            self._update_requester(response)
            return True
        except Exception:
            raise OSApiAuthenticationFail

    def _update_requester(self, session_response: dict):
        """When authenticating or re-auth update requester with token so it can make
        api calls

        Args:
            session_response (dict): Resposne from call.
        """

        self._requester.headers["Authorization"] = f"Bearer {session_response['token']}"
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
