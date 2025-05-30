# GET - User Password

Returns login and password expiry details of target user.

### Parameters&#x20;

* user\_id (str): Target user ID.

### Returns

* Dict: Details of user

### How To Use:

```python
my_api.users.get_user_password(
    "user_ID"
)
```

### Example Data Returned (Formatted)

```python
{
  "isLoginDisabled": false,
  "expirationDays": "-2147483648",
  "userId": "5132298513@example21.com"
}
```
