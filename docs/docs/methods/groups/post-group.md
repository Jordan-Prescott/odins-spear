# POST - Group
Creates a new group.

### Parameters&#x20;

* default\_domain (str): Default Domain for the Group
* user\_limit (int): User Limit for the Group
* group\_name (str): Name of the Group
* group\_id (str): Target Group ID
* service_provider\_id (str): Target Service Provider ID

### Returns

* Dict: Returns the newly created Group's information, such as the ID, userCount, Domain and Timezone.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.groups.post_group{
     "serviceProviderId",
     "groupId",
     "groupName",
     200,
     "DefaultDomain"
}


```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "defaultDomain": "domain.com",
  "userLimit": 25,
  "userCount": 8,
  "groupName": "grp.test",
  "timeZone": "America/New_York",
  "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
  "serviceProviderId": "ent.test",
  "groupId": "grp.test"
}

```