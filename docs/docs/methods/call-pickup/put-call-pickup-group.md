# PUT - Call Pickup Group

Updates the name of a pickup group for the specified group

Note: When updating users include all users in the group, not just the ones being added.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): The Target Group ID the user is apart of.
* pickup_group_name (str): The Target Pickup Group Name
* new_group_name (str): The new name of the pickup group
* users (list[str]): The list of user IDs to add to the pickup group

### Raises 
    ValueError: If no users or new_group_name are provided

### Returns

* None

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_pickup.put_call_pickup_group
(
    "my_service_provider_id", 
    "my_group_id",
    "pick_up_group_name",
    "new_group_name",
    users = [
      "userId",
      "userId",
      "userId"
    ]
)
```
{% endcode %}
