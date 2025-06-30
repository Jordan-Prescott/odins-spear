# GET - Service Provider Services

Fetch all services within a service provider.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target
*   onlyLicensed (bool, optional): Only fetch licensed services. Defaults to False.
*   onlyAuthorised (bool, optional): Only fetch authorised services. Defaults to False.

### Returns

*   Dict: A dictionary containing all the services within the service provider alongside their settings.

### How To Use:

```python
my_api.services.get_service_provider_services(
    service_provider_id="your_service_provider_id",
    onlyLicensed=False,
    onlyAuthorised=False
)
```

### Example Data Returned (Formatted)

```json
{
    "userServices": [
        {
            "serviceName": "Anonymous Call Rejection",
            "authorized": true,
            "assigned": true,
            "limited": "Unlimited",
            "quantity": -1,
            "usage": 0,
            "licensed": true,
            "allowed": -1,
            "userAssignable": true,
            "groupServiceAssignable": true,
            "tags": [],
            "alias": "Anonymous Call Rejection"
        },
        {
            "serviceName": "Authentication",
            "authorized": true,
            "assigned": true,
            "limited": "Unlimited",
            "quantity": -1,
            "usage": 0,
            "licensed": true,
            "allowed": -1,
            "userAssignable": true,
            "groupServiceAssignable": true,
            "tags": [],
            "alias": "Authentication"
        }
    ]
}
```