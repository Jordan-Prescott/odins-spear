# User Registration

This script is to pull User Id's, Registered Device Names, and Registration status from every user within a group. This is helpful to diagnose issues, and identify devices that have gone offline.

This script uses the below methods to achieve this:

```python
api.registration.get_bulk_user_registration()
```

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise where group is hosted.&#x20;
* group\_id (str): Target Group you would like to pull the registration of users for.&#x20;

### Return

* dict: Returns a dictionary output containing User ID, Device Name, and Registration Status&#x20;

### How To Use:

{% hint style="info" %}
This method requires keyword arguments i.e. group_id="group_id"
{% endhint %}

{% code overflow="wrap" %}
```python
from odins_spear import API, Scripter

my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

assistant = Scripter(my_api)

assistant.user_registration(
    service_provider_id="ServiceProviderID", 
    group_id="GroupID", 
)
```
{% endcode %}

### Formatted Output

```json
{
   "User1@odin.com":{
      "registration":{
         "Device123":{
            "registered":true
         }
      }
   },
   "User2@odin.com":{
      "registration":{
         
      }
   },
   "User3@odin.com":{
      "registration":{
         "DeskPhone":{
            "registered":true
         },
         "HomePhone":{
            "registered":true
         }
      }
   }
}
```
