from .base_endpoint import BaseEndpoint


class Session(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET

    def get_session(self):
        """Fetches session information for currently logged in user"""

        endpoint = "/auth/session"

        return self._requester.get(endpoint)

    # POST

    def post_session(self, username: str, password: str):
        """Requests access token.

        Args:
            username (str): Odin instance username
            password (str): Odin instance password
        """

        endpoint = "/auth/token"

        payload = {"username": username, "password": password}

        return self._requester.post(endpoint, data=payload)

    def post_session_switch(self, username: str):
        """Switch users

        Args:
            username (str): User you would like to switch to
        """

        endpoint = "/auth/switch-user"

        payload = {"username": username}

        return self._requester.post(endpoint, data=payload)

    def post_session_logout(self):
        """Logs out of session"""

        endpoint = "/auth/token/logout"

        payload = {"token": self._requester.token}

        return self._requester(endpoint, data=payload)

    # PUT

    def put_session(self):
        """Refreshes access token fetching a new one which will expire in 24hr"""

        endpoint = "/auth/token"

        return self._requester.put(endpoint)

    def put_change_password(self, user_id: str, new_password: str):
        """Change the password of a user

        Args:
            user_id (str): Tagrte user id of user to reset password
            new_password (str): New password
        """

        endpoint = "/users/passwords"

        updates = {"userId": user_id, "password": new_password}

        return self._requester.put(endpoint, data=updates)

    def put_password(self, user_id: str, old_password: str, new_password: str):
        """Change password of a specific user.

        Args:
            user_id (str): Target user to change password
            old_password (str): Current password user logs in with
            new_password (str): Password to change to
        """

        endpoint = "/auth/passwords"

        updates = {
            "userId": user_id,
            "oldPassword": old_password,
            "newPassword": new_password,
        }

        return self._requester.put(endpoint, data=updates)

    def put_my_password(self, old_password: str, new_password: str):
        """Change the password of the current user

        Args:
            old_password (str): Current password user logs in with
            new_password (str): Password to change to
        """

        endpoint = "/auth/password"

        updates = {"oldPassword": old_password, "newPassword": new_password}

        self._requester.put(endpoint, data=updates)

    # DELETE
