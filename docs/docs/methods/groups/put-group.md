# PUT - Group
Updates an existing Group with the specified settings.

### Parameters&#x20;

* group\_id (str): Target Group ID
* service_provider\_id (str): Target Service Provider ID
* default\_domain (str): Default Domain for the Group
* time\_zone (int): Timezone of the Group
* updates\_ (dict): Dictionary of updates to apply to the group.


### Returns

* Dict: Returns the updated Group's information, such as the ID, userCount, Domain and Timezone.

### How To Use:

{% code overflow="wrap" %}
```python
updates = "contact": {"contactName": "test name"}

my_api.groups.post_group{
     "serviceProviderId",
     "groupId",
     "defaultDomain",
     "timeZone",
     updates
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
  "callingLineIdName": "test solutions",
  "callingLineIdPhoneNumber": "+12345678900",
  "callingLineIdDisplayPhoneNumber": 2345678900,
  "timeZone": "America/New_York",
  "timeZoneDisplayName": "(GMT-05:00) (US) Eastern Time",
  "locationDialingCode": 234,
  "contact": {
    "contactName": "test name",
  },
  "serviceProviderId": "ent.test",
  "groupId": "grp.test"
}
```