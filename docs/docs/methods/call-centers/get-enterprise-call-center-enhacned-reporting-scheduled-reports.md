# GET - Enterprise Call Center Enhanced Reporting Scheduling Reports

Retrieves list of all scheduled reports for specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_enhanced_reporting_scheduled_reports(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "scheduledReports": [
    {
      "scheduleName": "VSOS MPV - AGENT ACTIVITY DETAIL cc_7928416",
      "description": "VSOS MPV - AGENT ACTIVITY DETAIL cc_7928416",
      "createdBy": "Administrator",
      "isSupervisorReport": false,
      "status": "Active",
      "reportTemplateName": "Agent Activity Detail Report",
      "reportTemplateLevel": "System",
      "recurring": "Daily"
    },
    {
      "scheduleName": "VSOS MPV - CALL CENTER CALL DETAIL cc_7928416",
      "description": "VSOS MPV - CALL CENTER CALL DETAIL cc_7928416",
      "createdBy": "Administrator",
      "isSupervisorReport": false,
      "status": "Active",
      "reportTemplateName": "Call Center Call Detail Report",
      "reportTemplateLevel": "System",
      "recurring": "Daily"
    }
  ]
}
```
