# PUT - Group Voice Messaging

Modifies The Groups Advanced Voice Messaging Service Settings

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Group is located.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_group_voice_messaging(
    "ServiceProviderID",
    "GroupID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
	"useMailServerSetting":"System Mail Server",
	"warnCallerBeforeRecordingVoiceMessage":false,
	"allowUsersConfiguringAdvancedSettings":true,
	"allowComposeOrForwardMessageToEntireGroup":false,
	"mailServerProtocol":"POP3",
	"realDeleteForImap":false,
	"maxMailboxLengthMinutes":30,
	"doesMessageAge":false,
	"holdPeriodDays":15,
	"serviceProviderId":"odin.mock.ent1",
	"groupId":"odin.mock.grp1"
}
```