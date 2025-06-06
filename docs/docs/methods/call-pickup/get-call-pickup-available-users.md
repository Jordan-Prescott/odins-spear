# GET - Call Pickup Available Users

Retrieves available users to assign to a pick up group for the specified group.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): The Target Group ID the user is apart of.
* pickup_group_name (str): The Target Pickup Group Name*

### Returns

* Dict: Available users to assign to a pick up group for the specified group.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_pickup.get_call_pickup_available_users(
    "my_service_provider_id", 
    "my_group_id"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```python
[
  {
    "userId": "9709580001",
    "lastName": "User1last",
    "firstName": "User1first",
    "hiraganaLastName": "User1last",
    "hiraganaFirstName": "User1first",
    "phoneNumber": "+1-9709580001",
    "extension": "0001",
    "department": "Odin Mock Dept (odin.mock.grp1)",
    "emailAddress": None
  },
  {
    "userId": "9709580002",
    "lastName": "User2last",
    "firstName": "User2first",
    "hiraganaLastName": "User2last",
    "hiraganaFirstName": "User2first",
    "phoneNumber": "+1-9709580002",
    "extension": "0002",
    "department": "Odin Mock Dept (odin.mock.grp1)",
    "emailAddress": None
  },
  {
    "userId": "9709580003",
    "lastName": "User3last",
    "firstName": "User3first",
    "hiraganaLastName": "User3last",
    "hiraganaFirstName": "User3first",
    "phoneNumber": "+1-9709580003",
    "extension": "0003",
    "department": "Odin Mock Dept (odin.mock.grp1)",
    "emailAddress": None
  },
  {
    "userId": "9709580004",
    "lastName": "User4last",
    "firstName": "User4first",
    "hiraganaLastName": "User4last",
    "hiraganaFirstName": "User4first",
    "phoneNumber": "+1-9709580004",
    "extension": "0004",
    "department": "Odin Mock Dept (odin.mock.grp1)",
    "emailAddress": None
  },
  {
    "userId": "9709580005",
    "lastName": "User5last",
    "firstName": "User5first",
    "hiraganaLastName": "User5last",
    "hiraganaFirstName": "User5first",
    "phoneNumber": "+1-9709580005",
    "extension": "0005",
    "department": "Odin Mock Dept (odin.mock.grp1)",
    "emailAddress": None
  }
]
```

