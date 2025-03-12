from .base_endpoint import BaseEndpoint


class Administrators(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    # POST

    def post_service_provider_admin(
        self,
        service_provider_id: str,
        user_id: str,
        password: str,
        first_name: str,
        last_name: str,
        language: str = "English",
        admin_type: str = "Normal",
        payload: dict = {},
    ):
        """Builds service provider administrator account.

        Args:
            service_provider_id (str): Target service parovider to build account.
            user_id (str): User ID of new account i.e. 'firstname.lastname@domain.com'
            password (str): Web access password user needs to log in.
            first_name (str): First name.
            last_name (str): Last name.
            language (str, optional): Find supported languages on your system. Defaults to "English".
            admin_type (str, optional): Type of admin, options: 'normal', 'customer', 'password reset only'. Defaults to normal.
            payload (dict, optional): Payload sent to API. Defaults to empty dict and is formatted for you.
        """

        endpoint = "/service-providers/admins"

        payload["serviceProviderId"] = service_provider_id
        payload["language"] = language
        payload["administratorType"] = admin_type.capitalize()
        payload["userId"] = user_id
        payload["password"] = password
        payload["firstName"] = first_name
        payload["lastName"] = last_name

        return self._requester.post(endpoint, data=payload)

    def post_group_admin(
        self,
        service_provider_id: str,
        group_id: str,
        user_id: str,
        password: str,
        payload: dict = {},
    ):
        """Builds a group-level administrator.

        Args:
            service_provider_id (str): Service provider ID where the admin should be built.
            group_id (str): Group ID where the admin should be built
            user_id (str): User ID of the admin.
            password (str): Password for the administrator profile. Note get.password_generate() can be used to get this.
            payload (dict, optional): Admin configuration data.

        Returns:
            Dict: Returns the admin profile.
        """

        endpoint = "/groups/admins"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["password"] = password

        return self._requester.post(endpoint, data=payload)

    def post_group_admin_policies_bulk(self, user_ids: list, policy_config: dict):
        """Applies policy settings to multiple group administrators.

        Note: See docs for formatting of parameters.

        Args:
            user_ids (list): User IDs of admins to apply policy to.
            policy_config (dict): Policy settings to apply to target users.

        Returns:
            Dict: Returns admins and policy applied.
        """
        endpoint = "/groups/admins/policies/bulk"

        data = {"users": [{"userId": user} for user in user_ids], "data": policy_config}

        self._requester.post(endpoint, data=data)

    # PUT

    def put_service_provider_admin_policies(self, user_id: str, policy_config: dict):
        """AI is creating summary for put_service_provider_admin_policies

        Args:
            user_id (str): User ID of target service provider admin.
            policy_config (dict): Policy settings to update.
        """

        endpoint = "/service-providers/admins/policies"

        policy_config["userId"] = user_id

        return self._requester.put(endpoint, data=policy_config)

    # DELETE
