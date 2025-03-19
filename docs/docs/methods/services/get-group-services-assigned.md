# GET - Group Services Assigned

Get details of the user/service instances where a particular service is assigned.

### Parameters&#x20;

*    group\_id (str): GroupID being targeted
*    service_provider\_id (str): Service provider/Enterprise ID where the group is located.
*    service_name (str): Name of the service querying
*    service_type (str): Type of service. Either: serviceName or servicePackName

### Returns

* Dict: Users/Service Instances where the service is assigned.

### How To Use:

```python
my_api.services.get_group_services_assigned(
    "groupId",
    "serviceProviderId",
    "serviceType",
    "serviceName"
)
```
{% endcode %}



### Example Data Returned (Formatted)
```json
{
   "serviceProviderId":"Test-Enterprise-EU",
   "groupId":"TGDMS",
   "serviceType":"userServices",
   "serviceName":"Anonymous Call Rejection",
   "users":[
      
   ]
}
```
```
