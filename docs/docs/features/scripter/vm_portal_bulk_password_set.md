# VM Portal Bulk Password Set

This takes an Enterprise, Group and passcode as input.
Will iterate through all the users in the group to set to the passcode to whatever was specified (usually 4-6 digits).

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where group is hosted.
* group\_id (str): Group ID where target user list is hosted. 
* new\_password (str): Voice Messaging passcode for user assignment.

### Return

* None: This routine has no specified return type

### How To Use:

{% code overflow="wrap" %}
```python
assistant = Scripter(my_api)

assistant.vm_portal_bulk_password_set(
    service_provider_id="serviceProviderId",
    group_id="groupId",
    new_password="test123"
)
```
{% endcode %}
