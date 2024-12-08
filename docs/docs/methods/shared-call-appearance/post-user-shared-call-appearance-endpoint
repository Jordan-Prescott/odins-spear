# POST - User Shared Call Appearance Endpoint

Creates a new Shared Call Apprance (SCA) on a single user.

### Parameters&#x20;

* user_id (str): Target user id of user to create SCA on.
* line_port (str): Line port to be assigned to the new SCA.
* device_name (str): Device to add for SCA from available devices.

### Returns

* Dict: New SCA details applied to user. 

### How To Use:

```python
from odins_spear import API

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

# updating a users service pack
my_api.shared_call_appearance.post_user_shared_call_appearance_endpoint(
    "userId@domain.com",
    "userId_webex_mobile@domain.com",
    "webex mobile user x"
)
```
