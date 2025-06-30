# GET - System Services

Fetch all services assigned to the system.

### Returns

*   Dict: A dictionary containing all the services assigned to the system.

### How To Use:

```python
my_api.services.get_system_services()
```

### Example Data Returned (Formatted)

```json
{
    "userServices": [
        {
            "serviceName": "900 Calling",
            "assigned": false
        },
        {
            "serviceName": "Anonymous Call Rejection",
            "assigned": true
        },
        {
            "serviceName": "Authentication",
            "assigned": true
        }
    ],
    "groupServices": [],
    "servicePackServices": []
}
```