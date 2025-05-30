# PUT - User ID

Updates the specified user's UserID, including domain.

{% hint style="warning" %}
**Warning:** This action may cause devices to become unregistered. When applying in bulk, please proceed with caution.
{% endhint %}

### Parameters&#x20;

* user\_id (str): Target user ID of the user you would like to change the UserID of.

### Returns

* None

### How To Use:

```python
my_api.users.put_user_id(
    "current_user_id",
    "new_user_id"
)
```