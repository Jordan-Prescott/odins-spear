# GET - Password Generate

Generates a single passwords following the groups rules.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider ID where Group is located.
* group\_id (str): Group ID to generate password for.

### Returns

* dict: Single password generated according to the groups rules..

### How To Use:

{% code overflow="wrap" %}
```python
my_api.password_generate.get_password_generate(
    "serviceProviderId",
    "groupID",
)
```
{% endcode %}

### Example Returned Data of SIP Passwords (Formatted)

```json
{
  "password": "?+^8RZ40MeC3+:i.BQ"
}
```
