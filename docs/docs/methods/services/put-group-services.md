# PUT - Group Services

Update the services assigned to a group.

### Parameters

*   service\_provider\_id (str): Service provider ID of the target
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
    service_provider_id="service_provider_id",
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
  "serviceProviderId": "service_provider_id",
  "groupId": "group_id",
  "userServices": [
    {
      "serviceName": "Anonymous Call Rejection",
      "authorized": true,
      "assigned": false,
      "limited": "Unlimited",
      "quantity": -1,
      "usage": 0,
      "licensed": true,
      "allowed": -1,
      "userAssignable": true,
      "groupServiceAssignable": true,
      "tags": [],
      "alias": "Anonymous Call Rejection"
    },
  ]
}
```