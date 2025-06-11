# DELETE - User Shared Call Appearance Endpoint

Deletes a Shared Call Appearance (SCA) endpoint for a specified user.

{% hint style="danger" %}
**Please use with caution!** This action is irreversible unless you have a backup of the SCA endpoint.
{% endhint %}

### Parameters

* device_level (str): Target device level of SCA endpoint to delete. (e.g., "Group", "Service Provider")
* device_name (str): Name of the device
* user_id (str): Target user id
* line_port (str): Target line port of SCA endpoint to delete.

### Returns

* Dict: Deleted SCA endpoint details.

### How To Use:

```python
my_api.shared_call_appearance.delete_user_shared_call_appearance_endpoint(
    device_level="Group",
    device_name="device1",
    user_id="user@example.com",
    line_port="line1"
)
```

### Example Data Returned (Formatted)

```python
{
    'userId': 'user@example.com',
    'deviceName': 'device1',
    'deviceLevel': 'Group',
    'linePort': 'line1',
    'isActive': True,
    'allowOrigination': True,
    'allowTermination': True
}
```
