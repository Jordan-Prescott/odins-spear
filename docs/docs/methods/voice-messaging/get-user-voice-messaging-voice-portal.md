# GET - User Voice Messaging Voice Portal

Retrieves The User's Voice Messaging Voice Portal Settings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service.&#x20;

### Returns

* Dict: User Voice Messaging Voice Portal Settings

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_voice_portal(
    "UserID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "usePersonalizedName": true,
  "voicePortalAutoLogin": true,
  "personalizedNameAudioFile": {
    "name": "Announcement",
    "mediaFileType": "WAV",
    "level": "User"
  },
  "userId": "9871515000@odinapi.net"
}
```
