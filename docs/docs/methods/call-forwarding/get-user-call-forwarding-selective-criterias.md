---
description: my_api.get.user_call_forwarding_selective_criterias()
---

# 🚗 GET - Call Forward selective criterias

Retrieves the Forwarding Selective status for a specified User, alongside the criteria's assigned.

### Parameters&#x20;

* user\_id (str): Target User ID

### Returns

* Dict: Forwarding enabled status and the Forwarding criteria's names and settings.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import api

my_api= api.Api(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_api.get.user_call_forwarding_selective_criterias{
    "userId"
}

```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "isActive": true,
    "criteriaName": "selective1",
    "timeSchedule": "Every Day All Day",
    "blacklisted": false,
    "holidaySchedule": "None",
    "forwardTo": 5131234321,
    "callsToType": null,
    "callsToNumber": null,
    "callsToExtension": null,
    "callsFrom": [
      "All calls"
    ]
  },
  {
    "isActive": false,
    "criteriaName": "selective2",
    "timeSchedule": "test",
    "blacklisted": false,
    "holidaySchedule": "None",
    "forwardTo": 5131234321,
    "callsToType": null,
    "callsToNumber": null,
    "callsToExtension": null,
    "callsFrom": [
      "Any private number",
      "Any unavailable number"
    ]
  }
]

```