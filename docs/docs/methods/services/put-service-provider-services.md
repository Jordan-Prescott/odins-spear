# PUT - Service Provider Services

Update the services assigned to a service provider.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target
*   services (list): List of services to be applied to service provider.
*   assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.
*   authorized (bool, optional): Authorize (True) or unauthorize(False). Defaults to True.
*   quantity (int, optional): Quantity of services to be applied to service provider. Defaults to None.
*   unlimited (bool, optional): If True, quantity is unlimited. Defaults to False.
*   allocated (int, optional): Allocated quantity of services to be applied to service provider. Defaults to None.

### Returns

*   Dict: Service provider services assigned to the service provider.

### How To Use:

```python
my_api.services.put_service_provider_services(
    service_provider_id="service_provider_id",
    services=["Anonymous Call Rejection", "Authentication"],
    assigned=True,
    authorized=True,
    quantity=100,
    unlimited=False,
    allocated=50
)
```

### Example Data Returned (Formatted) 

```json
{
    "serviceProviderId": "service_provider_id",
    "userServices": [
        {
            "serviceName": "3G/4G Continuity",
            "authorized": false,
            "assigned": false,
            "limited": "Unlimited",
            "quantity": -1,
            "allocated": 0,
            "licensed": false,
            "servicePackAllocation": 0,
            "userAssignable": true,
            "servicePackAssignable": true,
            "tags": [],
            "alias": "3G/4G Continuity"
        },
        {
            "serviceName": "Advice Of Charge",
            "authorized": false,
            "assigned": false,
            "limited": "Unlimited",
            "quantity": -1,
            "allocated": 0,
            "licensed": false,
            "servicePackAllocation": 0,
            "userAssignable": true,
            "servicePackAssignable": true,
            "tags": [],
            "alias": "Advice Of Charge"
        }
    ]
}
```