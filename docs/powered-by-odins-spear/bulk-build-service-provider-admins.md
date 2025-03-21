# Bulk Build Service Provider Admins

This script will build multiple service provider level admins and assign policy settings to all built. 

The policy confifuration is for customers with access to your odin portal but can be modified to fit needs.

### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import API

my_api = API("base_url", "username", "ENV-PASSWORD")

# CHANGE ME
service_provider_id = ""
group_id = ""  # choose a group from that sp (needed for password gen)
admin_type = "customer"  # change if needed options are 'normal', 'customer', 'password reset only'
language = "English"  # check language your system supports

# add the user ids to build
administrators = ["userId", "userId"]

# adjust policy to fit your needs
policy = {
    "profileAccess": "Read-Only",
    "groupAccess": "Restricted from Adding or Removing Groups",
    "userAccess": "Full Profile",
    "adminAccess": "Full",
    "departmentAccess": "Full",
    "accessDeviceAccess": "Read-Only",
    "phoneNumberExtensionAccess": "Read-Only",
    "callingLineIdNumberAccess": "Read-Only",
    "serviceAccess": "Read-Only",
    "servicePackAccess": "None",
    "sessionAdmissionControlAccess": "None",
    "webBrandingAccess": "None",
    "officeZoneAccess": "Read-Only",
    "communicationBarringAccess": "Read-Only",
    "networkPolicyAccess": "Full",
    "numberActivationAccess": "None",
    "dialableCallerIDAccess": "None",
}

for admin in administrators:
    gen_password = my_api.password_generate.get_password_generate(
        service_provider_id, group_id
    )["password"]
    try:
        my_api.administrators.post_service_provider_admin(
            service_provider_id=service_provider_id,
            user_id=admin,
            password=gen_password,
            first_name="",
            last_name="",
            language=language,
            admin_type=admin_type,
        )
        my_api.administrators.put_service_provider_admin_policies(
            user_id=admin, policy_config=policy
        )
        print(f"Built admin: {admin}")
    except Exception:
        print(f"Failed to build admin: {admin}")

```
{% endcode %}