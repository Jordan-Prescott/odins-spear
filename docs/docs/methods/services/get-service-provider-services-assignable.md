# GET - Service Provider Services Assignable

Fetch all services within a service provider that are assignable.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target

### Returns

*   Dict: A dictionary with the service names of all assignable services.

### How To Use:

```python
my_api.services.get_service_provider_services_assignable(
    service_provider_id="service_provider_id"
)
```

### Example Data Returned (Formatted)

```json
{
    "serviceProviderId": "service_provider_id",
    "userServices": {
            "serviceName": "Anonymous Call Rejection"
        },
        {
            "serviceName": "Authentication"
        },
        {
            "serviceName": "Call Forwarding Always"
        }
}
```