# PUT - Group Voice Messaging Portal

Modifies The Groups Advanced Voice Messaging Portal Service Settings

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Group is located.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_group_voice_messaging_portal(
    "ServiceProviderID",
    "GroupID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
	"serviceUserId":"224374430_261921865_VMR",
	"serviceInstanceProfile":{
		"name":"Voice Portal",
		"callingLineIdLastName":"Voice Portal",
		"callingLineIdFirstName":"Voice Portal",
		"hiraganaLastName":"Voice Portal",
		"hiraganaFirstName":"Voice Portal",
		"language":"English",
		"timeZone":"America/Denver"
	},
	"isActive":false,
	"enableExtendedScope":false,
	"allowIdentificationByPhoneNumberOrVoiceMailAliasesOnLogin":false,
	"useVoicePortalWizard":true,
	"voicePortalExternalRoutingScope":"System",
	"useExternalRouting":false,
	"serviceProviderId":"odin.mock.ent1",
	"groupId":"odin.mock.grp1"
}
```