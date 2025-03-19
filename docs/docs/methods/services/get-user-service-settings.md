# GET - User Service Settings

This method grabs all of a Broadwork entity's service settings.

### Parameters&#x20;

* user\_id (str): User ID of the target Broadworks entity.

### Returns

* Dict: Broadworks entity and all service settings.

### How To Use:

```python
my_api.services.get_user_service_settings(
    "userId@domain.com"
)
```
{% endcode %}

### Example Data Returned (Formatted)
```json
{
  "userId": "user@odinapi.net",
  "Advice Of Charge": {
    "isActive": false,
    "aocType": "During Call"
    }
}
```
```