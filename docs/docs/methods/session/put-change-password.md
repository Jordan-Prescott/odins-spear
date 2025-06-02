# PUT - Change Password 

Set new Web Authentication password for a single user.

### Parameters

* user_id (str): Target user ID to reset the web authentication password.
* new_password (str): New web authentication password to apply to new user.

### Returns

* None

### How To Use:

```python
my_api.session.put_change_password(
  "userId",
  "newPassword"
)
```

