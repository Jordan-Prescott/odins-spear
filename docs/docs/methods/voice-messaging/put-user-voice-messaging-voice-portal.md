# PUT - User Voice Messaging Voice Portal

Modifies The User's Voice Messaging Voice Portal Settings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging_voice_portal(
    "UserID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
    "usePersonalizedName": false,
    "voicePortalAutoLogin": true,
    "personalizedNameAudioFile": {
        "name": "Announcement",
        "mediaFileType": "WAV",
        "level": "User"
    },
    "userId": "9871515000@odinapi.net"
}
```