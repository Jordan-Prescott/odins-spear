# GET - Group Voice Messaging Portal

Retrieves The Groups Advanced Voice Messaging Portal Service Settings

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Group is located.&#x20;

### Returns

* Dict: Advanced Voice Messaging Portal

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_group_voice_messaging_portal(
    "ServiceProviderID",
    "GroupID",
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "serviceUserId": "224374430_261921865_VMR",
  "serviceInstanceProfile": {
    "name": "Voice Portal",
    "callingLineIdLastName": "Voice Portal",
    "callingLineIdFirstName": "Voice Portal",
    "hiraganaLastName": "Voice Portal",
    "hiraganaFirstName": "Voice Portal",
    "language": "English",
    "timeZone": "America/Denver",
    "timeZoneDisplayName": "(GMT-06:00) (US) Mountain Time"
  },
  "isActive": false,
  "enableExtendedScope": false,
  "allowIdentificationByPhoneNumberOrVoiceMailAliasesOnLogin": false,
  "useVoicePortalWizard": true,
  "voicePortalExternalRoutingScope": "System",
  "useExternalRouting": false,
  "serviceProviderId": "odin.mock.ent1",
  "groupId": "odin.mock.grp1"
}
```
