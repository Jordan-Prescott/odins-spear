# GET - User Voice Messaging Messages

Retrieves The User's Voice Messaging Messages

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Messages.&#x20;

### Returns

* Dict: User Voice Messaging Messages

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_messages(
    "UserID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "messages": [
    {
      "duration": "8400",
      "read": true,
      "time": "1598022283436",
      "messageId": "/v2.0/user/dwood.test@alliedtelecom.net/VoiceMessagingMessages/24227e30-4afb-4fd4-ad51-a26b542efc94",
      "dateTime": "2020-08-21 15:04:43",
      "seconds": 8.4,
      "id": "24227e30-4afb-4fd4-ad51-a26b542efc94",
      "callingPartyInfoName": "WOOD AWESOME",
      "callingPartyInfoAddress": "sip:+15555555555@alliedtelecom.net"
    },
    {
      "duration": "6540",
      "read": true,
      "time": "1598020864225",
      "messageId": "/v2.0/user/dwood.test@alliedtelecom.net/VoiceMessagingMessages/726d5cba-1046-492e-b7ab-4abfa12fe2e5",
      "dateTime": "2020-08-21 14:41:04",
      "seconds": 6.54,
      "id": "726d5cba-1046-492e-b7ab-4abfa12fe2e5",
      "callingPartyInfoName": "WOOD AWESOME",
      "callingPartyInfoAddress": "sip:+15555555555@alliedtelecom.net"
    },
    {
      "duration": "6860",
      "read": true,
      "time": "1599069908638",
      "messageId": "/v2.0/user/dwood.test@alliedtelecom.net/VoiceMessagingMessages/1c778318-b656-4d2f-a29b-ed50e4ebbcaf",
      "dateTime": "2020-09-02 18:05:08",
      "seconds": 6.86,
      "id": "1c778318-b656-4d2f-a29b-ed50e4ebbcaf",
      "callingPartyInfoName": "WOOD AWESOME",
      "callingPartyInfoAddress": "sip:+15555555555@alliedtelecom.net"
    }
  ],
  "userId": "dwood.test@alliedtelecom.net"
}
```
