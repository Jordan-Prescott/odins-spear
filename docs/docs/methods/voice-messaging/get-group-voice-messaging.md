# GET - Group Voice Messaging

Retrieves The Groups Advanced Voice Messaging Service Settings

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Group is located.&#x20;

### Returns

* Dict: Advanced Voice Messaging 

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_group_voice_messaging(
    "ServiceProviderID",
    "GroupID",
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "useMailServerSetting": "System Mail Server",
  "warnCallerBeforeRecordingVoiceMessage": false,
  "allowUsersConfiguringAdvancedSettings": true,
  "allowComposeOrForwardMessageToEntireGroup": false,
  "mailServerProtocol": "POP3",
  "realDeleteForImap": false,
  "maxMailboxLengthMinutes": 30,
  "doesMessageAge": false,
  "holdPeriodDays": 15,
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1"
}
```
