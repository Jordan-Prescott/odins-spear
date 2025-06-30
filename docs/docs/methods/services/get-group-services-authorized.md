# GET - Group Services Authorized

Fetch all services authorized within a group.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target
*   group\_id (str): Group ID of the target

### Returns

*   Dict: A dictionary with the service names of all authorized services within the group.

### How To Use:

```python
my_api.services.get_group_services_authorized(
    service_provider_id="service_provider_id",
    group_id="group_id"
)
```

### Example Data Returned (Formatted)

```json
{
    "userServices": [
        {
            "serviceName": "Anonymous Call Rejection",
            "authorized": false
        },
        {
            "serviceName": "Authentication",
            "authorized": false
        }
    ],
    "groupServices": [],
    "servicePackServices": []
}
```