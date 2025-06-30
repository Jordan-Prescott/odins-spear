# GET - Enterprise Call Center Enhanced Reporting

Enables/ retrieves enhanced reporting for specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Service Provider enhanced reporting

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_enhanced_reporting(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "serviceProviderId": "ent.odin",
  "reportingServer": "Enhanced"
}
```
