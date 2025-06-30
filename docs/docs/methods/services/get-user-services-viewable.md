# GET - User Services Viewable

Same as User Services Assigned, except filtered for Viewable Service Pack assignment.

### Parameters

*   user\_id (str): ID of the target user

### Returns

*   Dict: A dictionary containing all the services viewable by the user.

### How To Use:

```python
my_api.services.get_user_services_viewable(
    user_id="your_user_id"
)
```

### Example Data Returned (Formatted)

```json
{
  "userId": "0@domain.com",
  "userServices": [
    {
      "serviceName": "Authentication"
    },
    {
      "serviceName": "Basic Call Logs"
    },
    {
      "serviceName": "BroadWorks Anywhere"
    },
    {
      "serviceName": "BroadWorks Mobility",
      "isActive": "false"
    }
  ]
}
```