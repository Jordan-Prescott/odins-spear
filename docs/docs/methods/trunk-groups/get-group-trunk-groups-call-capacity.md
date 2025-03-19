# GET - Group Trunk Groups Call Capacity

Fetches Trunk Call Capacity data for a single Group.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located.&#x20;
* group\_id (str): Target Group to return data on.

### Returns

* Dict: Trunk Group Call Capacity data of target group.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.trunk_groups.get_group_trunk_groups_call_capacity(
    "ServiceProviderID",
    "GroupID"
    
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "maxActiveCalls": 3,
  "maxAvailableActiveCalls": 5,
  "burstingMaxActiveCalls": 3,
  "burstingMaxAvailableActiveCalls": 5,
  "serviceProviderId": "odin.mock.sp1",
  "groupId": "odin.mock.sp1.grp1"
}
```
