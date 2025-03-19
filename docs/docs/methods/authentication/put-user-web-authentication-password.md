# PUT - User Web Authentication Password

Set new Web Authentication password for a single user.

### Parameters&#x20;

* user\_id (str): Target user ID to reset the web authentication password.&#x20;
* new\_password (str): New web authentication password to apply to new user.

### Returns

* None: This method does not return any specific value.

### How To Use:

The below code will set the AA to deactivated.

{% code overflow="wrap" %}
```python
my_api.authentication.put_user_web_authentication_password(
    "userID@domain.com",
    "newPassword"
)
```
{% endcode %}

