# GET - Auto Attendant Submenus

Returns a list of the submenus of the specified Auto Attendant (AA). Works with Standard AAs only, basic AAs do not have submenus.

### Parameters&#x20;

* service_user_id (str): The service user ID of the AA.

### Returns

* List: Returns a list of the submenus associated with the AA.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.auto_attendants.get_auto_attendant_submenus(
    service_user_id="test_aa@domain.net"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
    {
        "submenuId": "Submenu 1",
        "isUsed": false,
        "serviceUserId": "test_aa@domain.com"
    },
    {
        "submenuId": "Submenu 2",
        "isUsed": false,
        "serviceUserId": "test_aa@domain.com"
    }
]

```
