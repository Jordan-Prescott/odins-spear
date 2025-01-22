# Service Provider Trunking Capacity

Returns a JSON breakdown of the Trunking Call Capacity of a Service Provider/ Enterprise (SP/ENT). This will show the totals at each level from SP/ ENT to Group to Trunk Groups located in Groups. At each level Max Active Calls and Bursting Max Active calls are detailed and then differences at calculated.

{% hint style="info" %}
```
This does not return data on Enterprise Trunks.
```
{% endhint %}

The script makes use of the following methods:

```python
api.trunk_groups.get_service_provider_trunk_group_call_capacity()
api.groups.get_groups()
api.trunk_groups.get_group_trunk_groups_call_capacity()
api.trunk_groups.get_group_trunk_groups()
api.trunk_groups.get_group_trunk_group()
```

### Parameters&#x20;

* service\_provider\_id (str): Target Service Provider ID/ Enterprise ID that you would like the Trunk Call Capacity breakdown.

### Return

* JSON:  JSON data of Trunking Call Capacity details of SP/ ENT, Groups, and Trunk Groups.

### How To Use:

{% hint style="info" %}
This method requires keyword arguments i.e. group_id="group_id"
{% endhint %}

```python
from odins_spear import API, Scripter

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

assistant = Scripter(my_api)

assistant.service_provider_trunking_capacity(
    service_provider_id="ServiceProviderID"
)

```

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "serviceProviderId": "ServiceProviderID",
  "maxActiveCalls": 226,
  "burstingMaxActiveCalls": 18,
  "groupsCallCapacityTotal": 114,
  "groupsBurstingCallCapacityTotal": 36,
  "groups": [
    {
      "groupId": "GroupIDA",
      "groupName": "Group A",
      "maxActiveCalls": 13,
      "burstingMaxAvailableActiveCalls": 5,
      "burstingMaxActiveCalls": 2,
      "trunkGroups": [
        {
          "name": "Trunk 1",
          "maxActiveCalls": 1,
          "burstingMaxActiveCalls": 0
        },
        {
          "name": "Trunk 2",
          "maxActiveCalls": 1,
          "burstingMaxActiveCalls": 0
        },
        {
          "name": "Trunk 3",
          "maxActiveCalls": 2,
          "burstingMaxActiveCalls": 0
        }
      ],
      "trunkGroupsCallCapacityTotal": 4,
      "trunkGroupsBurstingCallCapacityTotal": 0,
      "callCapacityDifference": 9,
      "burstingCallCapacityDifference": 0
    },
    {
      "groupId": "GroupIDB",
      "groupName": "Group B",
      "maxActiveCalls": 36,
      "burstingMaxAvailableActiveCalls": 5,
      "burstingMaxActiveCalls": 2,
      "trunkGroups": [
        {
          "name": "Trunk 1",
          "maxActiveCalls": 1,
          "burstingMaxActiveCalls": 0
        },
        {
          "name": "Trunk 2",
          "maxActiveCalls": 1,
          "burstingMaxActiveCalls": 0
        },
        {
          "name": "Trunk 3",
          "maxActiveCalls": 9,
          "burstingMaxActiveCalls": 0
        }
      ],
      "trunkGroupsCallCapacityTotal": 11,
      "trunkGroupsBurstingCallCapacityTotal": 0,
      "callCapacityDifference": 25,
      "burstingCallCapacityDifference": 0
    }
  "callCapacityDifference": 112,
  "burstingCallCapacityDifference": -18
```
