from .base_endpoint import BaseEndpoint


class Groups(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_groups(self, service_provider_id: str) -> list:
        """Returns the specificied Service Provider's Groups.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            List: List of groups and their Names, alongside groupID's and userLimits.
        """

        endpoint = "/groups"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group(self, service_provider_id: str, group_id: str) -> dict:
        """Returns the specificied Group's settings and information.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            Dict: Returns information about the specified group, such as the DID, userCount and Domain.
        """

        endpoint = "/groups"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    # POST
    def post_group(
        self,
        default_domain: str,
        user_limit: int,
        group_id: str,
        group_name: str,
        service_provider_id: str,
    ) -> dict:
        """Creates a new Group.

        Args:
            default_domain (str): Default Domain for the Group
            user_limit (int): User Limit for the Group
            group_id (str): Target Group ID
            group_name (str): Name of the Group
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Returns the newly created Group's information, such as the ID, userCount, Domain and Timezone.
        """

        endpoint = "/groups"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "groupName": group_name,
            "userLimit": user_limit,
            "defaultDomain": default_domain,
        }

        return self._requester.post(endpoint, data=data)

    # PUT

    def put_group(
        self,
        service_provider_id: str,
        group_id: str,
        default_domain: str,
        timezone: str,
        updates: dict,
    ) -> dict:
        """Updates an existing Group with the specified settings.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID
            default_domain (str): Default Domain of the Group
            timezone (str): Timezone of the Group
            updates (dict): Dictionary of updates to apply to the group.

        Returns:
            Dict: Returns the updated Group's information, such as the ID, userCount, Domain and Timezone.
        """

        endpoint = "/groups"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "defaultDomain": default_domain,
            "timeZone": timezone,
            **updates,
        }

        return self._requester.put(endpoint, data=data)

    # DELETE

    def delete_group(self, service_provider_id: str, group_id: str) -> dict:
        """Deletes a Group and all associated users, settings, services and numbers.

        Please use with caution! This action is irreversible unless you have a backup of the group.

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID

        Returns:
            Dict: Returns the deleted Group's information, such as the ID, userCount, Domain and Timezone.
        """

        endpoint = "/groups"

        data = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.delete(endpoint, data=data)
