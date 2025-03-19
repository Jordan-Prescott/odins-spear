# GET - Call Forward Always

Retrieves the Forwarding Always status for the specified User.

### Parameters&#x20;

* user\_id (str): Target User ID

### Returns

* Dict: Forwarding enabled status, and the Number to be Forwarded to.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_forwarding_always.get_user_call_forwarding_always{
    "userId"
}

```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "isActive": true,
  "forwardToPhoneNumber": 4500,
  "isRingSplashActive": false,
  "userId": "4001@pdomain.com"
}

```