from .base_endpoint import BaseEndpoint
from ..utils.formatters import format_filter_value


class Users(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET
    def get_users(
        self,
        service_provider_id: str = None,
        group_id: str = None,
        filter: str = None,
        filter_type: str = None,
        filter_value: str = None,
        limit: int = None,
        extended=False,
    ):
        """
        Returns list of users depending on filter criteria.

        Args:
            servive_provider_id (str, optional): Service or Enterprise ID,
            top level object. Defaults to None.
            group_id (str, optional): Group ID where user is hosted. Defaults to None.
            filter (str, optional): Filter criteria, supported filters below. Defaults to None.
            filter_type (str, optional): Options: equals, startsWith, endsWith, contains or endsWith. Defaults to None.
            filter_value (str, optional): Value filtering on e.g. firstName. Defaults to None.
            limit (int, optional): Limits the amount of values API returns. Defaults to None.

        Returns:
            dict: List of users.

        #Supported Filters
        macAddress: search by device
        lastName: filter by lastName
        firstName: filter by firstName
        dn: filter by dn
        emailAddress: filter by emailAddress
        userId: filter by userId
        extension: filter by extension

        ####Examples
        Get all users in Enterprise ent1
        GET /api/v2/users?serviceProviderId=ent1

        Get all users in Group grp1
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1

        Get up to 10 users in the system with a last name that contains smith
        GET /api/v2/users?lastName=*smith*&limit=10

        Get the users in grp1 that have a phone number that starts with 513333
        GET /api/v2/users?serviceProviderId=ent1&groupId=grp1&dn=513333*
        """

        endpoint = "/users?"

        params = {}

        if service_provider_id:
            params["serviceProviderId"] = service_provider_id
            if group_id:
                params["groupId"] = group_id
        if filter:
            params[filter] = format_filter_value(
                filter_criteria=filter,
                filter_type=filter_type,
                filter_value=filter_value,
            )
        if limit:
            params["limit"] = limit
        if extended:
            params["extended"] = True

        return self._requester.get(endpoint, params=params)

    def get_user_password(self, user_id: str):
        """Returns login and password expiry details of target user.

        Args:
            user_id (str):  Target user ID.

        Returns:
            dict: Details of user
        """

        endpoint = "/users/password"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_by_id(self, user_id: str):
        """Returns extensive details of a single user including alias, enpoint device, and more common
        details like first and last name.

        Args:
            user_id (str): Target user ID of the user you would like to review.

        Returns:
            Dict: Python dictionary of the users details
        """

        endpoint = "/users"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_audit(self, user_id: str):
        """Returns a detailed audit of user spanning from generic details to call policies and features assigned.

        Args:
            user_id (str): Target user ID to audit

        Returns:
            Dict: Audit details of user
        """

        endpoint = "/users/audit"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_login_info(self, user_id: str):
        """Returns detailed log in information such as password expirery

        Args:
            user_id (str): Target user ID

        Returns:
            Dict: Login details of target user
        """

        endpoint = "/users/login-info"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_portal_passcode(self, user_id: str):
        """Returns portal passcode details such as expirery

        Args:
            user_id (str): Target user ID

        Returns:
            Dict: Portal passcode details of target user
        """

        endpoint = "/users/portal-passcode"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_user_audit(self, service_provider_id: str, group_id: str):
        """AI is creating summary for get_group_user_audit

        Args:
            service_provider_id (str): Target Service Provider ID
            group_id (str): Target Group ID with users

        Returns:
            Dict: Audit of users in specified group
        """

        endpoint = "/groups/users/audit"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    # POST
    def post_user(
        self,
        service_provider_id: str,
        group_id: str,
        user_id: str,
        first_name: str,
        last_name: str,
        extension: str,
        web_auth_password: str,
        payload: dict = {},
    ):
        """
            Creates a new user in the specified group with the configuration defined in the payload.

        Args:
            service_provider_id (str): Service provider ID where Group is loctaed.
            group_id (str): Group ID where new user will be built.
            user_id (str): Complete User ID including group domain of new user.
            first_name (str): First name of new user.
            last_name (str): Last name of new user.
            extension (str): Extension number of new user.
            web_auth_password (str): Web authentication password. Note get.password_generate() can be used to get this.
            payload (dict, optional): User configuration.

        Returns:
            Dict: New user entity.
        """

        endpoint = "/users"

        payload["callingLineIdFirstName"] = (
            first_name
            if not payload.get("callingLineIdFirstName")
            else payload["callingLineIdFirstName"]
        )
        payload["callingLineIdLastName"] = (
            last_name
            if not payload.get("callingLineIdLastName")
            else payload["callingLineIdLastName"]
        )

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["userId"] = user_id
        payload["firstName"] = first_name
        payload["lastName"] = last_name
        payload["extension"] = extension
        payload["password"] = web_auth_password

        return self._requester.post(endpoint, data=payload)

    def post_user_reset(
        self,
        user_id: str,
        remove_from_group_services: bool,
        remove_call_records: bool,
        remove_alternate_user_ids: bool,
        remove_webex_person: bool,
        cycle_service_packs: bool,
        reset_password_passcode: bool,
    ):
        """Resets/ removes user across areas such as resetting password and cycling feature pack

        Note: Not fully understood, use with caution

        Args:
            user_id (str): Users Original Identifier
            remove_from_group_services (bool): Remove From Group Services
            remove_call_records (bool): Remove Call Record Instances
            remove_alternate_user_ids (bool): Remove Alternate User Identifiers
            remove_webex_person (bool): Remove Webex Entry
            cycle_service_packs (bool): Shift Service Packs
            reset_password_passcode (bool): Reset Password Forcing A New Login And Password
        Returns:
            None: This function doesn't return any details
        """

        endpoint = "/users/reset"

        payload = {
            "userId": user_id,
            "removeFromGroupServices": remove_from_group_services,
            "removeCallRecords": remove_call_records,
            "removeAlternateUserIds": remove_alternate_user_ids,
            "removeWebexPerson": remove_webex_person,
            "cycleServicePacks": cycle_service_packs,
            "resetPasswordPasscode": reset_password_passcode,
        }

        return self._requester.post(endpoint, data=payload)

    # PUT
    def put_users_bulk(self, users: list, updates: dict):
        """
        Updates specified list of User's options, such as extension, name and etc.

        Note: Available options to change can be seen through: get.user_by_id()

        Args:
            users (list): List of specified User IDs to update
            updates (dict): The updates to be applied to the list of Users e.g {"extension":"9999"}

        Returns:
            Dict: Returns the changes made including the list of User IDs and updates.
        """
        endpoint = "/users/bulk"

        target_users = [{"userId": user} for user in users]

        data = {"users": target_users, "data": updates}

        return self._requester.put(endpoint, data=data)

    def put_user(
        self, service_provider_id: str, group_id: str, user_id: str, updates: dict
    ):
        """
        Updates specified User's options, such as extension, name and etc.

        Note: Available options to change can be seen through: get.user_by_id()

        Args:
            service_provider_id (str):
            updates (dict): The updates to be applied Target Service Provider where group is located
            group_id (str): Target Group ID where user is located
            user_id (str): Target User IDto the list of Users e.g {"extension":"9999"}

        Returns:
            Dict: Returns the changes made including User ID and updates.
        """
        endpoint = "/users"

        updates["serviceProviderId"] = service_provider_id
        updates["groupId"] = group_id
        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_portal_passcode(self, user_id: str, new_passcode: str):
        """Updates the specified User's portal passcode.

        Args:
            user_id (str): User ID of the target user you would like to change the portal passcode for.
            new_passcode (int): New portal passcode to set for the target user.

        Raises:
            AOInvalidCode: If code is less than 4 or higher than 6.

        Returns:
            None: This method does not return any specific value.
        """

        if len(new_passcode) < 4 or len(new_passcode) > 6:
            from ..exceptions import OSInvalidCode

            raise OSInvalidCode

        endpoint = "/users/portal-passcode"

        data = {"userId": user_id, "newPasscode": new_passcode}

        return self._requester.put(endpoint, data=data)

    def put_user_sip_contacts(
        self, service_provider_id: str, group_id: str, user_id: str, sip_contacts: list
    ):
        """Adds a list of SIP Contacts to a specified user. If adding only 1 still include in a list.

        Note: 5 is the max amount of sip contats a user can have

        Args:
            service_provider_id (str): Service Provider ID which hosts Group
            group_id (str): Group ID which hosts User
            user_id (str): Target User ID
            sip_contact (list): List of sip contact details to add. 5 max.

        Returns:
            None: This function doesn't return any details
        """

        if sip_contacts.len() > 5:
            from ..exceptions import OSValueExceeded

            raise OSValueExceeded

        endpoint = "/users"

        data = {
            "serviceProviderId": service_provider_id,
            "groupId": group_id,
            "userId": user_id,
            "contacts": [{"sipContact": contact} for contact in sip_contacts],
        }

        return self._requester.put(endpoint, data=data)

    def put_user_id(self, current_user_id: str, new_user_id: str):
        """Updates a single user ID to a new user ID.

        Args:
            current_user_id (str): Existing User ID
            new_user_id (str): User ID to change to

        Returns:
            None: This function doesn't return any details
        """

        endpoint = "/users/user-id"

        data = {"userId": current_user_id, "newUserId": new_user_id}

        return self._requester.put(endpoint, data=data)

    def put_group_id_update(self, user_id: str, group_id: str, evaluate: bool = False):
        """Updates the Group the user belongs to.

        Note: Not fully understood - use with caution

        Args:
            user_id (str): Target user ID
            group_id (str): Target grouo ID to migrate to
            evaluate (bool, optional): True or False. Defaults to False.

        Returns:
            None
        """

        endpoint = "/users/group-id"

        data = {
            "userId": user_id,
            "newGroupId": group_id,
            "evaluateOnly": evaluate,
        }

        return self._requester.put(endpoint, data=data)

    # DELETE

    def delete_user(self, user_id: str):
        """Removes a single user form the platform

        Args:
            user_id (str): Target user ID

        Returns:
            None
        """

        endpoint = "/users"

        params = {"userId": user_id}

        return self._requester.delete(endpoint, params=params)
