# PUT - User Call Center

### Parameters&#x20;

* user\_id (str): User ID of the target user.&#x20;
* updates (dict): Updates to be applied to the user.

### Returns

* Dict: Agents' ACD status and status in each CC they are assigned to.

### How To Use:

```python
my_user_id = "user_id@domain.com"
my_updates = {
	"agentACDState":"Available",
	"agentThresholdProfileName":"Default Agent Threshold Profile",
	"useDefaultGuardTimer":true,
	"enableGuardTimer":false,
	"guardTimerSeconds":5,
	"useSystemDefaultUnavailableSettings":true,
	"forceAgentUnavailableOnDNDActivation":false,
	"forceAgentUnavailableOnPersonalCalls":false,
	"forceAgentUnavailableOnBouncedCallLimit":false,
	"numberConsecutiveBouncedCallsToForceAgentUnavailable":3,
	"forceAgentUnavailableOnNotReachable":false,
	"makeOutgoingCallsAsCallCenter":false,
	"callCenters":[
		{
			"serviceUserId":"mock.cc.1",
			"available":true,
			"skillLevel":null
		},
		{
			"serviceUserId":"mock.cc.2",
			"available":true,
			"skillLevel":10
		}
	]
}

my_api.call_centers.put_user_call_center(
    user_id = my_user_id,
    updates= my_updates 
)
```
