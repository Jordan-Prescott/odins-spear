# GET - User Authentication Service

Returns authentication details of authorised users. 

### Parameters&#x20;

* user\_id (str): Target user ID to reset the SIP authentication password.

### Returns

* Dict: Autnentication details of target user

### How To Use:

{% code overflow="wrap" %}
```python
my_api.authentication.put_user_authentication_service(
    "userId",
)
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```python
{
  "userName": 9709580001,
  "userId": "9709580001@microv-works.com",
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1",
  "isEnterprise": true
}
```