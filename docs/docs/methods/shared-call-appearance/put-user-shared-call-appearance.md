# PUT - User Shared Call Appearance

Updates Shared Call Appearance (SCA) settings for a specified user.

### Parameters

* user_id (str): Target user id to update SCA settings for
* settings (dict): Dictionary containing SCA settings to update

### Returns

* Dict: Updated SCA settings

### How To Use:

```python
my_api.shared_call_appearance.put_user_shared_call_appearance(
    user_id="user@example.com",
    settings={
        "isActive": True,
        "allowOrigination": True,
        "allowTermination": True
    }
)
```

### Example Data Returned (Formatted)

```python
{
    "userId": "user@example.com",
    "isActive": true,
    "allowOrigination": true,
    "allowTermination": true,
    "deviceName": "device1",
    "deviceLevel": "Group",
    "linePort": "line1"
}
```
