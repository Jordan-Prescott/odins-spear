from .base_endpoint import BaseEndpoint


class Authentication(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_authentication_service(self, user_id: str):
        """Returns authentication details of authorised users.

        Args:
            user_id (str): Target user ID.

        Returns:
            Dict: Autnentication details of target user
        """

        endpoint = "/users/authentication"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    def put_user_authentication_service(self, user_id: str, new_password: str):
        """Set new SIP Authentication password for a single user.

        Args:
            user_id (str): Target user ID to reset the SIP authentication password.
            new_password (str): New SIP authentication password to apply to new user.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/users/authentication"

        data = {"userId": user_id, "newPassword": new_password}

        return self._requester.put(endpoint, data=data)

    def put_user_authentication_user(
        self, username: str, user_id: str, old_password: str, new_password: str
    ):
        """Changes the authentication password of a single user

        Args:
            username (str): Username of target user
            user_id (str): User ID of target user
            old_password (str): Old password (current)
            new_password (str): Password to change to

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/users/authentication"

        params = {
            "userName": username,
            "userId": user_id,
            "password": {"old": old_password, "new": new_password},
        }

        return self._requester.put(endpoint, params=params)

    # DELETE
