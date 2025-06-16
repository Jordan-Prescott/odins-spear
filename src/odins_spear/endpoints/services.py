from .base_endpoint import BaseEndpoint


class Services(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_system_services(self):
        """Fetch all services assigned to the system.

        Returns:
            Dict: A dictionary containing all the services assigned to the system.
        """

        endpoint = "/system/services"

        return self._requester.get(endpoint)

    def get_service_provider_services(
        self,
        service_provider_id: str,
        onlyLicensed: bool = False,
        onlyAuthorised: bool = False,
    ):
        """Fetch all services within a service provider.

        Args:
            service_provider_id (str): Service provider ID of the target
            onlyLicensed (bool, optional): Only fetch licensed services. Defaults to False.
            onlyAuthorised (bool, optional): Only fetch authorised services. Defaults to False.

        Returns:
            Dict: A dictionary containing all the services within the service provider alongside their settings.
        """

        endpoint = "/service-providers/services"

        params = {
            "serviceProviderId": service_provider_id,
            "onlyLicensed": onlyLicensed,
            "onlyAuthorised": onlyAuthorised,
        }

        return self._requester.get(endpoint, params=params)

    def get_service_provider_services_assignable(self, service_provider_id: str):
        """Fetch all services within a service provider that are assignable.

        Args:
            service_provider_id (str): Service provider ID of the target

        Returns:
            Dict: A dictionary with the service names of all assignable services.
        """

        endpoint = "/service-providers/services/assignable"

        params = {
            "serviceProviderId": service_provider_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_service_provider_services_authorized(self, service_provider_id: str):
        """Fetch all services within a service provider that are authorized alongside their quantity and limit.

        Args:
            service_provider_id (str): Service provider ID of the target

        Returns:
            Dict: A dictionary with the service names of all authorized services alongside their quantity and limit.
        """

        endpoint = "/service-providers/services/authorized"

        params = {
            "serviceProviderId": service_provider_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_group_services(self, service_provider_id: str, group_id: str):
        """Fetch all services within a group.

        Args:
            service_provider_id (str): Service provider ID of the target
            group_id (str): Group ID of the target

        Returns:
            Dict: A dictionary with the service names of all User Services, Group Services and Service Pack Services within the group.
        """

        endpoint = "/groups/services"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services_authorized(self, service_provider_id: str, group_id: str):
        """Fetch all services authorized within a group.

        Args:
            service_provider_id (str): Service provider ID of the target
            group_id (str): Group ID of the target

        Returns:
            Dict: A dictionary with the service names of all authorized services within the group.
        """

        endpoint = "/groups/services/authorized"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services_assigned(self, service_provider_id: str, group_id: str):
        """Fetch all services assigned within a group.

        Args:
            service_provider_id (str): Service provider ID of the target
            group_id (str): Group ID of the target

        Returns:
            List: A list with the service names of all assigned services within the group.
        """

        endpoint = "/groups/services/assigned-list"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_service_is_assigned(
        self, service_provider_id: str, group_id: str, service_name: str
    ):
        """Fetch users who a service is assigned to within a group.

        Args:
            service_provider_id (str): Service provider ID of the target
            group_id (str): Group ID of the target
            service_name (str): Service name of the target

        Returns:
            Dict: A dictionary with the users who the service is assigned to.
        """

        endpoint = "/groups/services/assigned"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "serviceName": service_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_user_services_assigned(self, user_id: str):
        """Fetch all services assigned to a user.

        Args:
            user_id (str): User ID of the target

        Returns:
            Dict: A dictionary with the service names of all assigned services.
        """
        endpoint = "/users/services/assigned"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_services(self, user_id: str):
        """Fetch all services assigned to a broadwrok entity, this can be
        a user, AA, CC, or HG.

        Args:
            user_id (str): User ID of the target Broadworks entity.

        Returns:
            Dict: Broadwork entiy and a list of services assigned.
        """

        endpoint = "/users/services"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_service_settings(self, user_id: str):
        """Retrieves all service settings for a specific user.

        Args:
            user_id (str): ID of the target user

        Returns:
            Dict: A dictionary containing all the service settings for the specified user.
        """

        endpoint = "/users/services/settings"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services(self, group_id: str, service_provider_id: str):
        """
        Fetch all userServices, groupServices and servicePackServices assigned to a group.

        Args:
            group_id (str): GroupID of the target
            service_provider_id (str): Service Provider or Enterprise ID of the target.

        Returns:
            Dict: Authorised and assigned services within the group.
        """

        endpoint = "/groups/services"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_services_user_assigned(
        self,
        group_id: str,
        service_provider_id: str,
        service_name: str,
        service_type: str,
    ):
        """
        Get details of the user/service instances where a particular service is assigned.

        Args:
            group_id (str): GroupID being targeted
            service_provider_id (str): Service provider/Enterprise ID where the group is located.
            service_name (str): Name of the service querying
            service_type (str): Type of service. Either: serviceName or servicePackName

        Returns:
            Dict: Users/Service Instances where the service is assigned.
        """

        endpoint = "/groups/services/assigned"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "serviceType": service_type,
            "serviceName": service_name,
        }

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    def put_user_services(
        self,
        user_id: str,
        services: list = None,
        service_packs: list = None,
        assigned: bool = True,
    ):
        """Update the services assigned to a user. NOT service/feature packs.

        Args:
            user_id (str): User ID of the target user.
            services (list): List of services to be applied to user.
            service_packs (list): List of service packs to be applied to user.
            assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.

        Returns:
            Dict: User services assigned to the user.
        """

        endpoint = "/users/services"

        data = {"userId": user_id}

        if services:
            data["userServices"] = [
                {"serviceName": service, "assigned": assigned} for service in services
            ]
        if service_packs:
            data["servicePackServices"] = [
                {"serviceName": service_pack, "assigned": assigned}
                for service_pack in service_packs
            ]
        return self._requester.put(endpoint, data=data)

    def put_user_service_settings(self, user_id: str, settings: dict):
        """Updates specific service settings for a given user.
        This function allows you to modify one or more service settings associated with a particular user.

        Args:
            user_id (str): The ID of the target user
            settings (dict): A dictionary containing the new settings to be applied. The structure of this dictionary should mirror the API's expected format for updating service settings.

        Returns:
            Dict: A dictionary representing the updated service settings for the specified user.
        """

        endpoint = "/users/services/settings"

        data = {"userId": user_id, **settings}

        return self._requester.put(endpoint, data=data)


# DELETE
