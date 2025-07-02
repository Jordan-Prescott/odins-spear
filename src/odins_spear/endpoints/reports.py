from .base_endpoint import BaseEndpoint


class Reports(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_user_report(self, user_id: str):
        """Detailed report of user including services and service packs assigned.

        Args:
            user_id (str): Target user id of user.

        Returns:
            dict: Detailed report of user including services and service packs.
        """

        endpoint = "/users/reports/users"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_report(self, service_provider_id: str, group_id: str):
        """Detailed report of users within a group including services and service packs assigned.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is hosted.
            group_id (str): Target Group ID

        Returns:
            dict: Detailed report of users within a group including services and service packs.
        """

        endpoint = "/groups/reports/users"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)


# POST

# PUT

# DELETE
