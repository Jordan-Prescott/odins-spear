# GET - Group Schedules

Retrieves the Business Schedules for the specified group.

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider ID where group is hosted.
* group\_id (str): Target Group ID with schedules.

### Returns

* List: List of all the groups schedules, including Name, Type and Level.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.schedules.get_group_schedules(
    "serviceProviderID",
    "groupID"
)
```
{% endcode %}

### Example Response (Formatted)

```json
[
  {
    "name": "Spring",
    "type": "Time",
    "level": "Group",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  },
  {
    "name": "Tes",
    "type": "Holiday",
    "level": "Group",
    "serviceProviderId": "serviceProviderID",
    "groupId": "groupID"
  }
]
```
