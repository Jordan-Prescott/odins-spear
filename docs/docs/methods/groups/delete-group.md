# DELETE - Group
Deletes a Group and all associated users, settings, services and numbers.Returns the specificied Group's settings and information

{% hint style="danger" %}
**Please use with caution!** This action is irreversible unless you have a backup of the group.
{% endhint %}

### Parameters&#x20;

* service_provider\_id (str): Target Service Provider ID
* group\_id (str): Target Group ID

### Returns

* Dict: Returns the deleted Group's information, such as the ID, userCount, Domain and Timezone.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.groups.delete_group{
     "serviceProviderId",
     "groupId"
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
    "contactNumber": "513-123-1234",
    "contactEmail": "testname@domain.com"
  },
  "serviceProviderId": "ent.test",
  "groupId": "grp.test"
}

```