# GET - Groups

Returns the specificied Service Provider's Groups

### Parameters&#x20;

* service_provider\_id (str): Target Service Provider ID

### Returns

* List: List of groups and their Names, alongside groupID's and userLimits.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.groups.get_groups{
    "serviceProviderId"
}

```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "groupId": "otest.mock.grp1",
    "groupName": "test Mock Group 1",
    "userLimit": 25,
    "serviceProviderId": "test.mock.ent1"
  },
  {
    "groupId": "otest.mock.grp5",
    "groupName": "Group 5",
    "userLimit": 25,
    "serviceProviderId": "test.mock.ent1"
  }
]

```