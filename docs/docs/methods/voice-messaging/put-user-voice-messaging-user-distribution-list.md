# PUT - User Voice Messaging User Distribution List

Modifies A Specific User Distribution List For Voice Messaging

### Parameters&#x20;

* user\_id (str): The User ID For The Voice Messaging Service Settings.&#x20;
* list\_id (int): The Distribution List ID.&#x20;
* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging_user_distribution_list(
    "UserID",
    "ListID",
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
    "userId": "testuser1@cl1.lab.hosted-uc.com",
    "listId": "0",
    "description": "description-0",
    "phoneNumbers": [
        "5133334001",
        "5133334002"
    ]
}
```