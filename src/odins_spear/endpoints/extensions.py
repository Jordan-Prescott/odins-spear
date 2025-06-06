from .base_endpoint import BaseEndpoint


class Extensions(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_group_extensions(self, service_provider_id: str, group_id: str):
        """
        Gets extension settings for a group.

        Args:
            service_provider_id (str): The service provider ID.
            group_id (str): The group ID.
        """
        endpoint = "/groups/extensions"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    # POST

    # PUT

    def put_group_extensions(
        self,
        service_provider_id: str,
        group_id: str,
        min_ext_length: int = None,
        max_ext_lenth: int = None,
        default_ext_length: int = None,
    ):
        """
        Updates extension settings for a group.

        Args:
            service_provider_id (str): The service provider ID.
            group_id (str): The group ID.
            min_ext_length (int): The minimum extension length. Defaults to None.
            max_ext_lenth (int): The maximum extension length. Defaults to None.
            default_ext_length (int): The default extension length.Defaults to None.
        """
        endpoint = "/groups/extensions"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        if min_ext_length:
            params["minExtensionLength"] = min_ext_length
        if max_ext_lenth:
            params["maxExtensionLength"] = max_ext_lenth
        if default_ext_length:
            params["defaultExtensionLength"] = default_ext_length

        return self._requester.put(endpoint, params=params)

    # DELETE
