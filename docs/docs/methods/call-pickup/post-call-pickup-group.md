# POST - Call Pickup Group

Creates a new pickup group for the specified group

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): The Target Group ID the user is apart of.
* pickup_group_name (str): The Target Pickup Group Name

### Returns

* None

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_pickup.post_call_pickup_group
(
    "my_service_provider_id", 
    "my_group_id",
    "pick_up_group_name"
)
```
{% endcode %}
