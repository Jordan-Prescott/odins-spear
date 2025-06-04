from .base_endpoint import BaseEndpoint


class TrunkGroups(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET
    def get_group_trunk_groups_call_capacity(
        self, service_provider_id: str, group_id: str
    ):
        """Fetches Trunk Call Capacity data for a single Group.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Target Group to return data on.

        Returns:
            Dict: Trunk Group Call Capacity data of target group.
        """

        endpoint = "/groups/trunk-groups/call-capacity"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_trunk_group(
        self, service_provider_id: str, group_id: str, trunk_group_name: str
    ):
        """Fetches all Trunk Group details of a single Trunk Group in a Group.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Group ID where the target Trunk Group is located.
            trunk_group_name (str): Target Trunk Group Name.

        Returns:
            Dict: Details of a target trunk group.
        """

        endpoint = "/groups/trunk-groups"

        params = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "name": trunk_group_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_group_trunk_groups(self, service_provider_id: str, group_id: str):
        """Fetches list of all trunk groups in a single group.

        Args:
            service_provider_id (str): Service Provider/ Enterprise ID where Group is located.
            group_id (str): Group ID where the target Trunk Group is located.

        Returns:
            List: List of core details of all Trunk Groups located in a single Group.
        """

        endpoint = "/groups/trunk-groups"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_service_provider_trunk_group_call_capacity(self, service_provider_id: str):
        """Fetches trunk call capacity details of a single Service Provider.

        Args:
            service_provider_id (str): Target Service Provider/ Enterprise ID.

        Returns:
            Dict: Trunk call capacity details of a single Service Provider/ Enterprise ID.
        """

        endpoint = "/service-providers/trunk-groups/call-capacity"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_service_provider_trunk_call_capacity_report(self, service_provider_id: str):
        """Fetches trunk call capacity details of Service Provider/ Enterprise and all Groups in the SP/ ENT.

            Args:
                servive_provider_id (str): Target Service Provider/ Enterprise ID.

            Returns:
                Dict: Breakdown of all trunk call capacity details of target Service Provider/ Enterprise and all Groups \
                    in the target SP/ ENT.
            """

        endpoint = "/service-providers/trunk-groups/call-capacity/reports"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_group_trunk_group_users(
        self, service_provider_id: str, group_id: str, trunk_name: str
    ):
        """Fetches a list of users assigned to a specific trunk.

        Args:
            service_provider_id (str): Target service provider id
            group_id (str): Target group id where trunk group is hosted
            name (str): Target trunk group

        Returns:
            Dict: Trunk group and list of users assigned
        """
        endpoint = "/groups/trunk-groups/users"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": trunk_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_group_trunk_available_hosted_users(
        self, service_provider_id: str, group_id: str, trunk_name: str
    ):
        """Fetches a list of users available to assign to the trunk group

        Args:
            service_provider_id (str): Target service provider id
            group_id (str): Target group id where trunk group is hosted
            name (str): Target trunk group

        Returns:
            Dict: List of available users for assigning to trunk group
        """
        endpoint = "/groups/trunk-groups/users/hosted"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": trunk_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_service_providers_trunk_call_capacity_report_show(
        self, service_provider_id: str
    ):
        """Returns a report of each group in a Servcice Provider showing their call capacity values etc.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Detailed report of group and trunk group details.
        """
        endpoint = "/service-providers/trunk-groups/call-capacity/reports"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    # POST
    def post_group_trunk_group(
        self,
        service_provider_id: str,
        group_id: str,
        trunk_name: str,
        max_active_calls: int,
        payload: dict = {},
        sip_authentication_username: str = "",
        sip_authentication_password: str = "",
    ):
        """
        Builds a Trunk Group (TG) in the specified group.

        Args:
            service_provider_id (str): The service provider ID in which the target group is built.
            group_id (str): The group ID where the HG should be built.
            trunk_name (str): The name of the new TG.
            max_active_calls (str): The maximum active calls to be set on the TG.
            payload (dict, optional): Configuration for the TG.
            sip_authentication_username (str, optional): The SIP authentication username for the TG. This field is required if "requireAuthentication" is set to "true".
            sip_authentication_password (str, optional): The SIP authentication password for the TG. You can generate a password for this using get.sip_password_generator. This field is required if "requireAuthentication" is set to "true".

        Note:
            Several fields are set to have default values. Please refer to the online documentation.

        Returns:
            Dict: Returns the Trunk Group profile.
        """

        endpoint = "/groups/trunk-groups"

        payload["name"] = trunk_name
        payload["maxActiveCalls"] = max_active_calls
        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id

        default_payload_values = {
            "capacityExceededTrapInitialCalls": 0,
            "capacityExceededTrapOffsetCalls": 0,
            "clidSourceForScreenedCallsPolicy": "Profile Name Profile Number",
            "continuousOptionsSendingIntervalSeconds": 30,
            "failureOptionsSendingIntervalSeconds": 10,
            "failureThresholdCounter": 1,
            "invitationTimeout": 6,
            "inviteFailureThresholdCounter": 1,
            "inviteFailureThresholdWindowSeconds": 30,
            "pilotUserCallOptimizationPolicy": "Optimize For User Services",
            "pilotUserCallingLineAssertedIdentityPolicy": "Unscreened Originating Calls",
            "pilotUserCallingLineIdentityForEmergencyCallsPolicy": "No Calls",
            "pilotUserCallingLineIdentityForExternalCallsPolicy": "No Calls",
            "pilotUserChargeNumberPolicy": "No Calls",
            "successThresholdCounter": 1,
            "useSystemUserLookupPolicy": "true",
            "userLookupPolicy": "Basic",
            "requireAuthentication": "false",
        }
        for key, default_value in default_payload_values.items():
            payload.setdefault(key, default_value)

        if payload["requireAuthentication"]:
            payload["sipAuthenticationUserName"] = sip_authentication_username
            payload["sipAuthenticationPassword"] = sip_authentication_password

        return self._requester.post(endpoint, data=payload)

    # PUT

    def put_group_trunk_groups_call_capacity(
        self,
        service_provider_id: str,
        group_id: str,
        max_active_calls: int,
        bursting_max_active_calls: int = None,
    ):
        """Updates the trunking call capacity in the specified group.

        NOTE: The max available active calls cannot be changed here. Please see service_providers_trunk_group_call_capacity to update this.

        Args:
            service_provider_id (str): Service provider ID where the target group is built
            group_id (str): Group ID whose trunk group call capacity needs updating
            max_active_calls (int): The max active calls for the group
            bursting_max_active_calls (int, optional): The bursting max active calls for the group. Defaults to None.
        """

        endpoint = "/groups/trunk-groups/call-capacity"

        updates = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "maxActiveCalls": max_active_calls,
        }

        if bursting_max_active_calls is not None:
            updates["burstingMaxActiveCalls"] = bursting_max_active_calls

        return self._requester.put(endpoint, data=updates)

    def put_group_trunk_group(
        self,
        service_provider_id: str,
        group_id: str,
        trunk_group_name: str,
        updates: dict,
    ):
        """Updates trunk group (TG) configuration.

        Args:
            service_provider_id (str): Service provider ID where the target group is built.
            group_id (str): Group ID whose trunk group call capacity needs updating.
            trunk_group_name (str): The name of the trunk group that is being updated.
            updates (dict, optional): Updates to be applied to the TG.
        """

        endpoint = "/groups/trunk-groups"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["name"] = trunk_group_name

        return self._requester.put(endpoint, data=updates)

    def put_service_providers_trunk_group_call_capacity(
        self,
        service_provider_id: str,
        max_active_calls: int,
        bursting_max_active_calls: int = None,
    ):
        """Updates the max active calls and the bursting max active calls for the given service provider.

        Args:
            service_provider_id (str): Service provider ID for which the max active calls needs to be updated
            max_active_calls (int): The updates to be applied to the service provider's trunking call capacity
            bursting_max_active_calls (int, optional): Number of bursting calls. Defaults to none, do not include if only changing max active calls.
        """

        endpoint = "/service-providers/trunk-groups/call-capacity"

        updates = {
            "serviceProviderId": service_provider_id,
            "maxActiveCalls": max_active_calls,
        }

        if bursting_max_active_calls is not None:
            updates["burstingMaxActiveCalls"] = bursting_max_active_calls

        return self._requester.put(endpoint, data=updates)

    # DELETE

    def delete_trunk_group(
        self, service_provider_id: str, group_id: str, trunk_name: str
    ):
        """Deletes a trunk group.

        Args:
            service_provider_id (str): Target service provider id
            group_id (str): Target group id where trunk group is hosted
            name (str): Target trunk group

        Returns:
            None
        """
        endpoint = "/groups/trunk-groups"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "name": trunk_name,
        }

        return self._requester.delete(endpoint, params=params)
