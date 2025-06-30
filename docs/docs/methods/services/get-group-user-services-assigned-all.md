# GET - Get Group User Services Assigned All

Retrieves a list of all users assigned to a specific service within a given group, whether the service is assigned directly or via a service pack.

### Parameters

*   service\_provider\_id (str): Service provider/Enterprise ID being targeted.
*   group\_id (str): GroupID being targeted.
*   service\_name (str): Name of the service querying.
*   service\_type (str): Type of service. Either: serviceName or servicePackName 

### Returns

*   Dict: Users/Service Instances where the service is assigned.

### How To Use:

```python
my_api.services.group_user_services_assigned_all(
    "serviceProviderId",
    "groupId",
    "serviceName",
    "serviceType"
)
```
{% endcode %} 



### Example Data Returned (Formatted)
```json
{
    "serviceProviderId": "service_provider_id",
    "groupId": "group_id",
    "serviceType": "serviceName",
    "serviceName": "Authentication",
    "users": [
        {
            "userId": "john.doe@domain.com",
            "lastName": "Doe",
            "firstName": "John",
            "department": "Sales",
            "phoneNumber": null,
            "emailAddress": null,
            "hiraganaLastName": "Doe",
            "hiraganaFirstName": "John",
            "extension": "1000"
        }
    ]
}
```