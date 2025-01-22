
# Constants Documentation

The `constants.py` module contains predefined lists of filters, filter types, group services, and user services. These constants are designed to standardise and simplify usage.

## **Available Constants**

### **Supported Filters**
A list of supported filter attributes for searching entities:
```python
supported_filters = [
    "macAddress",
    "lastName",
    "firstName",
    "dn",
    "emailAddress",
    "userId",
    "extension",
]
```

### **Supported Filter Types**
Defines the operations that can be applied to filters:
```python
supported_filter_types = [
    "contains",
    "startsWith",
    "endsWith",
    "equals",
]
```

### **Group Services**
A list of group-level services in BroadWorks:
```python
group_services = [
    "Account/Authorization Codes",
    "Auto Attendant - Basic",
    "Auto Attendant - Standard",
    "Call Park",
    "Call Pickup",
    "Emergency Zones",
    "Group Paging",
    "Hunt Group",
    "Incoming Calling Plan",
    "Meet-Me Conferencing",
    "Music On Hold",
    "Outgoing Calling Plan",
    "Trunk Group",
    "Voice Messaging Group",
    "VoiceXML",
]
```

### **User Services**
A list of user-level services in BroadWorks:
```python
user_services = [
    "Advice Of Charge",
    "Alternate Numbers",
    "Anonymous Call Rejection",
    "Authentication",
    "Automatic Callback",
    "Automatic Hold/Retrieve",
    "Barge-in Exempt",
    "Basic Call Logs",
    "BroadWorks Agent",
    ...
    "Zone Calling Restrictions",
]
```

## **Usage Example**
To use these constants, import them from the `constants` module:
```python
from odins_spear.utils.constants import supported_filters, user_services

# Example: Using the supported_filters list
print(supported_filters)
```
