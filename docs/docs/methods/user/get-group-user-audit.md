# GET - Group User Audit 

Returns a detailed audit of all users inside a group.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* group_id (str): Target Group ID with users

### Returns

* Dict: Audit of users in specified group

### How To Use:

```python
my_api.users.get_group_user_audit(
    "service_provider_id",
    "group_id"
)
```

### Example Data Returned (Formatted)

```python
{
  "data": [
    {
      "users": [
        {
          "serviceProviderId": "ent.odin",
          "groupId": "grp.odin",
          "userId": "4003@parkbenchsolutions.com",
          "user": {
            "serviceProviderId": "ent.odin",
            "groupId": "grp.odin",
            "lastName": 4003,
            "firstName": 4003,
            "callingLineIdLastName": 4003,
            "callingLineIdFirstName": 4003,
            "hiraganaLastName": 4003,
            "hiraganaFirstName": 4003,
            "phoneNumber": "8135551003",
            "extension": "1003",
            "language": "English",
            "timeZone": "America/New_York",
            "timeZoneDisplayName": "(GMT-04:00) (US) Eastern Time",
            "defaultAlias": "4003@parkbenchsolutions.com",
            "accessDeviceEndpoint": {
              "accessDevice": {
                "deviceType": "Polycom IP550",
                "protocol": "SIP 2.0",
                "macAddress": 222222222222,
                "numberOfPorts": {
                  "quantity": "4"
                },
                "numberOfAssignedPorts": 1,
                "status": "Online",
                "configurationMode": "Default",
                "transportProtocol": "UDP",
                "useCustomUserNamePassword": false,
                "deviceName": "4003-polycom550",
                "deviceLevel": "Group",
                "accessDeviceCredentials": {
                  "userName": null
                },
                "serviceProviderId": "ent.odin",
                "groupId": "grp.odin",
                "tags": [],
                "relatedServices": []
              },
              "linePort": "4003@parkbenchsolutions.com",
              "staticRegistrationCapable": "false",
              "useDomain": "true",
              "supportVisualDeviceManagement": "false",
              "contacts": []
            },
            "countryCode": "1",
            "userId": "4003@parkbenchsolutions.com",
            "callingLineIdPhoneNumber": "",
            "domain": "parkbenchsolutions.com",
            "endpointType": "accessDeviceEndpoint",
            "aliases": [
              "4003-alias-1@parkbenchsolutions.com",
              "4003-alias-2@parkbenchsolutions.com",
              "4003-alias-3@parkbenchsolutions.com"
            ],
            "trunkAddressing": {
              "trunkGroupDeviceEndpoint": {
                "contacts": []
              }
            },
            "isEnterprise": true,
            "passwordExpiresDays": 2147483647
          },
          "outgoingCallingPlans": {
            "outgoingCallingPlanAuthorizationCode": {
              "settings": {
                "useCustomSettings": true,
                "userId": "4003@parkbenchsolutions.com",
                "serviceProviderId": "ent.odin",
                "groupId": "grp.odin",
                "isEnterprise": true
              },
              "codes": [
                {
                  "code": "1001",
                  "description": "1001"
                }
              ],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanCallMeNow": {
              "useCustomSettings": true,
              "userPermissions": {
                "group": true,
                "local": true,
                "tollFree": false,
                "toll": true,
                "international": true,
                "operatorAssisted": false,
                "chargeableDirectoryAssisted": false,
                "specialServicesI": false,
                "specialServicesII": false,
                "premiumServicesI": false,
                "premiumServicesII": false,
                "casual": false,
                "urlDialing": false,
                "unknown": false
              },
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanDigitPlanCallMeNow": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanDigitPlanOriginating": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanDigitPlanRedirecting": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanOriginating": {
              "useCustomSettings": true,
              "userPermissions": {
                "group": "Allow",
                "local": "Allow",
                "tollFree": "Allow",
                "toll": "Allow",
                "international": "Disallow",
                "operatorAssisted": "Allow",
                "chargeableDirectoryAssisted": "Allow",
                "specialServicesI": "Allow",
                "specialServicesII": "Allow",
                "premiumServicesI": "Disallow",
                "premiumServicesII": "Disallow",
                "casual": "Disallow",
                "urlDialing": "Allow",
                "unknown": "Allow"
              },
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanRedirected": {
              "useCustomSettings": true,
              "userPermissions": {
                "outsideGroup": true
              },
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanRedirecting": {
              "useCustomSettings": true,
              "userPermissions": {
                "group": true,
                "local": true,
                "tollFree": true,
                "toll": true,
                "international": true,
                "operatorAssisted": true,
                "chargeableDirectoryAssisted": true,
                "specialServicesI": true,
                "specialServicesII": true,
                "premiumServicesI": false,
                "premiumServicesII": false,
                "casual": false,
                "urlDialing": true,
                "unknown": true
              },
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanTransferNumbers": {
              "useCustomSettings": true,
              "userNumbers": {},
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanPinholeDigitPlanCallMeNow": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanPinholeDigitPlanOriginating": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "outgoingCallingPlanPinholeDigitPlanRedirecting": {
              "useCustomSettings": true,
              "userPermissions": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            }
          },
          "assignedServices": {
            "userId": "4003@parkbenchsolutions.com",
            "userServices": [
              {
                "serviceName": "Alternate Numbers"
              },
              {
                "serviceName": "Anonymous Call Rejection",
                "isActive": false
              },
              {
                "serviceName": "Authentication"
              },
              {
                "serviceName": "Basic Call Logs"
              },
              {
                "serviceName": "Busy Lamp Field"
              },
              {
                "serviceName": "Call Center - Basic"
              },
              {
                "serviceName": "Call Forwarding Always",
                "isActive": true
              },
              {
                "serviceName": "Call Forwarding Busy",
                "isActive": false
              },
              {
                "serviceName": "Call Forwarding No Answer",
                "isActive": false
              },
              {
                "serviceName": "Call Forwarding Not Reachable",
                "isActive": false
              },
              {
                "serviceName": "Call Forwarding Selective",
                "isActive": false
              },
              {
                "serviceName": "Client License 4"
              },
              {
                "serviceName": "CommPilot Express",
                "isActive": true
              },
              {
                "serviceName": "Fax Messaging",
                "isActive": true
              },
              {
                "serviceName": "Flexible Seating Guest",
                "isActive": false
              },
              {
                "serviceName": "Intercept User",
                "isActive": false
              },
              {
                "serviceName": "Selective Call Rejection",
                "isActive": true
              },
              {
                "serviceName": "Shared Call Appearance"
              },
              {
                "serviceName": "Speed Dial 100"
              },
              {
                "serviceName": "Speed Dial 8"
              },
              {
                "serviceName": "Virtual On-Net Enterprise Extensions"
              },
              {
                "serviceName": "Voice Portal Calling",
                "isActive": true
              },
              {
                "serviceName": "Zone Calling Restrictions"
              }
            ],
            "groupServices": [
              {
                "serviceName": "Music On Hold",
                "isActive": true
              }
            ],
            "serviceProviderId": "ent.odin",
            "groupId": "grp.odin",
            "isEnterprise": true
          },
          "serviceAssignment": {
            "userId": "4003@parkbenchsolutions.com",
            "userServices": [
              {
                "serviceName": "Anonymous Call Rejection",
                "assigned": false,
                "tags": [],
                "alias": "Anonymous Call Rejection"
              },
              {
                "serviceName": "Authentication",
                "assigned": true,
                "tags": [],
                "alias": "Authentication"
              },
              {
                "serviceName": "Call Forwarding Always",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding Always"
              },
              {
                "serviceName": "Call Forwarding Busy",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding Busy"
              },
              {
                "serviceName": "Call Forwarding No Answer",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding No Answer"
              },
              {
                "serviceName": "Call Notify",
                "assigned": false,
                "tags": [],
                "alias": "Call Notify"
              },
              {
                "serviceName": "Calling Line ID Delivery Blocking",
                "assigned": false,
                "tags": [],
                "alias": "Calling Line ID Delivery Blocking"
              },
              {
                "serviceName": "CommPilot Express",
                "assigned": true,
                "tags": [],
                "alias": "CommPilot Express"
              },
              {
                "serviceName": "CommPilot Call Manager",
                "assigned": false,
                "tags": [],
                "alias": "CommPilot Call Manager"
              },
              {
                "serviceName": "Do Not Disturb",
                "assigned": false,
                "tags": [],
                "alias": "Do Not Disturb"
              },
              {
                "serviceName": "Intercept User",
                "assigned": true,
                "tags": [],
                "alias": "Intercept User"
              },
              {
                "serviceName": "Last Number Redial",
                "assigned": false,
                "tags": [],
                "alias": "Last Number Redial"
              },
              {
                "serviceName": "Outlook Integration",
                "assigned": false,
                "tags": [],
                "alias": "Outlook Integration"
              },
              {
                "serviceName": "Priority Alert",
                "assigned": false,
                "tags": [],
                "alias": "Priority Alert"
              },
              {
                "serviceName": "Call Return",
                "assigned": false,
                "tags": [],
                "alias": "Call Return"
              },
              {
                "serviceName": "Remote Office",
                "assigned": false,
                "tags": [],
                "alias": "Remote Office"
              },
              {
                "serviceName": "Selective Call Acceptance",
                "assigned": false,
                "tags": [],
                "alias": "Selective Call Acceptance"
              },
              {
                "serviceName": "Call Forwarding Selective",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding Selective"
              },
              {
                "serviceName": "Selective Call Rejection",
                "assigned": true,
                "tags": [],
                "alias": "Selective Call Rejection"
              },
              {
                "serviceName": "Service Scripts User",
                "assigned": false,
                "tags": [],
                "alias": "Service Scripts User"
              },
              {
                "serviceName": "Simultaneous Ring Personal",
                "assigned": false,
                "tags": [],
                "alias": "Simultaneous Ring Personal"
              },
              {
                "serviceName": "Voice Messaging User",
                "assigned": false,
                "tags": [],
                "alias": "Voice Messaging User"
              },
              {
                "serviceName": "Alternate Numbers",
                "assigned": true,
                "tags": [],
                "alias": "Alternate Numbers"
              },
              {
                "serviceName": "Shared Call Appearance",
                "assigned": true,
                "tags": [
                  "UC-One"
                ],
                "alias": "Shared Call Appearance"
              },
              {
                "serviceName": "Speed Dial 8",
                "assigned": true,
                "tags": [],
                "alias": "Speed Dial 8"
              },
              {
                "serviceName": "Customer Originated Trace",
                "assigned": false,
                "tags": [],
                "alias": "Customer Originated Trace"
              },
              {
                "serviceName": "Attendant Console",
                "assigned": false,
                "tags": [],
                "alias": "Attendant Console"
              },
              {
                "serviceName": "Third-Party MWI Control",
                "assigned": false,
                "tags": [],
                "alias": "Third-Party MWI Control"
              },
              {
                "serviceName": "Client Call Control",
                "assigned": false,
                "tags": [],
                "alias": "Client Call Control"
              },
              {
                "serviceName": "Shared Call Appearance 5",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "Shared Call Appearance 5"
              },
              {
                "serviceName": "Shared Call Appearance 10",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 10"
              },
              {
                "serviceName": "Shared Call Appearance 15",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 15"
              },
              {
                "serviceName": "Shared Call Appearance 20",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 20"
              },
              {
                "serviceName": "Shared Call Appearance 25",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 25"
              },
              {
                "serviceName": "Shared Call Appearance 30",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 30"
              },
              {
                "serviceName": "Shared Call Appearance 35",
                "assigned": false,
                "tags": [],
                "alias": "Shared Call Appearance 35"
              },
              {
                "serviceName": "Calling Name Retrieval",
                "assigned": false,
                "tags": [],
                "alias": "Calling Name Retrieval"
              },
              {
                "serviceName": "Flash Call Hold",
                "assigned": false,
                "tags": [],
                "alias": "Flash Call Hold"
              },
              {
                "serviceName": "Speed Dial 100",
                "assigned": true,
                "tags": [],
                "alias": "Speed Dial 100"
              },
              {
                "serviceName": "Directed Call Pickup",
                "assigned": false,
                "tags": [],
                "alias": "Directed Call Pickup"
              },
              {
                "serviceName": "Third-Party Voice Mail Support",
                "assigned": false,
                "tags": [],
                "alias": "Third-Party Voice Mail Support"
              },
              {
                "serviceName": "Directed Call Pickup with Barge-in",
                "assigned": false,
                "tags": [],
                "alias": "Directed Call Pickup with Barge-in"
              },
              {
                "serviceName": "Voice Portal Calling",
                "assigned": true,
                "tags": [],
                "alias": "Voice Portal Calling"
              },
              {
                "serviceName": "External Calling Line ID Delivery",
                "assigned": false,
                "tags": [],
                "alias": "External Calling Line ID Delivery"
              },
              {
                "serviceName": "Internal Calling Line ID Delivery",
                "assigned": false,
                "tags": [],
                "alias": "Internal Calling Line ID Delivery"
              },
              {
                "serviceName": "Automatic Callback",
                "assigned": false,
                "tags": [],
                "alias": "Automatic Callback"
              },
              {
                "serviceName": "Call Waiting",
                "assigned": false,
                "tags": [],
                "alias": "Call Waiting"
              },
              {
                "serviceName": "Calling Line ID Blocking Override",
                "assigned": false,
                "tags": [],
                "alias": "Calling Line ID Blocking Override"
              },
              {
                "serviceName": "Calling Party Category",
                "assigned": false,
                "tags": [],
                "alias": "Calling Party Category"
              },
              {
                "serviceName": "Barge-in Exempt",
                "assigned": false,
                "tags": [],
                "alias": "Barge-in Exempt"
              },
              {
                "serviceName": "Video Add-On",
                "assigned": false,
                "tags": [],
                "alias": "Video Add-On"
              },
              {
                "serviceName": "Malicious Call Trace",
                "assigned": false,
                "tags": [],
                "alias": "Malicious Call Trace"
              },
              {
                "serviceName": "Preferred Carrier User",
                "assigned": false,
                "tags": [],
                "alias": "Preferred Carrier User"
              },
              {
                "serviceName": "Push to Talk",
                "assigned": false,
                "tags": [],
                "alias": "Push to Talk"
              },
              {
                "serviceName": "Basic Call Logs",
                "assigned": true,
                "tags": [],
                "alias": "Basic Call Logs"
              },
              {
                "serviceName": "Enhanced Call Logs",
                "assigned": false,
                "tags": [],
                "alias": "Enhanced Call Logs"
              },
              {
                "serviceName": "Hoteling Host",
                "assigned": false,
                "tags": [],
                "alias": "Hoteling Host"
              },
              {
                "serviceName": "Hoteling Guest",
                "assigned": false,
                "tags": [],
                "alias": "Hoteling Guest"
              },
              {
                "serviceName": "Voice Messaging User - Video",
                "assigned": false,
                "tags": [],
                "alias": "Voice Messaging User - Video"
              },
              {
                "serviceName": "Diversion Inhibitor",
                "assigned": false,
                "tags": [],
                "alias": "Diversion Inhibitor"
              },
              {
                "serviceName": "Multiple Call Arrangement",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "Multiple Call Arrangement"
              },
              {
                "serviceName": "Custom Ringback User",
                "assigned": false,
                "tags": [],
                "alias": "Custom Ringback User"
              },
              {
                "serviceName": "Custom Ringback User - Video",
                "assigned": false,
                "tags": [],
                "alias": "Custom Ringback User - Video"
              },
              {
                "serviceName": "Automatic Hold/Retrieve",
                "assigned": false,
                "tags": [],
                "alias": "Automatic Hold/Retrieve"
              },
              {
                "serviceName": "Busy Lamp Field",
                "assigned": true,
                "tags": [],
                "alias": "Busy Lamp Field"
              },
              {
                "serviceName": "Three-Way Call",
                "assigned": false,
                "tags": [],
                "alias": "Three-Way Call"
              },
              {
                "serviceName": "Call Transfer",
                "assigned": false,
                "tags": [],
                "alias": "Call Transfer"
              },
              {
                "serviceName": "Privacy",
                "assigned": false,
                "tags": [],
                "alias": "Privacy"
              },
              {
                "serviceName": "Fax Messaging",
                "assigned": true,
                "tags": [],
                "alias": "Fax Messaging"
              },
              {
                "serviceName": "Physical Location",
                "assigned": false,
                "tags": [],
                "alias": "Physical Location"
              },
              {
                "serviceName": "Charge Number",
                "assigned": false,
                "tags": [],
                "alias": "Charge Number"
              },
              {
                "serviceName": "BroadWorks Supervisor",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Supervisor"
              },
              {
                "serviceName": "BroadWorks Agent",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Agent"
              },
              {
                "serviceName": "N-Way Call",
                "assigned": false,
                "tags": [],
                "alias": "N-Way Call"
              },
              {
                "serviceName": "Two-Stage Dialing",
                "assigned": false,
                "tags": [],
                "alias": "Two-Stage Dialing"
              },
              {
                "serviceName": "Call Forwarding Not Reachable",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding Not Reachable"
              },
              {
                "serviceName": "MWI Delivery to Mobile Endpoint",
                "assigned": false,
                "tags": [],
                "alias": "MWI Delivery to Mobile Endpoint"
              },
              {
                "serviceName": "BroadWorks Receptionist - Small Business",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Receptionist - Small Business"
              },
              {
                "serviceName": "BroadWorks Receptionist - Office",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Receptionist - Office"
              },
              {
                "serviceName": "External Custom Ringback",
                "assigned": false,
                "tags": [],
                "alias": "External Custom Ringback"
              },
              {
                "serviceName": "In-Call Service Activation",
                "assigned": false,
                "tags": [],
                "alias": "In-Call Service Activation"
              },
              {
                "serviceName": "Connected Line Identification Presentation",
                "assigned": false,
                "tags": [],
                "alias": "Connected Line Identification Presentation"
              },
              {
                "serviceName": "Connected Line Identification Restriction",
                "assigned": false,
                "tags": [],
                "alias": "Connected Line Identification Restriction"
              },
              {
                "serviceName": "BroadWorks Anywhere",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Anywhere"
              },
              {
                "serviceName": "Zone Calling Restrictions",
                "assigned": true,
                "tags": [],
                "alias": "Zone Calling Restrictions"
              },
              {
                "serviceName": "Polycom Phone Services",
                "assigned": false,
                "tags": [],
                "alias": "Polycom Phone Services"
              },
              {
                "serviceName": "Custom Ringback User - Call Waiting",
                "assigned": false,
                "tags": [],
                "alias": "Custom Ringback User - Call Waiting"
              },
              {
                "serviceName": "Music On Hold User",
                "assigned": false,
                "tags": [],
                "alias": "Music On Hold User"
              },
              {
                "serviceName": "Video On Hold User",
                "assigned": false,
                "tags": [],
                "alias": "Video On Hold User"
              },
              {
                "serviceName": "Advice Of Charge",
                "assigned": false,
                "tags": [],
                "alias": "Advice Of Charge"
              },
              {
                "serviceName": "Prepaid",
                "assigned": false,
                "tags": [],
                "alias": "Prepaid"
              },
              {
                "serviceName": "Call Center - Basic",
                "assigned": false,
                "tags": [],
                "alias": "Call Center - Basic"
              },
              {
                "serviceName": "Call Center - Standard",
                "assigned": false,
                "tags": [],
                "alias": "Call Center - Standard"
              },
              {
                "serviceName": "Call Center - Premium",
                "assigned": false,
                "tags": [],
                "alias": "Call Center - Premium"
              },
              {
                "serviceName": "Communication Barring User-Control",
                "assigned": false,
                "tags": [],
                "alias": "Communication Barring User-Control"
              },
              {
                "serviceName": "Classmark",
                "assigned": false,
                "tags": [],
                "alias": "Classmark"
              },
              {
                "serviceName": "Calling Name Delivery",
                "assigned": false,
                "tags": [],
                "alias": "Calling Name Delivery"
              },
              {
                "serviceName": "Calling Number Delivery",
                "assigned": false,
                "tags": [],
                "alias": "Calling Number Delivery"
              },
              {
                "serviceName": "Virtual On-Net Enterprise Extensions",
                "assigned": true,
                "tags": [],
                "alias": "Virtual On-Net Enterprise Extensions"
              },
              {
                "serviceName": "Office Communicator Tab",
                "assigned": false,
                "tags": [],
                "alias": "Office Communicator Tab"
              },
              {
                "serviceName": "Pre-alerting Announcement",
                "assigned": false,
                "tags": [],
                "alias": "Pre-alerting Announcement"
              },
              {
                "serviceName": "Call Center Monitoring",
                "assigned": false,
                "tags": [],
                "alias": "Call Center Monitoring"
              },
              {
                "serviceName": "Location-Based Calling Restrictions",
                "assigned": false,
                "tags": [],
                "alias": "Location-Based Calling Restrictions"
              },
              {
                "serviceName": "BroadWorks Mobility",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Mobility"
              },
              {
                "serviceName": "Call Me Now",
                "assigned": false,
                "tags": [],
                "alias": "Call Me Now"
              },
              {
                "serviceName": "Call Recording",
                "assigned": false,
                "tags": [],
                "alias": "Call Recording"
              },
              {
                "serviceName": "BroadWorks Connector for Lotus Sametime",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Connector for Lotus Sametime"
              },
              {
                "serviceName": "Integrated IMP",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "Integrated IMP"
              },
              {
                "serviceName": "Group Night Forwarding",
                "assigned": false,
                "tags": [],
                "alias": "Group Night Forwarding"
              },
              {
                "serviceName": "BroadTouch Business Communicator Desktop",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Desktop"
              },
              {
                "serviceName": "BroadTouch Business Communicator Desktop - Audio",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Desktop - Audio"
              },
              {
                "serviceName": "BroadTouch Business Communicator Mobile",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Mobile"
              },
              {
                "serviceName": "BroadTouch Business Communicator Mobile - Audio",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Mobile - Audio"
              },
              {
                "serviceName": "BroadTouch Business Communicator Tablet",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Tablet"
              },
              {
                "serviceName": "BroadTouch Business Communicator Tablet - Audio",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch Business Communicator Tablet - Audio"
              },
              {
                "serviceName": "BroadTouch Business Communicator Tablet - Video",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "BroadTouch Business Communicator Tablet - Video"
              },
              {
                "serviceName": "Executive",
                "assigned": false,
                "tags": [],
                "alias": "Executive"
              },
              {
                "serviceName": "Executive-Assistant",
                "assigned": false,
                "tags": [],
                "alias": "Executive-Assistant"
              },
              {
                "serviceName": "Client License 3",
                "assigned": false,
                "tags": [],
                "alias": "BroadWorks Assistant - Enterprise"
              },
              {
                "serviceName": "Client License 4",
                "assigned": true,
                "tags": [],
                "alias": "BroadWorks Receptionist - Enterprise"
              },
              {
                "serviceName": "Client License 15",
                "assigned": false,
                "tags": [],
                "alias": "Client License 15"
              },
              {
                "serviceName": "Client License 16",
                "assigned": false,
                "tags": [],
                "alias": "Client License 16"
              },
              {
                "serviceName": "Client License 17",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "BroadTouch Business Communicator Mobile - Video"
              },
              {
                "serviceName": "Client License 18",
                "assigned": false,
                "tags": [
                  "UC-One"
                ],
                "alias": "BroadTouch Business Communicator Destop - Video"
              },
              {
                "serviceName": "Client License 19",
                "assigned": false,
                "tags": [],
                "alias": "BroadTouch MobileLink"
              },
              {
                "serviceName": "Security Classification",
                "assigned": false,
                "tags": [],
                "alias": "Security Classification"
              },
              {
                "serviceName": "Flexible Seating Guest",
                "assigned": true,
                "tags": [],
                "alias": "Flexible Seating Guest"
              },
              {
                "serviceName": "Personal Assistant",
                "assigned": false,
                "tags": [],
                "alias": "Personal Assistant"
              },
              {
                "serviceName": "Route List",
                "assigned": false,
                "tags": [],
                "alias": "Route List"
              },
              {
                "serviceName": "Collaborate - Audio",
                "assigned": false,
                "tags": [],
                "alias": "Collaborate - Audio"
              },
              {
                "serviceName": "Collaborate - Video",
                "assigned": false,
                "tags": [],
                "alias": "Collaborate - Video"
              },
              {
                "serviceName": "Collaborate - Sharing",
                "assigned": false,
                "tags": [],
                "alias": "Collaborate - Sharing"
              },
              {
                "serviceName": "Call Forwarding Always Secondary",
                "assigned": false,
                "tags": [],
                "alias": "Call Forwarding Always Secondary"
              },
              {
                "serviceName": "Silent Alerting",
                "assigned": false,
                "tags": [],
                "alias": "Silent Alerting"
              },
              {
                "serviceName": "Conference Room",
                "assigned": false,
                "tags": [],
                "alias": "Conference Room"
              },
              {
                "serviceName": "Sequential Ring",
                "assigned": false,
                "tags": [],
                "alias": "Sequential Ring"
              },
              {
                "serviceName": "Number Portability Announcement",
                "assigned": false,
                "tags": [],
                "alias": "Number Portability Announcement"
              },
              {
                "serviceName": "Direct Route",
                "assigned": false,
                "tags": [],
                "alias": "Direct Route"
              },
              {
                "serviceName": "Terminating Alternate Trunk Identity",
                "assigned": false,
                "tags": [],
                "alias": "Terminating Alternate Trunk Identity"
              }
            ],
            "servicePackServices": [
              {
                "assigned": true,
                "description": "Standard",
                "serviceName": "Standard",
                "alias": "Standard"
              },
              {
                "assigned": false,
                "description": "Premium",
                "serviceName": "Premium",
                "alias": "Premium"
              },
              {
                "assigned": false,
                "description": "Basic",
                "serviceName": "Basic",
                "alias": "Basic"
              }
            ],
            "serviceProviderId": "ent.odin",
            "groupId": "grp.odin",
            "isEnterprise": true
          },
          "serviceSettings": {
            "Alternate Numbers": {
              "userId": "4003@parkbenchsolutions.com",
              "distinctiveRing": true,
              "alternateEntries": [
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 1
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 2
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 3
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 4
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 5
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 6
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 7
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 8
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 9
                },
                {
                  "phoneNumber": null,
                  "extension": null,
                  "ringPattern": null,
                  "alternateEntryId": 10
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Anonymous Call Rejection": {
              "isActive": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Busy Lamp Field": {
              "enableCallParkNotification": true,
              "users": [],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Call Forwarding Always": {
              "isActive": true,
              "forwardToPhoneNumber": 6500,
              "isRingSplashActive": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Call Forwarding Busy": {
              "isActive": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Call Forwarding No Answer": {
              "isActive": false,
              "numberOfRings": 3,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Call Forwarding Not Reachable": {
              "isActive": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Call Forwarding Selective": {
              "isActive": false,
              "playRingReminder": false,
              "userId": "4003@parkbenchsolutions.com",
              "criteria": [],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "CommPilot Express": {
              "profile": "Available In Office",
              "availableInOffice": {
                "additionalPhoneNumberToRing": "1113334444",
                "busySetting": {
                  "action": "Transfer To Voice Mail"
                },
                "noAnswerSetting": {
                  "action": "Transfer To Voice Mail"
                }
              },
              "availableOutOfOffice": {
                "incomingCalls": {
                  "action": "Transfer To Voice Mail"
                },
                "incomingCallNotify": {
                  "sendEmail": "false"
                }
              },
              "busy": {
                "incomingCalls": {
                  "sendCallsToVoiceMailExceptExcludedNumbers": "false"
                },
                "voiceMailNotify": {
                  "sendEmail": "false"
                }
              },
              "unavailable": {
                "incomingCalls": {
                  "sendCallsToVoiceMailExceptExcludedNumbers": "false"
                },
                "voiceMailGreeting": "No Answer"
              },
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Fax Messaging": {
              "isActive": true,
              "phoneNumber": 8135551005,
              "extension": 1005,
              "userId": "4003@parkbenchsolutions.com",
              "aliases": [
                {
                  "alias": "4004@parkbenchsolutions.com",
                  "phoneNumber": "4004",
                  "domain": "parkbenchsolutions.com"
                },
                {
                  "alias": "4005@parkbenchsolutions.com",
                  "phoneNumber": "4005",
                  "domain": "parkbenchsolutions.com"
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Intercept User": {
              "isActive": false,
              "announcementSelection": "Default",
              "inboundCallMode": "Intercept All",
              "alternateBlockingAnnouncement": false,
              "exemptInboundMobilityCalls": true,
              "disableParallelRingingToNetworkLocations": true,
              "routeToVoiceMail": true,
              "playNewPhoneNumber": true,
              "newPhoneNumber": 123,
              "transferOnZeroToPhoneNumber": true,
              "transferPhoneNumber": 111111,
              "outboundCallMode": "Block All",
              "exemptOutboundMobilityCalls": true,
              "rerouteOutboundCalls": true,
              "outboundReroutePhoneNumber": 1234,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Selective Call Rejection": {
              "criteria": [
                {
                  "isActive": true,
                  "criteriaName": "Reject Calls",
                  "timeSchedule": "Every Day All Day",
                  "callsFrom": "12345,54321",
                  "blacklisted": true,
                  "holidaySchedule": "None",
                  "callsToType": null,
                  "callsToNumber": null,
                  "callsToExtension": null,
                  "fromDnCriteria": {
                    "fromDnCriteriaSelection": "Specified Only",
                    "includeAnonymousCallers": "false",
                    "includeUnavailableCallers": "false",
                    "phoneNumbers": [
                      "12345",
                      "54321"
                    ]
                  },
                  "private": false,
                  "userId": "4003@parkbenchsolutions.com"
                }
              ],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Shared Call Appearance": {
              "alertAllAppearancesForClickToDialCalls": true,
              "alertAllAppearancesForGroupPagingCalls": true,
              "maxAppearances": 2,
              "allowSCACallRetrieve": true,
              "enableMultipleCallArrangement": false,
              "multipleCallArrangementIsActive": false,
              "allowBridgingBetweenLocations": true,
              "bridgeWarningTone": "Barge-In",
              "enableCallParkNotification": true,
              "userId": "4003@parkbenchsolutions.com",
              "endpoints": [
                {
                  "deviceLevel": "Group",
                  "deviceName": "shared_4003_1",
                  "deviceType": "Polycom IP550",
                  "portNumber": null,
                  "deviceSupportVisualDeviceManagement": false,
                  "isActive": true,
                  "allowOrigination": true,
                  "allowTermination": true,
                  "macAddress": null,
                  "linePort": "shared_4003_1@parkbenchsolutions.com",
                  "sipContact": "sip:"
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Speed Dial 100": {
              "userId": "4003@parkbenchsolutions.com",
              "speedCodes": [
                {
                  "speedCode": "0",
                  "phoneNumber": "1111",
                  "description": "1111"
                },
                {
                  "speedCode": "1",
                  "phoneNumber": "2000",
                  "description": "2000"
                },
                {
                  "speedCode": "2",
                  "phoneNumber": "2222",
                  "description": "2222"
                },
                {
                  "speedCode": "15",
                  "phoneNumber": "1415",
                  "description": "1515"
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Speed Dial 8": {
              "userId": "4003@parkbenchsolutions.com",
              "speedCodes": [
                {
                  "speedCode": "2",
                  "phoneNumber": "222"
                },
                {
                  "speedCode": "3",
                  "phoneNumber": "333"
                },
                {
                  "speedCode": "4"
                },
                {
                  "speedCode": "5"
                },
                {
                  "speedCode": "6"
                },
                {
                  "speedCode": "7"
                },
                {
                  "speedCode": "8"
                },
                {
                  "speedCode": "9"
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Voice Portal Calling": {
              "isActive": true,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "Zone Calling Restrictions": {
              "homeZoneName": "Office",
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            }
          },
          "utilities": {
            "alternateUserId": {
              "users": [
                {
                  "userId": "userid12",
                  "alternate": true,
                  "description": "description1"
                },
                {
                  "userId": "userid45",
                  "alternate": true,
                  "description": "userid4"
                },
                {
                  "userId": "userTest",
                  "alternate": true,
                  "description": "userTest"
                }
              ],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "announcementFile": {
              "totalFileSize": 0,
              "maxFileSize": 1000,
              "userId": "4003@parkbenchsolutions.com",
              "announcementType": "",
              "announcements": []
            },
            "callPolicies": {
              "redirectedCallsCOLPPrivacy": "No Privacy",
              "callBeingForwardedResponseCallType": "Never",
              "callingLineIdentityForRedirectedCalls": "Originating Identity",
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "callProcessingPolicy": {
              "useUserCLIDSetting": false,
              "useUserMediaSetting": false,
              "useUserCallLimitsSetting": false,
              "useUserDCLIDSetting": false,
              "useMaxSimultaneousCalls": true,
              "maxSimultaneousCalls": 3,
              "useMaxSimultaneousVideoCalls": true,
              "maxSimultaneousVideoCalls": 1,
              "useMaxCallTimeForAnsweredCalls": true,
              "maxCallTimeForAnsweredCallsMinutes": 1440,
              "useMaxCallTimeForUnansweredCalls": false,
              "maxCallTimeForUnansweredCallsMinutes": 2,
              "mediaPolicySelection": "No Restrictions",
              "useMaxConcurrentRedirectedCalls": false,
              "maxConcurrentRedirectedCalls": 5,
              "useMaxFindMeFollowMeDepth": true,
              "maxFindMeFollowMeDepth": 3,
              "maxRedirectionDepth": 5,
              "useMaxConcurrentFindMeFollowMeInvocations": true,
              "maxConcurrentFindMeFollowMeInvocations": 3,
              "clidPolicy": "Use DN",
              "emergencyClidPolicy": "Use DN",
              "allowAlternateNumbersForRedirectingIdentity": true,
              "useGroupName": false,
              "blockCallingNameForExternalCalls": false,
              "enableDialableCallerID": false,
              "allowConfigurableCLIDForRedirectingIdentity": true,
              "allowDepartmentCLIDNameOverride": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "communicationBarring": {
              "useGroupSetting": false,
              "profileName": "test",
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "devicePolicies": {
              "lineMode": "Single User Private and Shared",
              "enableDeviceFeatureSynchronization": true,
              "enableDnd": false,
              "enableCallForwardingAlways": false,
              "enableCallForwardingBusy": false,
              "enableCallForwardingNoAnswer": false,
              "enableAcd": false,
              "enableExecutive": false,
              "enableExecutiveAssistant": false,
              "enableSecurityClassification": false,
              "enableCallRecording": false,
              "enableCallDecline": false,
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "featureAccessCode": {
              "userId": "4003@parkbenchsolutions.com",
              "featureAccessCodes": [
                {
                  "featureAccessCodeName": "Call Forwarding Not Reachable Deactivation",
                  "mainCode": "*95",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Bridge",
                  "mainCode": "*15",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Park",
                  "mainCode": "*68",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Group Call Park",
                  "mainCode": "#58",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Speed Dial 100",
                  "mainCode": "*75",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Busy Activation",
                  "mainCode": "*90",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Speed Dial 8",
                  "mainCode": "*74",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Anonymous Call Rejection Deactivation",
                  "mainCode": "*87",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Location Control Deactivation",
                  "mainCode": "*13",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "No Answer Timer",
                  "mainCode": "*610",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding No Answer Interrogation",
                  "mainCode": "*61*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Busy Interrogation",
                  "mainCode": "*67*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Per-Call Account Code",
                  "mainCode": "*71",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding No Answer Activation",
                  "mainCode": "*92",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Anonymous Call Rejection Interrogation",
                  "mainCode": "*52*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "EOCP Sustained Authorization Code Unlock",
                  "mainCode": "*47",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Always Activation",
                  "mainCode": "*72",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Not Reachable Interrogation",
                  "mainCode": "*63*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Hunt Group Busy Interrogation",
                  "mainCode": "#53",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding No Answer Deactivation",
                  "mainCode": "*93",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Selective Call Forwarding Activation",
                  "mainCode": "#76",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Selective Call Rejection Interrogation",
                  "mainCode": "*51*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Anonymous Call Rejection Activation",
                  "mainCode": "*77",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Always Interrogation",
                  "mainCode": "*21*",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Hunt Group Busy Deactivation",
                  "mainCode": "#52",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Retrieve",
                  "mainCode": "*11",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "EOCP Sustained Authorization Code Lock",
                  "mainCode": "*37",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Hunt Group Busy Activation",
                  "mainCode": "#51",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Location Control Activation",
                  "mainCode": "*12",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Selective Call Forwarding Deactivation",
                  "mainCode": "#77",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Voice Portal Access",
                  "mainCode": "*62",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Park Retrieve",
                  "mainCode": "*88",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Push Notification Retrieval",
                  "mainCode": "#0322",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Music On Hold Per-Call Deactivation",
                  "mainCode": "*60",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Always Deactivation",
                  "mainCode": "*73",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Pickup",
                  "mainCode": "*98",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Busy Deactivation",
                  "mainCode": "*91",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "FMFM Call Push",
                  "mainCode": "*26",
                  "enableFAC": "true"
                },
                {
                  "featureAccessCodeName": "Call Forwarding Not Reachable Activation",
                  "mainCode": "*94",
                  "enableFAC": "true"
                }
              ],
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            },
            "portalPasscode": {
              "isLoginDisabled": false,
              "expirationDays": -22,
              "passcode": "*****",
              "userId": "4003@parkbenchsolutions.com"
            },
            "userSchedules": {
              "schedules": [
                {
                  "name": "user schedule1",
                  "type": "Holiday",
                  "level": "User",
                  "userId": "4003@parkbenchsolutions.com",
                  "events": [
                    {
                      "eventName": "Christmas",
                      "startTime": "2019-12-25T00:00:00",
                      "endTime": "2019-12-25T23:59:59",
                      "allDayEvent": true,
                      "name": "user schedule1",
                      "type": "Holiday",
                      "userId": "4003@parkbenchsolutions.com",
                      "rrule": "DTSTART:20191225T050000Z\nRRULE:FREQ=YEARLY;BYMONTHDAY=25;BYMONTH=12"
                    }
                  ]
                }
              ],
              "userId": "4003@parkbenchsolutions.com",
              "serviceProviderId": "ent.odin",
              "groupId": "grp.odin",
              "isEnterprise": true
            }
          }
        },
        ...
      ]
    }
  ]
}
```
