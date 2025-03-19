# GET - Auto Attendant Submenu Usage

Returns the type of the specified Auto Attendant (AA) submenu. NOTE: This method does not return any usage data. 

### Parameters&#x20;

* service_user_id (str): The servivce user ID of the AA being queried.
* submenu_id (str): The submenu ID of the submenu being queried. 

### Returns

* List: Returns a list containing a single dict of the submenu. 

### How To Use:

{% code overflow="wrap" %}
```python
my_api.auto_attendants.get_auto_attendant_submenus(
    service_user_id="test_aa@domain.net", 
    submenu_id="Submenu 1"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
[
    {
        "type": "Business Hours Menu",
        "submenuId": null
    }
]

```
