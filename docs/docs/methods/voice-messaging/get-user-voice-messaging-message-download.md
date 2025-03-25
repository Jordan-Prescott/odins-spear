# GET - User Voice Messaging Message Download

Downloads A Specific User Voice Message

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service.&#x20;
* id (str): The Message ID For The Specific Voice Message.&#x20;

### Returns

* bytes: The Downloaded Voice Message File

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_message_download(
    "UserID",
    "ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{}
```
