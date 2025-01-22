# Service Pack Audit

A stripped down audit of the service packs assigned within the group. This only shows the service packs assigned and total count.

{% hint style="info" %}
```
Scripter - Group Audit shows further details such as users assigned. 
```
{% endhint %}

{% content-ref url="contact.md" %}
[Group Audit](features/scripter/group-audit.md)
{% endcontent-ref %}

### How To Use:

```python
from odins_spear import API

my_api = API("base_url", "username", "ENV-PASSWORD")
my_api.authenticate()

#CHANGE ME
service_provider_id = 'ServiceProviderId'
group_id = 'group_id'

service_report = api.services.get_group_services(group_id, service_provider_id)
assigned_service_pack_services = []

for sps in service_report["servicePackServices"]:
   if sps["usage"] > 0:
      del sps["authorized"]
      del sps["assigned"]
      del sps["limited"]
      del sps["allowed"]
      del sps["serviceName"]
      del sps["quantity"]
      del sps["alias"]

      assigned_service_pack_services.append(sps)

print(service_report)

```

### Example returned data (formatted):

```json
   [
      {
         "servicePackName":"Admin-A",
         "usage":21,
         "description":null
      },
      {
         "servicePackName":"Unity-R",
         "usage":4,
         "description":null
      },
      {
         "servicePackName":"WBX-B",
         "usage":45,
         "description":"Webex for BroadWorks Basic"
      }
   ]
```
