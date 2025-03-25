# PUT - User Voice Messaging Bulk

Modifies Bulk Voice Messaging Settings For A Passed List Of Users

### Parameters&#x20;

* updates (dict): Formatted Data To Emplace In The Put Request.&#x20;

### Returns

* None: This routine has no return type

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.put_user_voice_messaging_bulk(
    "Updates"
)
```
{% endcode %}

### Example Body Data (Formatted)

```json
{
	"data":{
		"isActive":true
	},
	"users":[
		{"userId":"9709580001@microv-works.com"},
		{"userId":"9709580002@microv-works.com"}
	]
}
```
