# GET - Service Providers Trunk Call Capacity Report Show

Returns a report of each group in a Servcice Provider showing their call capacity values etc..

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider ID

### Returns

* Dict: Detailed report of group and trunk group details.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.trunk_groups.get_service_providers_trunk_call_capacity_report_show(
    "ServiceProviderID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceProviderId": "ent.odin",
  "serviceProviderTrunkCapacity": {
    "serviceProviderId": "ent.odin",
    "maxActiveCalls": 40,
    "burstingMaxActiveCalls": -1
  },
  "groups": [
    {
      "groupId": "connections.demo",
      "groupName": "connections.demo",
      "userLimit": 200,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Limited",
        "quantity": 1,
        "usage": 0,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 10,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "connections.demo"
      }
    },
    {
      "groupId": "group.odin",
      "groupName": "odin Group",
      "userLimit": 100,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Unlimited",
        "quantity": -1,
        "usage": 4,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 15,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "group.odin"
      }
    },
    {
      "groupId": "phonism.test",
      "groupName": "Phonism Test",
      "userLimit": 25,
      "service": {
        "serviceName": "Trunk Group",
        "authorized": true,
        "assigned": true,
        "limited": "Unlimited",
        "quantity": -1,
        "usage": 0,
        "licensed": true,
        "allowed": -1,
        "alias": "Trunk Group"
      },
      "groupTrunkCapacity": {
        "maxActiveCalls": 40,
        "maxAvailableActiveCalls": 40,
        "burstingMaxActiveCalls": 0,
        "burstingMaxAvailableActiveCalls": -1,
        "serviceProviderId": "ent.odin",
        "groupId": "phonism.test"
      }
    }
  ]
}
```
