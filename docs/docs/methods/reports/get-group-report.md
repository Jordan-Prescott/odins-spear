# GET - Group Report

Retrieves a detailed report of every user in a group including services and service packs assigned.

### Parameters&#x20;

* service_provider_id (str): Service Provider/ Enterprise ID where Group is hosted.
* group_id (str): Target Group ID

### Returns

* dict: Detailed report of users within a group including services and service packs.

### How To Use:

The following code snippet demonstrates how to fetch a list of all Users:

{% code overflow="wrap" %}
```python
my_api.reports.get_user_report("ServiceProvider", "Group")
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
[
    {
            "userId": "user1001@example.com",
            "phoneNumberActivated": false,
            "inTrunkGroup": false,
            "serviceProviderId": "ExampleSP",
            "groupId": "ExampleGroup",
            "lastName": "Doe",
            "firstName": "John",
            "callingLineIdLastName": "Doe",
            "callingLineIdFirstName": "John",
            "hiraganaLastName": "Doe",
            "hiraganaFirstName": "John",
            "extension": "1001",
            "language": "English",
            "timeZone": "UTC",
            "timeZoneDisplayName": "(GMT) UTC",
            "defaultAlias": "user1001@example.com",
            "accessDeviceEndpoint": {
                "accessDevice": {
                    "deviceType": "Yealink T43U",
                    "protocol": "SIP 2.0",
                    "numberOfPorts": {
                        "quantity": "12"
                    },
                    "numberOfAssignedPorts": 1,
                    "status": "Online",
                    "configurationMode": "Default",
                    "transportProtocol": "UDP",
                    "useCustomUserNamePassword": false,
                    "deviceName": "Device-ABC-123",
                    "serviceProviderId": "ExampleSP",
                    "groupId": "ExampleGroup",
                    "macAddress": "AA:BB:CC:11:22:33",
                    "deviceLevel": "Group",
                    "accessDeviceCredentials": {
                        "userName": null
                    },
                    "tags": [],
                    "relatedServices": []
                },
                "linePort": "user1001@example.com",
                "staticRegistrationCapable": "false",
                "useDomain": "true",
                "supportVisualDeviceManagement": "false",
                "contacts": []
            },
            "countryCode": "1",
            "allowVideo": true,
            "callingLineIdPhoneNumber": "",
            "phoneNumber": "",
            "domain": "example.com",
            "endpointType": "accessDeviceEndpoint",
            "aliases": [
                "alias1@example.com",
                "alias2@example.com"
            ],
            "trunkAddressing": {
                "trunkGroupDeviceEndpoint": {
                    "contacts": []
                }
            },
            "department": {
                "serviceProviderId": "ExampleSP",
                "groupId": "ExampleGroup",
                "name": "Sales"
            },
            "emailAddress": "john.doe@example.com",
            "nationalPrefix": "",
            "isEnterprise": true,
            "passwordExpiresDays": "-2147483648",
            "premiumServices": [],
            "userServices": [],
            "servicePacks": [
                "StandardPack"
            ],
            "userLinePorts": [],
            "userAgents": []
        },
        {
            "userId": "trunkuser2001@example.com",
            "phoneNumberActivated": false,
            "inTrunkGroup": true,
            "serviceProviderId": "ExampleSP",
            "groupId": "ExampleGroup",
            "lastName": "Smith",
            "firstName": "Jane",
            "callingLineIdLastName": "Smith",
            "callingLineIdFirstName": "Jane",
            "hiraganaLastName": "Smith",
            "hiraganaFirstName": "Jane",
            "extension": "2001",
            "language": "English",
            "timeZone": "UTC",
            "timeZoneDisplayName": "(GMT) UTC",
            "defaultAlias": "trunkuser2001@example.com",
            "trunkAddressing": {
                "trunkGroupDeviceEndpoint": {
                    "name": "ExampleTrunkGroup",
                    "linePort": "trunkuser2001@example.com",
                    "staticRegistrationCapable": "false",
                    "useDomain": "true",
                    "isPilotUser": "true",
                    "contacts": []
                }
            },
            "countryCode": "1",
            "allowVideo": true,
            "callingLineIdPhoneNumber": "",
            "phoneNumber": "",
            "domain": "example.com",
            "endpointType": "trunkAddressing",
            "aliases": [],
            "accessDeviceEndpoint": {
                "contacts": []
            },
            "department": {
                "serviceProviderId": "ExampleSP",
                "groupId": "ExampleGroup",
                "name": "Engineering"
            },
            "emailAddress": "jane.smith@example.com",
            "nationalPrefix": "",
            "isEnterprise": true,
            "passwordExpiresDays": "-2147483648",
            "premiumServices": [],
            "userServices": [],
            "servicePacks": [
                "StandardPack"
            ],
            "userLinePorts": [],
            "userAgents": []
        },
        {
            "userId": "trunkuser2002@example.com",
            "phoneNumberActivated": false,
            "inTrunkGroup": true,
            "serviceProviderId": "ExampleSP",
            "groupId": "ExampleGroup",
            "lastName": "Jones",
            "firstName": "Peter",
            "callingLineIdLastName": "Jones",
            "callingLineIdFirstName": "Peter",
            "hiraganaLastName": "Jones",
            "hiraganaFirstName": "Peter",
            "extension": "2002",
            "language": "English",
            "timeZone": "UTC",
            "timeZoneDisplayName": "(GMT) UTC",
            "defaultAlias": "trunkuser2002@example.com",
            "trunkAddressing": {
                "trunkGroupDeviceEndpoint": {
                    "name": "ExampleTrunkGroup",
                    "linePort": "trunkuser2002@example.com",
                    "staticRegistrationCapable": "false",
                    "useDomain": "true",
                    "isPilotUser": "false",
                    "contacts": []
                }
            },
            "countryCode": "1",
            "allowVideo": true,
            "callingLineIdPhoneNumber": "",
            "phoneNumber": "",
            "domain": "example.com",
            "endpointType": "trunkAddressing",
            "aliases": [],
            "accessDeviceEndpoint": {
                "contacts": []
            },
            "department": {
                "serviceProviderId": "ExampleSP",
                "groupId": "ExampleGroup",
                "name": "Support"
            },
            "emailAddress": "peter.jones@example.com",
            "nationalPrefix": "",
            "isEnterprise": true,
            "passwordExpiresDays": "-2147483648",
            "premiumServices": [],
            "userServices": [],
            "servicePacks": [
                "StandardPack"
            ],
            "userLinePorts": [],
            "userAgents": []
    }
]
```