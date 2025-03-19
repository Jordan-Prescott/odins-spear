# GET - SIP Password Generate

Generates a single SIP password.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.&#x20;
* group\_id (str): Group ID to generate SIP password for.

### Returns

* dict: Single SIP password generated according to the groups rules.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.password_generate.get_sip_password_generate(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "password": "8!01T_8Hk{R6"
}
```
