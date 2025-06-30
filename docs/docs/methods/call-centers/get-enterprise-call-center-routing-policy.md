# GET - Enterprise Call Center Routing Policy

Retrieves call center call routing settings that are hosted by the specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID

### Returns

* Dict: Call Centers and their settings.

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_routing_policy(
    service_provider_id="ent.odin"
)
```

### Example Returned Data (Formatted)
```python
{
  "routingPolicy": "Longest Wait Time",
  "callCenters": [
    {
      "serviceUserId": "call-center-1",
      "name": "CC1-test-1",
      "priority": 1
    },
    {
      "serviceUserId": "call-center-2",
      "name": "call centeww12340000",
      "priority": 2
    },
    {
      "serviceUserId": "standard-cc-1",
      "name": "standard-cc-1",
      "priority": 3
    },
    {
      "serviceUserId": "call-center-1-test-1",
      "name": "call-center-1-test-1",
      "priority": 4
    },
    {
      "serviceUserId": "9871515004",
      "name": "mock.cc.1",
      "priority": 5
    },
    {
      "serviceUserId": "9871515005",
      "name": "mock.cc.2",
      "priority": 6
    },
    {
      "serviceUserId": "9871515006",
      "name": "mock.cc.3",
      "priority": 7
    },
    {
      "serviceUserId": "9871515007",
      "name": "mock.cc.4",
      "priority": 8
    },
    {
      "serviceUserId": "9871515008",
      "name": "mock.cc.5",
      "priority": 9
    },
    {
      "serviceUserId": "9871515009",
      "name": "mock.cc.6",
      "priority": 10
    },
    {
      "serviceUserId": "mock.cc.7",
      "name": "mock.cc.7",
      "priority": 11
    },
    {
      "serviceUserId": "Prithwidipta@abccorp.com",
      "name": "Prithwidipta Samajpati",
      "priority": 12
    }
  ],
  "serviceProviderId": "ent.odin"
}
```
