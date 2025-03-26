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

    def post_service_provider_device(
        self,
        service_provider_id: str,
        device_name: str,
        device_type: str,
        device_level: str,
        payload: dict
    ):
        """
        """

        endpoint: str = "/service-providers/devices"

        payload["serviceProviderId"] = (
            service_provider_id
            if not payload.get("serviceProviderId")
            else payload["serviceProviderId"]
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
    
    def post_system_device(
            self,
            service_provider_id: str,
            device_name: str
    ):
        endpoint = "/groups/devices/reset"
            
        params = {
            "deviceName": device_name,
            "serviceProviderId": service_provider_id
        }

        return self._requester.post(endpoint, data=params)

    def post_group_device_reset(
            self,
            service_provider_id: str,
            group_id: str,
            device_name: str
    ):
        """Rest device. This is for a single device **Not Group Wide**

        Args:
            service_provider_id (str): Service provider ID where the device should be reset.
            group_id (str): Group ID where the device should be reset.
            device_name (str): Name of the device.

        Returns:
            Dict: 
        """
        endpoint = "/groups/devices/reset"

        params = {
            "deviceName": device_name,
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self._requester.post(endpoint, data=params)
    
    def post_group_device_rebuild(
            self,
            service_provider_id: str,
            group_id: str,
            device_name: str
    ):
        """Rebuild the device files. This is for a single device **Not Group Wide**

        Args:
            service_provider_id (str): Service provider ID where the device should be rebuilt.
            group_id (str): Group ID where the device should be rebuilt.
            device_name (str): Name of the device.

        Returns:
            Dict: 
        """
        endpoint = "/groups/devices/rebuild"

        params = {
            "deviceName": device_name,
            "serviceProviderId": service_provider_id,
            "groupId": group_id
        }

        return self._requester.post(endpoint, data=params)

    def post_service_provider_device_reset(
            self,
            service_provider_id: str,
            device_name: str
    ):
        """Reset the device files. This is **Group Wide*

        Args:
            service_provider_id (str): Service provider ID where the device should be reset.
            device_name (str): Name of the device.

        Returns:
            Dict: 
        """
        endpoint = "/service-providers/devices/reset"

        params = {
            "deviceName": device_name,
            "serviceProviderId": service_provider_id
        }

        return self._requester.post(endpoint, data=params)
    
    def post_service_provider_device_rebuild(
            self,
            service_provider_id: str,
            device_name: str
    ):
        """Rebuild the device files. This is **Group Wide*

        Args:
            service_provider_id (str): Service provider ID where the device should be rebuilt.
            device_name (str): Name of the device.

        Returns:
            Dict: 
        """
        endpoint = "/service-providers/devices/rebuild"

        params = {
            "deviceName": device_name,
            "serviceProviderId": service_provider_id
        }

        return self._requester.post(endpoint, data=params)
    
    def post_system_device_rebuild(
            self,
            device_name: str
    ):
        """Rebuild the device at system level.

        Args:
            device_name (str): Name of the device to have files rebuilt.

        Returns:
            Dict: 
        """
        endpoint = "/system/devices/rebuild"

        params = {
            "deviceName": device_name
        }

        return self._requester.post(endpoint, data=params)
 
    def post_system_device_reset(
            self,
            device_name: str
    ):
        """Reset the device at system level.

        Args:
            device_name (str): Name of the device to be reset.

        Returns:
            Dict: 
        """
        endpoint = "/system/devices/reset"

        params = {
            "deviceName": device_name
        }

        return self._requester.post(endpoint, data=params)

    def post_group_device_tag(
            self,
            service_provider_id: str,
            group_id: str,
            tag_name: str,
            tag_value: str,
            device_name: str
        ):

        """Rebuild the device type files group wide.

            Args:
                service_provider_id (str): Service provider ID where the device should be rebuilt.
                group_id (str): Group ID where the device should be rebuilt.
                tag_name (str): Name of tag has to start and end with %, example - %MyTagName%.
                tag_value (str): Value of tag, this can be anything.
                device_name (str): Name of Device.

            Returns:
                Dict: 
            """
        endpoint = "/groups/devices/tags"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "tagName": tag_name,
            "tagValue": tag_value,
            "deviceName": device_name
        }
        
        return self._requester.post(endpoint, data=params)
    
    def post_service_provider_device_tag(
            self,
            service_provider_id: str,
            tag_name: str,
            tag_value: str,
            device_name: str
        ):

        """Rebuild the device type files group wide.

            Args:
                service_provider_id (str): Service provider ID where the device should be rebuilt.
                tag_name (str): Name of tag has to start and end with %, example - %MyTagName%.
                tag_value (str): Value of tag, this can be anything.
                device_name (str): Name of Device.

            Returns:
                Dict: 
            """
        endpoint = "/service-providers/devices/tags"

        params = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "tagName": tag_name,
            "tagValue": tag_value,
            "deviceName": device_name
        }
        
        return self._requester.post(endpoint, data=params)

    def post_group_device_type_rebuild(
                self,
                service_provider_id: str,
                group_id: str,
                device_type: str
        ):
            """Rebuild the device type files group wide.

            Args:
                service_provider_id (str): Service provider ID where the device should be rebuilt.
                group_id (str): Group ID where the device should be rebuilt.
                device_type (str): Name of the device type.

            Returns:
                Dict: 
            """
            endpoint = "/groups/device-types/rebuild"

            params = {
                "serviceProviderId": service_provider_id,
                "groupId": group_id,
                "deviceType": device_type
            }

            return self._requester.post(endpoint, data=params)

    def post_group_device_type_reset(
                self,
                service_provider_id: str,
                group_id: str,
                device_type: str
        ):
            """Reset the device group side.

            Args:
                service_provider_id (str): Service provider ID where the device should be reset.
                group_id (str): Group ID where the device should be reset.
                device_type (str): Name of the device type.

            Returns:
                Dict: 
            """
            endpoint = "/groups/device-types/reset"

            params = {
                "serviceProviderId": service_provider_id,
                "groupId": group_id,
                "deviceType": device_type
            }

            return self._requester.post(endpoint, data=params)
