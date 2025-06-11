# GET - User Shared Call Appearance

Gets all Shared Call Appearances (SCAs) for a specified user.

### Parameters

* user_id (str): Target user id of user to get SCAs for.

### Returns

* List[Dict]: List of SCA details and settings

### How To Use:

```python
my_api.shared_call_appearance.get_user_shared_call_appearance(user_id="user@example.com")
```

### Example Data Returned (Formatted)

```python
[
    {
        "userId": "user@example.com",
        "isActive": true,
        "allowOrigination": true,
        "allowTermination": true,
        "deviceName": "device1",
        "deviceLevel": "Group",
        "linePort": "line1"
    }
]
```
