# GET - System DN Utilisation

Returns DN statistics for each Service Provider/ Enterprise such as total DNs assigned.

### Returns

* List: List of all Service Provider/ Enterprises with statistics of DNs for each.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.dns.get_system_dn_utilization()
```
{% endcode %}

### Example Returned Data (Formatted)

```json
[
  {
    "serviceProviderId": "ent.odin",
    "phoneNumbers": 382,
    "assignedtoGroups": 159,
    "percentageAssigned": 41,
    "isEnterprise": true,
    "activatedOnGroups": 20
  }
]
```
