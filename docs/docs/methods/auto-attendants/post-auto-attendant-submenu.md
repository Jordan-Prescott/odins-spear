# POST - Auto Attendant Submenu

Posts a new submenu to the specified Auto Attendant (AA).

### Parameters&#x20;

* service_user_id (str): Service User ID of the AA.
* submenu_id (str): ID of the submenu to be created. 
* announcement_selection (str, optional): "Default" or "Personal". Defaults to "Default".
* extension_dialing (bool, optional): Whether Level Extension Dialing is enabled or not. Defaults to True.

### Returns

* None: This method does not return any specific value.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.auto_attendants.post_auto_attendant_submenu(
    service_user_id= "test_aa@domain.net", 
    submenu_id="Menu 1"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[]


```
