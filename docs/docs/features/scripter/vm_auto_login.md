# VM Auto Login

Takes an Enterprise and Group as input and will iterate through all the users in the group and enable Voice Portal Auto Login.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where group is hosted.
* group\_id (str): Group ID where target user list is hosted. 

### Return

* None: This routine has no specified return type

### How To Use:

{% code overflow="wrap" %}
```python
assistant = Scripter(my_api)

assistant.vm_auto_login(
    service_provider_id="serviceProviderId",
    group_id="groupId"
)
```
{% endcode %}
