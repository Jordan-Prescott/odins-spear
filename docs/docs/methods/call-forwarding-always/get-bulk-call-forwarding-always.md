# GET - Bulk Call Forward Always

Retrieves the Forwarding Always status for all users within a specified group

### Parameters&#x20;

* service\_provider_id (str): Target Service Provider where group is hosted
* group\_id (str): Target Group ID

### Returns

* List: Forwarding enabled status, the Number to be Forwarded to, and User information.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import API

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.call_forwarding_always.get_bulk_call_forwarding_always{
    "serviceProviderId",
    "groupId"
}

```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "service": {
      "assigned": true,
      "serviceName": "Call Forwarding Always"
    },
    "user": {
      "userId": "9709580001@domain.com",
      "lastName": "Mock1",
      "firstName": "Mock1",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580001",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "Mock1",
      "hiraganaFirstName": "Mock1",
      "inTrunkGroup": false,
      "extension": "0001",
      "domain": "domain.com"
    },
    "data": {
      "isActive": false,
      "isRingSplashActive": false,
      "userId": "9709580001@domain.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Call Forwarding Always"
    },
    "user": {
      "userId": "9709580002@domain.com",
      "lastName": "User2last",
      "firstName": "User2first",
      "department": "test Mock Dept (test.mock.grp1)",
      "phoneNumber": "+1-9709580002",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "User2last",
      "hiraganaFirstName": "User2first",
      "inTrunkGroup": false,
      "extension": "0002",
      "domain": "domain.com"
    },
    "data": {
      "isActive": false,
      "isRingSplashActive": false,
      "userId": "9709580002@domain.com"
    }
  }
]

```