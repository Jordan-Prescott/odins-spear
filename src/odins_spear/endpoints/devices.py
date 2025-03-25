from .base_endpoint import BaseEndpoint
from ..utils.formatters import format_filter_value


class Devices(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET
    def get_group_devices(
        self,
        service_provider_id: str,
        group_id: str,
        filter: str = None,
        filter_type: str = None,
        filter_value: str = None,
        limit: int = None,
    ):
        """
        
        """

        endpoint: str = "/groups/devices?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        if filter:
            params[filter] = format_filter_value(filter_type, filter_value)
        if limit:
            params["limit"] = limit

        return self._requester.get(endpoint, params=params)
    
    def get_group_device(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        filter: str = None,
        filter_type: str = None,
        filter_value: str = None,
        limit: int = None,
    ):
        """
        
        """
        
        endpoint: str = "/groups/devices?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name
        }

        if filter:
            params[filter] = format_filter_value(filter_type, filter_value)
        if limit:
            params["limit"] = limit

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_available_ports(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        device_level: str = "Group"
    ):
        """
        """

        endpoint: str = "/groups/devices/available-ports?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name,
            "deviceLevel": device_level
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_devices_available(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """
        """

        endpoint: str = "/groups/devices?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "q": "available"
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_users(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str
    ):
        """
        """

        endpoint: str = "/groups/devices/users?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)


