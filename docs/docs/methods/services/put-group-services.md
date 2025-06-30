# PUT - Group Services

Update the services assigned to a group.

### Parameters

*   group\_id (str): Group ID of the target
*   services (list): List of services to be applied to group.
*   assigned (bool, optional): Assign (True) or unassign(False). Defaults to True.
*   authorized (bool, optional): Authorize (True) or unauthorize(False). Defaults to True.
*   quantity (int, optional): Quantity of services to be applied to group. Defaults to None.
*   unlimited (bool, optional): If True, quantity is unlimited. Defaults to False.
*   allocated (int, optional): Allocated quantity of services to be applied to group. Defaults to None.

### How To Use:

```python
my_api.services.put_group_services(
    group_id="group_id",
    services=["Anonymous Call Rejection", "Authentication"],
    assigned=True,
    authorized=True,
    quantity=10,
    allocated=5
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