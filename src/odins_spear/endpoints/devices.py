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
    
    def get_service_provider_devices(
        self,
        service_provider_id: str
    ):
        """
        """

        endpoint: str = "/service-providers/devices?"

        params: dict = {
            "serviceProviderId": service_provider_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_service_provider_device(
        self,
        service_provider_id: str,
        device_name: str,
        q: str = "available",
        group_id: str = None
    ):
        """
        """

        endpoint: str = "/service-providers/devices?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceName": device_name,
            "q": q
        }

        if group_id:
            params["groupId"] = group_id

        return self._requester.get(endpoint, params=params)
    
    def get_service_provider_device_user(
        self,
        service_provider_id: str,
        device_name: str
    ):
        """
        """

        endpoint: str = "/service-providers/devices/users?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_system_device_types(
        self
    ):
        """
        """

        endpoint: str = "/system/device-types"

        return self._requester.get(endpoint)

    def get_system_devices(
        self
    ):
        """
        """

        endpoint: str = "/system/devices"

        return self._requester.get(endpoint)
    
    def get_system_device(
        self,
        device_name: str
    ):
        """
        """

        endpoint: str = "/system/devices?"

        params: dict = {
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)

    def get_system_device_user(
        self,
        device_name: str
    ):
        """
        """

        endpoint: str = "/system/devices/users?"

        params: dict = {
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)  

    def get_group_device_files(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str
    ):
        """
        """

        endpoint: str = "/groups/devices/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_file(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        file_format: str
    ):
        """
        
        """

        endpoint: str = "/groups/devices/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name,
            "fileFormat": file_format
        }

        return self._requester.get(endpoint, params=params)
    
    def get_service_provider_device_files(
        self,
        service_provider_id: str,
        device_name: str
    ):
        """
        """

        endpoint: str = "/service-providers/devices/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_service_provider_device_file(
        self,
        service_provider_id: str,
        device_name: str,
        file_format: str
    ):
        """
        
        """

        endpoint: str = "/service-providers/devices/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceName": device_name,
            "fileFormat": file_format
        }

        return self._requester.get(endpoint, params=params)

    def get_system_device_files(
        self,
        device_name: str
    ):
        """
        """

        endpoint: str = "/system/devices/files?"

        params: dict = {
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_system_device_file(
        self,
        device_name: str,
        file_format: str
    ):
        """
        
        """

        endpoint: str = "/system/devices/files?"

        params: dict = {
            "deviceName": device_name,
            "fileFormat": file_format
        }

        return self._requester.get(endpoint, params=params)

    def get_group_device_tags(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str
    ):
        """
        
        """

        endpoint: str = "/groups/devices/tags?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)

    def get_group_device_tags(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str,
        device_name: str
    ):
        """
        
        """

        endpoint: str = "/groups/devices/profile?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)

    def get_group_device_tags_bulk(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """
        
        """

        endpoint: str = "/groups/devices/tags?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_service_provider_device_tags(
        self,
        service_provider_id: str,
        device_name: str
    ):
        """
        
        """

        endpoint: str = "/service-providers/devices/tags?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_system_device_tags(
        self,
        device_name: str
    ):
        """
        
        """

        endpoint: str = "/system/devices/tags?"

        params: dict = {
            "deviceName": device_name
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_types(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """
        """

        endpoint: str = "/groups/device-types?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_type(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str
    ):
        """
        """

        endpoint: str = "/groups/device-types?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_type_files(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str
    ):
        """
        """

        endpoint: str = "/groups/device-types/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_type_files(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str,
        file_format: str
    ):
        """
        """

        endpoint: str = "/groups/device-types/files?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type,
            "fileFormat": file_format
        }

        return self._requester.get(endpoint, params=params)

    def get_group_device_type_tags(
        self,
        service_provider_id: str,
        group_id: str,
        device_type: str
    ):
        """
        """

        endpoint: str = "/groups/device-types/tags?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "deviceType": device_type
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_device_type_tags(
        self,
        service_provider_id: str,
        device_type: str
    ):
        """
        """

        endpoint: str = "/service-providers/device-types/tags?"

        params: dict = {
            "serviceProviderId": service_provider_id,
            "deviceType": device_type
        }

        return self._requester.get(endpoint, params=params)
    
    # POST
    def post_group_device(
        self,
        service_provider_id: str,
        group_id: str,
        device_name: str,
        device_type: str,
        device_level: str,
        payload: dict
    ):
        """
        """

        endpoint: str = "/groups/devices"

        payload["serviceProviderId"] = (
            service_provider_id
            if not payload.get("serviceProviderId")
            else payload["serviceProviderId"]
        )

        payload["groupId"] = (
            group_id
            if not payload.get("groupId")
            else payload["groupId"]
        )

        payload["deviceName"] = (
            device_name
            if not payload.get("deviceName")
            else payload["deviceName"]
        )

        payload["deviceType"] = (
            device_type
            if not payload.get("deviceType")
            else payload["deviceType"]
        )

        payload["deviceLevel"] = (
            device_level
            if not payload.get("deviceLevel")
            else payload["deviceLevel"]
        )

        return self._requester.post(endpoint, data=payload)
