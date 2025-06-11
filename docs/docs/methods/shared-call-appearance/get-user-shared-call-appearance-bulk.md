# GET - User Shared Call Appearance Bulk

Gets all Shared Call Appearances (SCAs) within a specified group.

### Parameters

* service_provider_id (str): Service Provider/ Enterprise ID where Group is hosted.
* group_id (str): Target Group ID where users are located.

### Returns

* List[Dict]: List of SCA details for the group

### How To Use:

```python
my_api.shared_call_appearance.get_user_shared_call_appearance_bulk(
    service_provider_id="provider1",
    group_id="group1"
)
```

### Example Data Returned (Formatted)

```python
[
    {
        "userId": "user1@example.com",
        "isActive": true,
        "allowOrigination": true,
        "allowTermination": true,
        "deviceName": "device1",
        "deviceLevel": "Group",
        "linePort": "line1"
    },
    {
        "userId": "user2@example.com",
        "isActive": true,
        "allowOrigination": true,
        "allowTermination": true,
        "deviceName": "device2",
        "deviceLevel": "Group",
        "linePort": "line2"
    }
]
```
