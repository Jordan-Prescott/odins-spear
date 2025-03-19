# DELETE - Delete User

Removes the specified user from the platform entirely.

{% hint style="danger" %}
**Warning:** This action will permanently delete the user and all associated attributes, including unassigning phone numbers. Once deleted, this action cannot be undone unless a prior backup exists. Proceed with caution.
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to delete

### Returns

* Nothing

### How To Use:

{% code overflow="wrap" %}
```python
my_api.users.delete_user(
    "user_ID"
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[]
```