# PUT - User Shared Call Appearance

Updates Shared Call Appearance (SCA) settings for a specified user.

### Parameters

* user_id (str): Target user id to update SCA settings for
* settings (dict): Dictionary containing SCA settings to update

### Returns

* Dict: Updated SCA settings

### How To Use:

```python
my_api.shared_call_appearance.put_user_shared_call_appearance(
    user_id="user@example.com",
    settings={
        "enableMultipleCallArrangement":true,
	    "multipleCallArrangementIsActive":true,
	    "allowBridgingBetweenLocations":true,
    }
)
```

### Example Data Returned (Formatted)

```python
{
	"alertAllAppearancesForClickToDialCalls":true,
	"alertAllAppearancesForGroupPagingCalls":true,
	"maxAppearances":35,
	"allowSCACallRetrieve":true,
	"enableMultipleCallArrangement":true,
	"multipleCallArrangementIsActive":true,
	"allowBridgingBetweenLocations":true,
	"bridgeWarningTone":"Barge-In",
	"enableCallParkNotification":true,
	"userId":"9709580001@microv-works.com"
}
```
