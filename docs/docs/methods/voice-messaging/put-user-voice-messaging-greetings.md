# PUT - User Voice Messaging Greetings

Modifies The User's Voice Messaging Greetings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging_greetings(
    "UserID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
    "busyAnnouncementSelection": "Default",
    "noAnswerAnnouncementSelection": "Default",
    "noAnswerAlternateGreeting01": {
        "name": "",
        "audio": null
    },
    "noAnswerAlternateGreeting02": {
        "name": "",
        "audio": null
    },
    "noAnswerAlternateGreeting03": {
        "name": "",
        "audio": null
    },
    "extendedAwayEnabled": false,
    "extendedAwayDisableMessageDeposit": true,
    "noAnswerNumberOfRings": 3,
    "disableMessageDeposit": false,
    "disableMessageDepositAction": "Disconnect",
    "userId": "user.hwilkins@voicecci.net",
    "busyPersonalAudio": null,
    "noAnswerPersonalAudio": null,
    "extendedAwayAudio": null
}
```