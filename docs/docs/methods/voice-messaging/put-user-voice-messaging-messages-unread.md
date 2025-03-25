# PUT - User Voice Messaging Messages Unread

Marks User Voice Messages As Unread

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;
* updates (dict): Message IDs To Mark As Unread.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging_messages_unread(
    "UserID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
    "messages": [
        {
            "id": "726d5cba-1046-492e-b7ab-4abfa12fe2e5"
        },
        {
            "id": "f39e47f0-d75c-4095-9bd9-c33430665eb0"
        },
        {
            "id": "1c778318-b656-4d2f-a29b-ed50e4ebbcaf"
        }
    ]
}
```