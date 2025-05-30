# DELETE - Delete User

Removes the specified user from the platform entirely.

{% hint style="danger" %}
**Warning:** This action will permanently delete the user and all associated attributes, including unassigning phone numbers. Once deleted, this action cannot be undone unless a prior backup exists. Proceed with caution.
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to delete

### Returns

* None

### How To Use:

```python
my_api.users.delete_user(
    "user_ID"
)
```
