# GET - User Service Instance Search

Search for service instances for a user, group or service provider.

### Parameters

*   user\_id (str): ID of the target user
*   service\_provider\_id (str, optional): Service provider ID of the target
*   group\_id (str, optional): Group ID of the target
*   filter (str, optional): Filter criteria, supported filters below. Defaults to None.
*   filter\_type (str, optional): Options: equals, startsWith, endsWith, contains or endsWith. Defaults to None.
*   filter\_value (str, optional): Value filtering on e.g. firstName. Defaults to None.
*   limit (int, optional): Limits the amount of values API returns. Defaults to None.
*   extended (bool, optional): If True, returns the full user profile. Defaults to False.

### Returns

*   Dict: A dictionary containing all the service instances for the user, group or service provider.

### How To Use:

```python
my_api.services.get_user_service_instance_search(
    user_id="user_id",
    service_provider_id="service_provider_id",
    group_id="group_id",
    filter="firstName",
    filter_type="startsWith",
    filter_value="J",
    limit=10,
    extended=True
)
```

### Example Data Returned (Formatted)

```json
[
    {
        "serviceType": "User",
        "name": "John Doe",
        "phoneNumber": "1234567890",
        "extension": "1001",
        "department": "Sales",
        "groupId": "sales_group",
        "userId": "john.doe@example.com",
        "serviceProviderId": "example_corp",
        "userIdShort": "john.doe@example.com",
        "domain": "example.com"
    },
    {
        "serviceType": "User",
        "name": "Jane Doe",
        "phoneNumber": "0987654321",
        "extension": "1002",
        "department": "Sales",
        "groupId": "sales_group",
        "userId": "jane.doe@example.com",
        "serviceProviderId": "example_corp",
        "userIdShort": "jane.doe@example.com",
        "domain": "example.com"
    }
]
```