# GET - Enterprise Call Center Enhanced Reporting Scheduling Report

Retrieves a single scheduled report for specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* schedule_name (str): Target Schedule Name

### Returns

* Dict: Service Provider enhanced reporting

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_enhanced_reporting_scheduled_report(
    service_provider_id="ent.odin",
    schedule_name="schedule name"
)
```

### Example Returned Data (Formatted)
```python
{
  "description": "VSOS MPV - CALL CENTER CALL DETAIL cc_7928416",
  "reportTemplate": {
    "templateLevel": "System",
    "templateName": "Call Center Call Detail Report"
  },
  "schedule": {
    "recurrence": {
      "timeZone": "America/Los_Angeles",
      "startDate": "2020-06-04-07:00",
      "scheduleTime": {
        "hour": "8",
        "minute": "40"
      },
      "recurrence": {
        "recurDaily": {
          "recurInterval": "1"
        },
        "recurForEver": "true"
      }
    }
  },
  "reportTimeZone": "America/Los_Angeles",
  "reportDateFormat": "MMDDYYYY",
  "reportTimeFormat": "AM/PM",
  "reportInterval": {
    "past": {
      "number": "1",
      "timeUnit": "Day"
    }
  },
  "reportFormat": "PDF",
  "callCenter": {
    "allCallCenter": "true"
  },
  "emailAddress": "joseph.malinao@hotmail.com",
  "serviceProviderId": "ent_366103",
  "scheduleName": "VSOS MPV - CALL CENTER CALL DETAIL cc_7928416"
}
```
