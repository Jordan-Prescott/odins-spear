# PUT - Password

Change the password of the current user (yourself)

### Parameters

* old_password (str): Current password user logs in with
* new_password (str): Password to change to

### Returns

* None

### How To Use:

```python
my_api.session.put_my_password(
  "oldPassword",
  "newPassword"
)
```

