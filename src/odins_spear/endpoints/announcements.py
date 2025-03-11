from .base_endpoint import BaseEndpoint
from ..exceptions import OSFileNotFound
import base64


class Announcements(BaseEndpoint):
    def __init__(self):
        super().__init__()

    # GET
    def get_user_announcements(self, user_id: str):
        """Retrieves announcements from the given user, including Anouncement Type and file size limits.

        Args:
            user_id (str): User ID of the target user you would like to retrieve the announcements from.

        Returns:
            Dict: Contains Announcement Info, and a list of Announcements.
        """

        endpoint = "/users/announcements"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_announcements(self, group_id: str, service_provider_id: str):
        """Retrieves announcements from the given Group, including Anouncement Type and file size limits.

        Args:
            group_id (str): Group ID of the target Group you would like to retrieve the announcements from.
            service_provider_id (str): Service Provider ID of where the group resides

        Returns:
            Dict: Contains Announcement Info, and a list of Announcements.
        """

        endpoint = "/groups/announcements"

        params = {"groupId": group_id, "serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_user_announcement(
        self,
        user_id: str,
        name: str,
        description: str,
        file_path: str,
        media_type: str = "WAV",
    ):
        """Adds an announcement to the given user.

        Args:
            user_id (str): User ID of the target user you would like to add the Announcement to.
            name (str): Desired name of the Announcement
            description (str): Description assigned to the Announcement.
            file_path (str): File path to the Announcement Audio File. (Raw String)
            media_type (str): Audio file format

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/users/announcements"

        try:
            with open(
                file_path, "rb"
            ) as audio_file:  # Converts input audio file into b64
                audio_bytes = audio_file.read()
                b64_audio_bytes = base64.b64encode(audio_bytes)
                content = b64_audio_bytes.decode("ascii")
        except FileNotFoundError:
            raise OSFileNotFound

        payload = {
            "userId": user_id,
            "name": name,
            "mediaType": media_type,
            "description": description,
            "content": content,
        }

        return self._requester.post(endpoint, data=payload)

    def post_group_announcement(
        self,
        group_id: str,
        service_provider_id: str,
        name: str,
        description: str,
        file_path: str,
        media_type: str = "WAV",
    ):
        """Adds an announcement to the given user.

        Args:
            group_id (str): Group ID of the target Group you would like to add the Announcement to.
            service_provider_id (str): Service Provider ID of where the group resides
            name (str): Desired name of the Announcement
            description (str): Description assigned to the Announcement.
            file_path (str): File path to the Announcement Audio File. (Raw String)
            media_type (str): Audio file format

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/announcements"

        try:
            with open(
                file_path, "rb"
            ) as audio_file:  # Converts input audio file into b64
                audio_bytes = audio_file.read()
                b64_audio_bytes = base64.b64encode(audio_bytes)
                content = b64_audio_bytes.decode("ascii")
        except FileNotFoundError:
            raise OSFileNotFound

        payload = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "name": name,
            "mediaType": media_type,
            "description": description,
            "content": content,
        }

        return self._requester.post(endpoint, data=payload)

    # PUT

    def put_user_announcement(
        self, user_id: str, name: str, media_type: str, new_name: str
    ):
        """Updates the name of the given user Announcement

        Args:
            user_id (str): User ID of the user the announcement resides
            name (str): Current name of the Announcement
            media_type (str): Audio file format
            new_name (str): Desired name of the Announcement


        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/users/announcements"

        updates = {
            "userId": user_id,
            "name": name,
            "mediaType": media_type,
            "newName": new_name,
        }

        return self._requester.put(endpoint, data=updates)

    def put_group_announcement(
        self,
        group_id: str,
        service_provider_id: str,
        name: str,
        new_name: str,
        media_type: str = "WAV",
    ):
        """Updates the name of the given Group Announcement

        Args:
            group_id (str): Group ID of the target Group you would like to change the Announcement name of.
            service_provider_id (str): Service Provider ID of where the group resides
            name (str): Current name of the Announcement
            new_name (str): Desired name of the Announcement
            media_type (str): Audio file format


        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/announcements"

        updates = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "name": name,
            "mediaType": media_type,
            "newName": new_name,
        }

        return self._requester.put(endpoint, data=updates)

    # DELETE

    def delete_user_announcement(self, user_id: str, name: str, media_type: str):
        """Removes the given user Announcement

        Args:
            user_id (str): User ID of the user the announcement resides
            name (str): Current name of the Announcement
            media_type (str): Audio file format


        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/users/announcements"

        data = {
            "userId": user_id,
            "name": name,
            "mediaType": media_type,
        }

        return self._requester.delete(endpoint, data=data)

    def delete_group_announcement(
        self,
        group_id: str,
        service_provider_id: str,
        name: str,
        media_type: str = "WAV",
    ):
        """Removes the given Group Announcement

        Args:
            group_id (str): Group ID of the target Group you would like to remove
            service_provider_id (str): Service Provider ID of where the group resides
            media_type (str): Audio file format


        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/announcements"

        data = {
            "groupId": group_id,
            "serviceProviderId": service_provider_id,
            "name": name,
            "mediaType": media_type,
        }

        return self._requester.delete(endpoint, data=data)
