# GET - Call Pickup Group 

Retrieves Pickup Group information for the specified group.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): The Target Group ID the user is apart of.
* pickup_group_name (str): The Target Pickup Group Name*

### Returns

* Dict: Specified users pickup group, and the users within that group.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_pickup.get_call_pickup_group(
    "my_service_provider_id", 
    "my_group_id",
    "pickup_group_name"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```python
{
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1",
  "name": "Call Pickup 1",
  "users": []
}
```

