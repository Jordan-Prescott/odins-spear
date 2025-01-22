# AA, CC, HG Audit

This script pulls the services assigned to Auto Attendants, Call Centres, and Hunt Groups. 

{% hint style="info" %}
```
Only services are applied to these entities no service packs
```
{% endhint %}


### How To Use:

```python
from odins_spear import API

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

audit = {"auto_attendants": [], "call_centers": [], "hunt_groups": []}

for entity_type, api_method in [
   ("auto_attendants", api.auto_attendants.get_auto_attendants),
   ("call_centers", api.call_centers.get_group_call_centers),
   ("hunt_groups", api.hunt_groups.get_group_hunt_groups),
]:
   entities = api_method(service_provider_id, group_id)
   for entity in tqdm(
      entities, desc=f"Analysing {entity_type.replace("_", " ").title()}"
   ):
      services = api.services.get_user_services_assigned(entity["serviceUserId"])
      return_data[entity_type].append(
            {
               "serviceUserId": entity["serviceUserId"],
               "type": entity.get("type", "None"),
               "services": services.get("userServices", []),
            }
      )

print(audit)
```

### Example returned data (formatted):

```json
{
   "autoAttendants":[
      {
         "serviceUserId":"basic_aa@domain.com",
         "type":"Basic",
         "services":[
            
         ]
      }
   ],
   "callCenters":[
      {
         "serviceUserId":"basic_cc@domain.com",
         "type":"Basic",
         "services":[
            
         ]
      }
   ],
   "huntGroups":[
      {
         "serviceUserId":"EVA_External_HG@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_Internal_HG@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_External_HG_SB@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"EVA_Internal_HG_SB@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"testing@domain.com",
         "services":[
            
         ]
      },
      {
         "serviceUserId":"odin.mock.hg.2@domain.com",
         "services":[
            
         ]
      }
   ]
}

```
