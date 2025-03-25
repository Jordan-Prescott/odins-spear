# GET - User Voice Messaging Advanced

The User's Advanced Voice Messaging Settings

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service.&#x20;

### Returns

* Dict: User Advanced Voice Messaging Settings

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_advanced(
    "UserID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "mailServerSelection": "Group Mail Server",
  "groupMailServerEmailAddress": "vm4001.5001@parkbenchsolutions.com",
  "groupMailServerUserId": "vm4001.5001",
  "useGroupDefaultMailServerFullMailboxLimit": true,
  "personalMailServerProtocol": "POP3",
  "personalMailServerRealDeleteForImap": false,
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "userId": "4001.5001@lab.tekvoice.net"
}
```
