# GET - Enterprise Call Center Agents Unavailable Codes Settings

Retrieves call center agent unavailable codes that are hosted by the specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider IDD

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_agents_unavailable_codes_settings(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "enableAgentUnavailableCodes": true,
  "defaultAgentUnavailableCodeOnDND": 1002,
  "defaultAgentUnavailableCodeOnPersonalCalls": 1002,
  "defaultAgentUnavailableCodeOnConsecutiveBounces": 1002,
  "defaultAgentUnavailableCodeOnNotReachable": 1002,
  "forceUseOfAgentUnavailableCodes": false,
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
