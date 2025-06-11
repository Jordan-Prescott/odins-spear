from .base_endpoint import BaseEndpoint


class SharedCallAppearance(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_user_shared_call_appearance(self, user_id: str):
        """Gets all Shared Call Appearances (SCAs) for a specified user.

        Args:
            user_id (str): Target user id of user to get SCA for.

        Returns:
            dict: List of SCA details for specified user alongside SCA settings.
        """

        endpoint = "/users/shared-call-appearance"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_shared_call_appearance_bulk(
        self, service_provider_id: str, group_id: str
    ):
        """Gets all Shared Call Appearances (SCAs) within a specified group.

        Args:
            service_provider_id (str): Target service provider id where group is located.
            group_id (str): Target group id to pull SCA details for.

        Returns:
            dict: List of SCA details for specified group.
        """

        endpoint = "/users/shared-call-appearance/bulk"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_user_shared_call_appearance_endpoint(
        self, device_level: str, device_name: str, user_id: str, line_port: str
    ):
        """Gets a specific Shared Call Appearance (SCA) endpoint for a specified user.

        Args:
            device_level (str): Target device level of SCA endpoint to pull details for.
            device_name (str): Target device name of SCA endpoint to pull details for.
            user_id (str): Target user id of user to get SCA endpoint for.
            line_port (str): Target line port of SCA endpoint to pull details for.

        Returns:
            dict: SCA endpoint details such as if the endpoint is active, if it allows origination, if it allows termination, and the device name and level.
        """

        endpoint = "/users/shared-call-appearance/endpoints"

        params = {
            "deviceLevel": device_level,
            "deviceName": device_name,
            "userId": user_id,
            "linePort": line_port,
        }

        return self._requester.get(endpoint, params=params)

    # POST

    def post_user_shared_call_appearance_endpoint(
        self, user_id: str, line_port: str, device_name: str
    ):
        """Creates a new Shared Call Apprance (SCA) on a single user.

        Args:
            user_id (str): Target user id of user to create SCA on.
            line_port (str): Line port to be assigned to the new SCA.
            device_name (_type_): Device to add for SCA from available devices.

        Returns:
            dict: New SCA details applied to user.
        """

        endpoint = "/users/shared-call-appearance/endpoints"

        data = {
            "userId": user_id,
            "linePort": line_port,
            "isActive": True,
            "allowOrigination": True,
            "allowTermination": True,
            "deviceName": device_name,
            "deviceLevel": "Group",
        }

        return self._requester.post(endpoint, data=data)

    # PUT

    def put_user_shared_call_appearance(self, user_id: str, settings: dict):
        """Updates the Shared Call Appearance (SCA) settings for a specified user.

        Args:
            user_id (str): Target user id of user to update SCA settings for.
            settings (dict): Dictionary of updates to apply to the SCA settings.

        Returns:
            dict: Updated SCA settings for specified user.
        """

        endpoint = "/users/shared-call-appearance"

        updates = {
            "userId": user_id,
            **settings,
        }

        return self._requester.put(endpoint, data=updates)

    def put_user_shared_call_appearance_endpoint(
        self,
        user_id: str,
        line_port: str,
        device_name: str,
        device_level: str,
        is_active: bool,
        allow_origination: bool,
        allow_termination: bool,
    ):
        """Updates the Shared Call Appearance (SCA) endpoint settings for a specified user.

        Args:
            user_id (str): Target user id of user to update SCA endpoint settings for.
            line_port (str): Target line port of SCA endpoint to update settings for.
            device_name (str): Target device name of SCA endpoint to update settings for.
            device_level (str): Target device level of SCA endpoint to update settings for.
            is_active (bool): Whether the SCA endpoint is active.
            allow_origination (bool): Whether the SCA endpoint allows origination.
            allow_termination (bool): Whether the SCA endpoint allows termination.

        Returns:
            dict: Updated SCA endpoint settings for specified user.
        """

        endpoint = "/users/shared-call-appearance/endpoints"

        updates = {
            "userId": user_id,
            "linePort": line_port,
            "deviceName": device_name,
            "deviceLevel": device_level,
            "isActive": is_active,
            "allowOrigination": allow_origination,
            "allowTermination": allow_termination,
        }

        return self._requester.put(endpoint, data=updates)

    # DELETE

    def delete_user_shared_call_appearance_endpoint(
        self, device_level: str, device_name: str, user_id: str, line_port: str
    ):
        """Deletes a Shared Call Appearance (SCA) endpoint for a specified user.

        Please use with caution! This action is irreversible unless you have a backup of the SCA endpoint.

        Args:
            device_level (str): Target device level of SCA endpoint to delete.
            device_name (str): Target device name of SCA endpoint to delete.
            user_id (str): Target user id of user to delete SCA endpoint for.
            line_port (str): Target line port of SCA endpoint to delete.

        Returns:
            dict: Deleted SCA endpoint details.
        """

        endpoint = "/users/shared-call-appearance/endpoints"

        params = {
            "deviceLevel": device_level,
            "deviceName": device_name,
            "userId": user_id,
            "linePort": line_port,
        }

        return self._requester.delete(endpoint, params=params)
