from .base_endpoint import BaseEndpoint

class VoiceMessaging(
    BaseEndpoint
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET
    def get_group_voice_messaging(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """Retrieves The Groups Advanced Voice Messaging Service Settings

        Args:
            service_provider_id (str): Provider ID For The Groups Voice Message Service Setting
            group_id (str): Group ID For The Groups Voice Message Service Setting

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: Advanced Voice Messaging Json Stub
        """
        endpoint: str = "/groups/voice-messaging?"

        params: dict = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_group_voice_messaging_portal(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """Retrieves The Groups Advanced Voice Messaging Portal Service Settings

        Args:
            service_provider_id (str): Provider ID For The Groups Voice Message Portal Service Setting
            group_id (str): Group ID For The Groups Voice Message Portal Service Setting

        Raises:
            None: This Method Raises No Error

        Returns:
            None: Advanced Voice Messaging Portal Json Stub
        """
        endpoint: str = "/groups/voice-messaging/voice-portal?"

        params: dict = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self._requester.get(endpoint, params=params)

    def get_user_voice_messaging(
        self,
        user_id: str
    ):
        """Retrieves The User's Voice Messaging Service Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service Settings

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Voice Messaging Service Settings JSON Stub
        """
        endpoint: str = "/users/voice-messaging?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_messages(
        self,
        user_id: str
    ):
        """Retrieves The User's Voice Messaging Messages

        Args:
            user_id (str): The User ID For The Voice Messaging Messages

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Voice Messaging Messages JSON Stub
        """
        endpoint: str = "/users/voice-messaging/messages?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_message_details(
        self,
        user_id: str,
        id: str
    ):
        """Retrieves Details Of A Specific User Voice Message

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            id (str): The Message ID For The Specific Voice Message

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: Detailed Information Of The Specified Voice Message
        """
        endpoint: str = "/users/voice-messaging/message?"

        params: dict = {
            "userId": user_id,
            "id": id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_message_download(
        self,
        user_id: str,
        id: str
    ):
        """Downloads A Specific User Voice Message

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            id (str): The Message ID For The Specific Voice Message

        Raises:
            None: This Method Raises No Error

        Returns:
            bytes: The Downloaded Voice Message File
        """
        endpoint: str = "/users/voice-messaging/messages/download?"

        params: dict = {
            "userId": user_id,
            "id": id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_voice_portal(
        self,
        user_id: str
    ):
        """Retrieves The User's Voice Messaging Voice Portal Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Voice Messaging Voice Portal Settings JSON Stub
        """
        endpoint: str = "/users/voice-messaging/voice-portal?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_user_distribution_list(
        self,
        user_id: str,
        list_id: int
    ):
        """Retrieves A Specific User Distribution List For Voice Messaging

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            list_id (int): The Distribution List ID

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Distribution List Details JSON Stub
        """
        endpoint: str = "/users/voice-messaging/user-distribution-list?"

        params: dict = {
            "userId": user_id,
            "listId": list_id
        }

        return self._requester.get(endpoint, params=params)


    def get_user_voice_messaging_user_distribution_lists(
        self,
        user_id: str
    ):
        """Retrieves All User Distribution Lists For Voice Messaging

        Args:
            user_id (str): The User ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: List Of User Distribution Lists JSON Stub
        """
        endpoint: str = "/users/voice-messaging/user-distribution-lists?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_advanced(
        self,
        user_id: str
    ):
        """Retrieves The User's Advanced Voice Messaging Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Advanced Voice Messaging Settings JSON Stub
        """
        endpoint: str = "/users/voice-messaging/advanced?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)
    
    def get_user_voice_messaging_greetings(
        self,
        user_id: str
    ):
        """Retrieves The User's Voice Messaging Greetings

        Args:
            user_id (str): The User ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: User Voice Messaging Greetings JSON Stub
        """
        endpoint: str = "/users/voice-messaging/greetings?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.get(endpoint, params=params)

    def get_user_voice_messaging_bulk(
        self,
        service_provider_id: str,
        group_id: str
    ):
        """Retrieves Bulk Voice Messaging Settings For A Group

        Args:
            service_provider_id (str): Provider ID For The Group Voice Messaging Service
            group_id (str): Group ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            dict: Bulk Voice Messaging Settings JSON Stub
        """
        endpoint: str = "/users/voice-messaging/bulk?"

        params: dict = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id
        }

        return self._requester.get(endpoint, params=params)
    
    # PUT
    def put_group_voice_messaging(
        self,
        service_provider_id: str,
        group_id: str,
        updates: dict
    ):
        """Modifies The Groups Advanced Voice Messaging Service Settings

        Args:
            service_provider_id (str): Provider ID For The Groups Voice Message Service Setting
            service_provider_id (str): Group ID For The Groups Voice Message Service Setting
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None: 
        """
        endpoint: str = "/groups/voice-messaging"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id

        return self._requester.put(endpoint, data=updates)
    
    def put_group_voice_messaging_portal(
        self,
        service_provider_id: str,
        group_id: str,
        updates: dict
    ):
        """Modifies The Groups Advanced Voice Messaging Portal Service Settings

        Args:
            service_provider_id (str): Provider ID For The Groups Voice Message Portal Service Setting
            group_id (str): Group ID For The Groups Voice Message Portal Service Setting
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/groups/voice-messaging/voice-portal"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id

        return self._requester.put(endpoint, data=updates)
        
    def put_user_voice_messaging(
        self,
        user_id: str,
        updates: dict
    ):
        """Modifies The User's Voice Messaging Service Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service Settings
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging"

        updates["userId"] = user_id

        return self._requester.get(endpoint, data=updates)

    def put_user_voice_messaging_messages_read(
        self,
        user_id: str,
        updates: dict
    ):
        """Marks User Voice Messages As Read

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            updates (dict): List Of Message IDs To Mark As Read

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/messages/read"

        params: dict = {
            "userId": user_id
        }

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates, params=params)


    def put_user_voice_messaging_messages_unread(
        self,
        user_id: str,
        updates: dict
    ):
        """Marks User Voice Messages As Unread

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            updates (dict): List Of Message IDs To Mark As Unread

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/messages/unread"

        params: dict = {
            "userId": user_id
        }

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates, params=params)

    def put_user_voice_messaging_voice_portal(
        self,
        user_id: str,
        updates: dict
    ):
        """Modifies The User's Voice Messaging Voice Portal Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/voice-portal"

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_voice_messaging_greetings(
        self,
        user_id: str,
        updates: dict
    ):
        """Modifies The User's Voice Messaging Greetings

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/greetings"

        updates["userId"] = user_id

        return self._requester.get(endpoint, data=updates)

    def put_user_voice_messaging_advanced(
        self,
        user_id: str,
        updates: dict
    ):
        """Modifies The User's Advanced Voice Messaging Settings

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/advanced"

        updates["userId"] = user_id

        return self._requester.get(endpoint, data=updates)

    def put_user_voice_messaging_bulk(
        self,
        updates: dict
    ):  
        """Modifies Bulk Voice Messaging Settings For A Group

        Args:
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/bulk"

        return self._requester.put(endpoint, data=updates)

    def put_user_voice_messaging_user_distribution_list(
        self,
        user_id: str,
        list_id: int,
        updates: dict
    ):
        """Modifies A Specific User Distribution List For Voice Messaging

        Args:
            user_id (str): The User ID For The Voice Messaging Service
            list_id (int): The Distribution List ID
            updates (dict): Formatted Data To Emplace In The Put Request

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/user-distribution-list"

        updates["userId"] = user_id
        updates["listId"] = list_id

        return self._requester.get(endpoint, data=updates)
    
    # DELETE
    def delete_user_voice_messaging_messages(
        self,
        user_id: str
    ):
        """Deletes All User Voice Messages

        Args:
            user_id (str): The User ID For The Voice Messaging Service

        Raises:
            None: This Method Raises No Error

        Returns:
            None:
        """
        endpoint: str = "/users/voice-messaging/messages?"

        params: dict = {
            "userId": user_id
        }

        return self._requester.delete(endpoint, params=params)
    
    # POST
