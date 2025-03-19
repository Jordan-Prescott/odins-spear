# GET - System DN Summary

Returns all numbers assigned to system.

### Returns

* List: List of all Service Providers/ Enterprises and numbers assigned in ranges.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.dns.get_system_dn_summary()
```
{% endcode %}

### Example Returned Data (Formatted)

```json
[
  {
    "isEnterprise": true,
    "serviceProviderId": "ent.odin",
    "min": "+1-5131111110",
    "max": "+1-5131111120"
  },
  {
    "isEnterprise": true,
    "serviceProviderId": "ent.odin",
    "min": "+1-6143334444",
    "max": "+1-6143334448"
  }
]
```
