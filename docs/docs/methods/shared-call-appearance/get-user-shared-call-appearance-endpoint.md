# GET - User Shared Call Appearance Endpoint

Gets a specific Shared Call Appearance (SCA) endpoint for a user.

### Parameters

* device_level (str): Level of device (e.g., "Group", "Service Provider")
* device_name (str): Name of the device
* user_id (str): Target user id
* line_port (str): Line port identifier

### Returns

* Dict: Endpoint details including active status, permissions, and device information

### How To Use:

```python
my_api.shared_call_appearance.get_user_shared_call_appearance_endpoint(
    device_level="Group",
    device_name="device1",
    user_id="user@example.com",
    line_port="line1"
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
