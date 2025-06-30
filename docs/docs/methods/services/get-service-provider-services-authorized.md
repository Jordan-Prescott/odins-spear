# GET - Service Provider Services Authorized

Fetch all services within a service provider that are authorized alongside their quantity and limit.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target

### Returns

*   Dict: A dictionary with the service names of all authorized services alongside their quantity and limit.

### How To Use:

```python
my_api.services.get_service_provider_services_authorized(
    service_provider_id="service_provider_id"
)
```

### Example Data Returned (Formatted)

```json
{
    "serviceProviderId": "service_provider_id",
    "userServices": [
        {
            "serviceName": "Alternate Numbers",
            "authorized": true,
            "assigned": false,
            "limited": "Unlimited",
            "quantity": -1,
            "allocated": -1,
            "licensed": true,
            "servicePackAllocation": 0,
            "userAssignable": true,
            "servicePackAssignable": true,
            "tags": [],
            "alias": "Alternate Numbers"
        },
        {
            "serviceName": "Anonymous Call Rejection",
            "authorized": true,
            "assigned": false,
            "limited": "Unlimited",
            "quantity": -1,
            "allocated": -1,
            "licensed": true,
            "servicePackAllocation": "Unlimited",
            "userAssignable": true,
            "servicePackAssignable": true,
            "tags": [],
            "alias": "Anonymous Call Rejection"
        },
        {
            "serviceName": "Authentication",
            "authorized": true,
            "assigned": false,
            "limited": "Unlimited",
            "quantity": -1,
            "allocated": -1,
            "licensed": true,
            "servicePackAllocation": "Unlimited",
            "userAssignable": true,
            "servicePackAssignable": true,
            "tags": [],
            "alias": "Authentication"
        }
    ]
}
```