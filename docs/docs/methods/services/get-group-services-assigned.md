# GET - Group Services Assigned

Fetch all services assigned within a group.

### Parameters&#x20;

*    group\_id (str): GroupID being targeted
*    service_provider\_id (str): Service provider/Enterprise ID where the group is located.

### Returns

* List: A list with the service names of all assigned services within the group.

### How To Use:

```python
my_api.services.get_group_services_assigned(
    "groupId",
    "serviceProviderId",
)
```
{% endcode %} 



### Example Data Returned (Formatted)
```json
[
    "Alternate Numbers",
    "Anonymous Call Rejection",
    "Authentication",
    "PBX Integration",
    "Personal Assistant",
    "Physical Location",
    "Polycom Phone Services",
    "Pre-alerting Announcement",
    "Preferred Carrier User",
    "Prepaid",
    "Priority Alert",
    "Privacy",
    "Push to Talk",
    "Remote Office",
    "Resource Priority",
    "Route List",
    "Security Classification",
    "Selective Call Acceptance",
    "Selective Call Rejection",
    "Sequential Ring",
    "Shared Call Appearance",
    "Silent Alerting",
    "Simultaneous Ring Family",
    "Simultaneous Ring Personal",
    "Speed Dial 100",
    "Speed Dial 8",
    "Terminating Alternate Trunk Identity",
    "Third-Party MWI Control",
    "Third-Party Voice Mail Support",
    "Three-Way Call",
    "Trunk Group",
    "Two-Stage Dialing",
    "Video Add-On",
    "Video On Hold User",
    "Virtual On-Net Enterprise Extensions",
    "Voice Messaging Group",
    "Voice Messaging User",
    "Voice Messaging User - Video",
    "Voice Portal Calling",
    "Zone Calling Restrictions"
]
```
```
