# GET - Group Services User Assigned

Get details of users who have a service assigned directly. This excludes users who have the service assigned via a service pack.

### Parameters

*   group\_id (str): GroupID being targeted
*   service\_provider\_id (str): Service provider/Enterprise ID where the group is located.
*   service\_name (str): Name of the service querying
*   service\_type (str): Type of service. Either: serviceName or servicePackName

### Returns

*   Dict: Users/Service Instances where the service is assigned.

### How To Use:

## Example 1

```python
my_api.services.get_group_services_user_assigned(
    group_id="group_id",
    service_provider_id="service_provider_id",
    service_name="Anonymous Call Rejection",
    service_type="serviceName"
)
```

### Example Data Returned (Formatted)

```json
{
    "serviceProviderId": "serviceProviderId",
    "groupId": "groupId",
    "serviceType": "serviceName",
    "serviceName": "Authentication",
    "users": [
        {
            "userId": "john.doe@domain.com",
            "lastName": "Doe",
            "firstName": "John",
            "department": "Department",
            "phoneNumber": null,
            "emailAddress": null,
            "hiraganaLastName": "Doe",
            "hiraganaFirstName": "John",
            "extension": "0"
        }
    ]
}
```

## Example 2

```python
my_api.services.get_group_services_user_assigned(
    group_id="group_id",
    service_provider_id="service_provider_id",
    service_name="myServicePack",
    service_type="servicePackName"
)
```

### Example Data Returned (Formatted)

```json
{
    "serviceProviderId": "serviceProviderId",
    "groupId": "groupId",
    "serviceType": "servicePackName",
    "serviceName": "myServicePack",
    "users": [
        {
            "userId": "john.doe@domain.com",
            "lastName": "Doe",
            "firstName": "John",
            "department": "Department",
            "phoneNumber": null,
            "emailAddress": null,
            "hiraganaLastName": "Doe",
            "hiraganaFirstName": "John",
            "extension": "0"
        },
    ],
    and so on...
}
```