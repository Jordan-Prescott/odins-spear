# GET - Enterprise Call Center

Retrieves call center settings that are hosted by the specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "useSystemDefaultGuardTimer": false,
  "enableGuardTimer": true,
  "guardTimerSeconds": 5,
  "useSystemDefaultUnavailableSettings": false,
  "forceAgentUnavailableOnDNDActivation": true,
  "forceAgentUnavailableOnPersonalCalls": true,
  "forceAgentUnavailableOnBouncedCallLimit": true,
  "numberConsecutiveBouncedCallsToForceAgentUnavailable": 3,
  "forceAgentUnavailableOnNotReachable": true,
  "serviceProviderId": "ent.odin"
}
```
