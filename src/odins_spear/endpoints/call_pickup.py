from .base_endpoint import BaseEndpoint


class CallPickup(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_call_pickup_groups(self, service_provider_id: str, group_id: str):
        """Retrieves Pickup Group information for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.

        Returns:
            Dict: Specified users pickup group, and the users within that group.
        """

        endpoint = "/groups/call-pickup/groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_call_pickup_group(
        self, service_provider_id: str, group_id: str, pickup_group_name: str
    ):
        """Retrieves Pickup Group information for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            pickup_group_name (str): The Target Pickup Group Name

        Returns:
            Dict: Specified users pickup group, and the users within that group.
        """

        endpoint = "/groups/call-pickup/groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": pickup_group_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_call_pickup_group_user(
        self, service_provider_id: str, group_id: str, user_id: str
    ):
        """Retrieves Pickup Group information for the specified user.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            user_id (str): Target User ID

        Returns:
            Dict: Specified users pickup group, and the users within that group.
        """

        endpoint = "/groups/call-pickup/user"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_call_pickup_available_users(self, service_provider_id: str, group_id: str):
        """Retrieves available users to assign to a pick up group for the specified group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.

        Returns:
            Dict: Available users to assign to a pick up group for the specified group.
        """

        endpoint = "groups/call-pickup/users"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_call_pickup_group(
        self, service_provider_id: str, group_id: str, pickup_group_name: str
    ):
        """Creates a new pickup group for the specified group

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            pickup_group_name (str): The Target Pickup Group Name

        Returns:
            Dict: The newly created pickup group.
        """

        endpoint = "/groups/call-pickup/groups"

        payload = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": pickup_group_name,
        }

        return self._requester.post(endpoint, data=payload)

    # PUT

    def put_call_pickup_group(
        self,
        service_provider_id: str,
        group_id: str,
        pickup_group_name: str,
        new_group_name: str,
        users: list[str] = [],
    ):
        """Updates the name of a pickup group for the specified group

        Note: When updating users include all users in the group, not just the ones being added.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            pickup_group_name (str): The Target Pickup Group Name
            new_group_name (str): The new name of the pickup group
            users (list[str]): The list of user IDs to add to the pickup group

        Raises:
            ValueError: If no users or new_group_name are provided

        Returns:
            Dict: The updated pickup group.
        """

        endpoint = "/groups/call-pickup/groups"

        updates = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": pickup_group_name,
        }

        if not users and not new_group_name:
            raise ValueError("At least one of users or new_group_name must be provided")
        if users:
            updates["users"] = [{"userId": u} for u in users]
        if pickup_group_name:
            updates["name"] = new_group_name

        return self._requester.put(endpoint, data=updates)

    # DELETE

    def delete_call_pickup_group(
        self, service_provider_id: str, group_id: str, pickup_group_name: str
    ):
        """Deletes a pickup group for the specified group

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): The Target Group ID the user is apart of.
            pickup_group_name (str): The Target Pickup Group Name
        """

        endpoint = "/groups/call-pickup/groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": pickup_group_name,
        }

        return self._requester.delete(endpoint, params=params)
