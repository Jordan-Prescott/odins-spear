# POST - Group Admin Policies Bulk

Applies policy settings to multiple group administrators.

### Parameters&#x20;

* user\_ids (list): User IDs of admins to apply policy to.
* policy\_config (dict): Policy settings to apply to target users.

### Returns

* Dict: Returns users and applied policies.

### How To Use:

```python
users = ['first_name.last_name','first_name.last_name']
# Customer admin account 
policy = {
    "profileAccess": "Read-Only",
    "userAccess": "Full Profile",    
    "adminAccess": "Read-Only",    
    "departmentAccess": "Full",    
    "accessDeviceAccess": "Read-Only",    
    "enhancedServiceInstanceAccess": "Modify-Only",    
    "featureAccessCodeAccess": "Read-Only",    
    "phoneNumberExtensionAccess": "Read-Only",    
    "callingLineIdNumberAccess": "Full",    
    "serviceAccess": "Read-Only",    
    "trunkGroupAccess": "Read-Only Resources",    
    "sessionAdmissionControlAccess": "Read-Only",    
    "officeZoneAccess": "Read-Only",    
    "numberActivationAccess": "None",    
    "dialableCallerIDAccess": "Full"
}

my_api.post.group_admin_policies_bulk(    
    user_ids=[user+group_domain for user in users],    
    policy_config=policy
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
{
  "users": [
    {
      "userId": "first_name.last_name"
    },
    {
      "userId": "first_name.last_name"
    }
  ],
  "data": {
    "profileAccess": "Read-Only",
    "userAccess": "Full Profile",    
    "adminAccess": "Read-Only",    
    "departmentAccess": "Full",    
    "accessDeviceAccess": "Read-Only",    
    "enhancedServiceInstanceAccess": "Modify-Only",    
    "featureAccessCodeAccess": "Read-Only",    
    "phoneNumberExtensionAccess": "Read-Only",    
    "callingLineIdNumberAccess": "Full",    
    "serviceAccess": "Read-Only",    
    "trunkGroupAccess": "Read-Only Resources",    
    "sessionAdmissionControlAccess": "Read-Only",    
    "officeZoneAccess": "Read-Only",    
    "numberActivationAccess": "None",    
    "dialableCallerIDAccess": "Full"
  }
}
```