# GET - User Call Center

Retrieves a list of call centers that the specified user is currently associated with.

### Parameters&#x20;

* user_id (str): Target User ID.

### Returns

* Dict: Agents Call Centers setting and a list of the User's associated Call Centers.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_centers.get_user_call_center(
    user_id="myUserID@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "agentACDState": "Available",
  "agentThresholdProfileName": "Default Agent Threshold Profile",
  "useDefaultGuardTimer": true,
  "enableGuardTimer": false,
  "guardTimerSeconds": 5,
  "useSystemDefaultUnavailableSettings": true,
  "forceAgentUnavailableOnDNDActivation": false,
  "forceAgentUnavailableOnPersonalCalls": false,
  "forceAgentUnavailableOnBouncedCallLimit": false,
  "numberConsecutiveBouncedCallsToForceAgentUnavailable": 3,
  "forceAgentUnavailableOnNotReachable": false,
  "makeOutgoingCallsAsCallCenter": false,
  "userId": "myUserID@domain.com",
  "callCenters": [
    {
      "serviceUserId": "TestCallCenter",
      "phoneNumber": null,
      "extension": null,
      "available": true,
      "logoffAllowed": false,
      "type": "Premium",
      "priority": 1,
      "routingType": "Priority Based",
      "skillLevel": null
    }
  ]
}
```
