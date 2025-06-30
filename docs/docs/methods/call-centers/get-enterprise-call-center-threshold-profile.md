# GET - Enterprise Call Center Threshold Profile

Retrieves a threshold profile of specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* profile_name (str): Target profile Name

### Returns

* Dict: Service Provider enhanced reporting

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_threshold_profile(
    service_provider_id="ent.odin",
    profile_name="profile name"
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
