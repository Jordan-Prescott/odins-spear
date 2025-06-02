# PUT - Password

Change password of a specific user.

### Parameters

* user_id (str): Target user to change password
* old_password (str): Current password user logs in with
* new_password (str): Password to change to

### Returns

* None

### How To Use:

```python
my_api.session.put_password(
  "userId",
  "oldPassword",
  "newPassword"
)
```

