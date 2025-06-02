# PUT - User Authentication User

Changes the authentication password of a single userto use this method. 

### Parameters&#x20;

* username (str): Username of target user
* user_id (str): User ID of target user
* old_password (str): Old password (current)
* new_password (str): Password to change to

### Returns

* None: This method does not return any specific value. 

### How To Use:

{% code overflow="wrap" %}
```python
my_api.authentication.put_user_authentication_service(
    "username",
    "userId",
    "oldPassword",
    "newPassword"
)
```
{% endcode %}
