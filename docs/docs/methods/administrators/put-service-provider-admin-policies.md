# PUT - Service Provider Admin Policies

Builds Service Provider level administrattor.

### Parameters&#x20;

* user_id (str): User ID of target service provider admin.
* policy_config (dict): Policy settings to update.

### Returns

* None

### How To Use:

```python
from odins_spear import API

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

my_policy = {
    "profileAccess": "Read-Only",
    "groupAccess": "None",
    "userAccess": "Full Profile",
    "adminAccess": "Full",
    "departmentAccess": "Full",
    "accessDeviceAccess": "Associate User With Device",
    "phoneNumberExtensionAccess": "Assign To Services and Users",
    "callingLineIdNumberAccess": "Full",
    "serviceAccess": "No Authorization",
    "servicePackAccess": "None",
    "sessionAdmissionControlAccess": "Read-Only",
    "webBrandingAccess": "None",
    "officeZoneAccess": "Read-Only",
    "communicationBarringAccess": "Read-Only",
    "networkPolicyAccess": "Full",
    "numberActivationAccess": "Read-Only",
    "dialableCallerIDAccess": "Full",
}

my_api.administrators.put_service_provider_admin_policies(
	user_id="userId", 
	policy=my_policy)


```
{% endcode %}