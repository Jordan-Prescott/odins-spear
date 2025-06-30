# GET - Enterprise Call Center Threshold Profiles

Retrieves threshold profiles of specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Service Provider enhanced reporting

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_threshold_profiles(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
[
  {
    "default": true,
    "name": "Default Agent Threshold Profile",
    "description": "Default Agent Threshold Profile"
  }
]
```
