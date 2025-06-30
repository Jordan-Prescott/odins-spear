# GET - Enterprise Call Center Agents Unavailable Codes

Retrieves call center agent unavailable codes that are hosted by the specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target service provider ID

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_agents_unavailable_codes(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "codes": [
    {
      "isActive": true,
      "code": 1001,
      "description": 1001
    },
    {
      "isActive": true,
      "code": 1002,
      "description": "description 1002"
    }
  ],
  "serviceProviderId": "ent.odin"
}
```
