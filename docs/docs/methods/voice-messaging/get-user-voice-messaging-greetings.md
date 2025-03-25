# GET - User Voice Messaging Greetings

Retrieves The User's Voice Messaging Greetings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service.&#x20;

### Returns

* Dict: User Voice Messaging Greetings 

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_greetings(
    "UserID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "busyAnnouncementSelection": "Default",
  "noAnswerAnnouncementSelection": "Default",
  "noAnswerNumberOfRings": 4,
  "disableMessageDeposit": false,
  "disableMessageDepositAction": "Disconnect",
  "userId": "9709580001@microv-works.com"
}
```
