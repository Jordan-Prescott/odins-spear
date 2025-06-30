# GET - Enterprise Call Center Enhanced Reporting Branding

Enables/ retrieves enhanced reporting for specified service provider.

NOTE: Not fully understood, use with caution.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_enhanced_reporting_branding(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "serviceProviderId": "ent.odin",
  "brandingChoice": "Custom",
  "brandingFileDescription": "branding.xsl"
}
```
