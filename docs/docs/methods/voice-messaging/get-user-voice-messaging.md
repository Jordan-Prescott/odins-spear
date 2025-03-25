# GET - User Voice Messaging

Retrieves The User's Voice Messaging Service Settings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;

### Returns

* Dict: User Voice Messaging Service Settings 

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging(
    "UserID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "isActive": true,
  "processing": "Unified Voice and Email Messaging",
  "voiceMessageDeliveryEmailAddress": "pbs.cc@parkbenchsolutions.com",
  "usePhoneMessageWaitingIndicator": true,
  "sendVoiceMessageNotifyEmail": true,
  "voiceMessageNotifyEmailAddress": "pbs.stt@parkbenchsolutions.com",
  "sendCarbonCopyVoiceMessage": true,
  "voiceMessageCarbonCopyEmailAddress": "pbs.cc@parkbenchsolutions.com",
  "transferOnZeroToPhoneNumber": true,
  "transferPhoneNumber": 4500,
  "alwaysRedirectToVoiceMail": false,
  "busyRedirectToVoiceMail": true,
  "noAnswerRedirectToVoiceMail": true,
  "outOfPrimaryZoneRedirectToVoiceMail": false,
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "userId": "4001.5001@lab.tekvoice.net"
}
```
