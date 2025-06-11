# PUT - User Shared Call Appearance Endpoint

Updates Shared Call Appearance (SCA) endpoint settings for a user.

### Parameters

* user_id (str): Target user id
* line_port (str): Line port identifier
* device_name (str): Name of the device
* device_level (str): Level of device (e.g., "Group", "Service Provider")
* is_active (bool): Whether the endpoint is active
* allow_origination (bool): Whether to allow call origination
* allow_termination (bool): Whether to allow call termination

### Returns

* Dict: Updated endpoint settings

### How To Use:

```python
my_api.shared_call_appearance.put_user_shared_call_appearance_endpoint(
    user_id="user@example.com",
    line_port="line1",
    device_name="device1",
    device_level="Group",
    is_active=True,
    allow_origination=True,
    allow_termination=True
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
