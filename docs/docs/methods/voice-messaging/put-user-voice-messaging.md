# PUT - User Voice Messaging

Modifies The User's Voice Messaging Service Settings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging(
    "UserID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
    "isActive": true,
    "processing": "Unified Voice and Email Messaging",
    "voiceMessageDeliveryEmailAddress": "developer@parkbenchsolutions.com",
    "usePhoneMessageWaitingIndicator": true,
    "sendVoiceMessageNotifyEmail": true,
    "voiceMessageNotifyEmailAddress": "developer@parkbenchsolutions.com",
    "sendCarbonCopyVoiceMessage": true,
    "voiceMessageCarbonCopyEmailAddress": "developer@parkbenchsolutions.com",
    "transferOnZeroToPhoneNumber": true,
    "transferPhoneNumber": 1005551414,
    "alwaysRedirectToVoiceMail": false,
    "busyRedirectToVoiceMail": true,
    "noAnswerRedirectToVoiceMail": true,
    "outOfPrimaryZoneRedirectToVoiceMail": false,
    "userId": "4001@parkbenchsolutions.com",
    "serviceProviderId": "ent.odin",
    "groupId": "grp.odin",
    "isEnterprise": true
}
```