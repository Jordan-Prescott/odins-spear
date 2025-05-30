# GET - User Audit 

Returns a detailed audit of user spanning from generic details to call policies and features assigned.

### Parameters&#x20;

* user\_id (str): Target user ID.

### Returns

* Dict: Audit details of user

### How To Use:

```python
my_api.users.get_user_audit(
    "user_ID"
)
```

### Example Data Returned (Formatted)

```python
{
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin",
  "userId": "4001@parkbenchsolutions.com",
  "Settings": {
    "User": {
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "lastName": 4001,
      "firstName": 4001,
      "callingLineIdLastName": "4001-lastname",
      "callingLineIdFirstName": "4001-firstname",
      "hiraganaLastName": 4001,
      "hiraganaFirstName": 4001,
      "phoneNumber": "8595551401",
      "extension": "1401",
      "language": "English",
      "timeZone": "America/New_York",
      "timeZoneDisplayName": "(GMT-04:00) (US) Eastern Time",
      "defaultAlias": "4001@parkbenchsolutions.com",
      "accessDeviceEndpoint": {
        "accessDevice": {
          "deviceType": "Polycom VVX500",
          "protocol": "SIP 2.0",
          "numberOfPorts": {
            "quantity": "32"
          },
          "numberOfAssignedPorts": 1,
          "status": "Online",
          "configurationMode": "Default",
          "transportProtocol": "UDP",
          "useCustomUserNamePassword": false,
          "deviceName": "polycomvvx_500_iii",
          "deviceLevel": "Group",
          "accessDeviceCredentials": {
            "userName": null
          },
          "serviceProviderId": "ent.odin",
          "groupId": "grp.odin",
          "tags": [],
          "relatedServices": []
        },
        "linePort": "4001@parkbenchsolutions.com",
        "staticRegistrationCapable": "false",
        "useDomain": "true",
        "supportVisualDeviceManagement": "false",
        "contacts": []
      },
      "title": "Programmer",
      "pagerPhoneNumber": "100-555-1414",
      "mobilePhoneNumber": "100-444-1414",
      "emailAddress": "developer@parkbenchsolutions.com",
      "yahooId": "developer@yahoo.com",
      "addressLocation": "Main Building",
      "address": {
        "addressLine1": "123 main street",
        "addressLine2": "suite 100",
        "city": "disney",
        "stateOrProvince": "Florida",
        "zipOrPostalCode": "12345",
        "country": "US"
      },
      "countryCode": "1",
      "impId": "4001.ent.odin@lab.alliedtelecom.net",
      "userId": "4001@parkbenchsolutions.com",
      "callingLineIdPhoneNumber": "",
      "domain": "parkbenchsolutions.com",
      "endpointType": "accessDeviceEndpoint",
      "aliases": [],
      "trunkAddressing": {
        "trunkGroupDeviceEndpoint": {
          "contacts": []
        }
      },
      "isEnterprise": true,
      "passwordExpiresDays": 2147483647
    },
    "Alternate User Id": {
      "users": [],
      "userId": "4001@parkbenchsolutions.com"
    },
    "Announcement File": {
      "totalFileSize": 0,
      "maxFileSize": 1000,
      "userId": "4001@parkbenchsolutions.com",
      "announcementType": "",
      "announcements": []
    },
    "Call Policies": {
      "redirectedCallsCOLPPrivacy": "Privacy For All Calls",
      "callBeingForwardedResponseCallType": "All Calls",
      "callingLineIdentityForRedirectedCalls": "Redirecting User Identity For All Redirections",
      "userId": "4001@parkbenchsolutions.com"
    },
    "Call Processing Policy": {
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
      "userId": "4001@parkbenchsolutions.com"
    },
    "Communication Barring": {
      "useGroupSetting": true,
      "userId": "4001@parkbenchsolutions.com"
    },
    "Communication Barring Authorization Code": [
      {
        "code": "1234",
        "description": "1234",
        "userId": "4001@parkbenchsolutions.com"
      }
    ],
    "Device Policies": {
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
      "userId": "4001@parkbenchsolutions.com"
    },
    "Feature Access Code": {
      "userId": "4001@parkbenchsolutions.com",
      "featureAccessCodes": [
        {
          "featureAccessCodeName": "Mobility Calling Line ID Deactivation Per Call",
          "mainCode": "*29",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding Not Reachable Deactivation",
          "mainCode": "*95",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Direct Voice Mail Transfer",
          "mainCode": "*55",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Bridge",
          "mainCode": "*15",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Calling Line ID Delivery per Call",
          "mainCode": "*65",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Park",
          "mainCode": "*68",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Connected Line Identification Restriction Interrogation",
          "mainCode": "*56*",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Group Call Park",
          "mainCode": "#58",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Call Anchoring Deactivation Per Call",
          "mainCode": "*24",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Calling Line ID Activation",
          "mainCode": "#28",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Voice Mail Clear MWI",
          "mainCode": "*99",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Speed Dial 100",
          "mainCode": "*75",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Cancel Call Waiting",
          "mainCode": "*70",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding No Answer To Voice Mail Deactivation",
          "mainCode": "#41",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Calling Line ID Deactivation",
          "mainCode": "#29",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding Busy Activation",
          "mainCode": "*90",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Recording - Pause",
          "mainCode": "*48",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Recording - Start",
          "mainCode": "*44",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Call Anchoring Activation",
          "mainCode": "#23",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Call Anchoring Deactivation",
          "mainCode": "#24",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Do Not Disturb Activation",
          "mainCode": "*78",
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
          "featureAccessCodeName": "Calling Line ID Delivery Blocking Interrogation",
          "mainCode": "*54*",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Location Control Deactivation",
          "mainCode": "*13",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Calling Line ID Delivery Blocking Persistent Activation",
          "mainCode": "*31",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Communication Barring User-Control Activation",
          "mainCode": "*33*",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Waiting Persistent Deactivation",
          "mainCode": "#43",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Calling Line ID Delivery Blocking Persistent Deactivation",
          "mainCode": "#31",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "No Answer Timer",
          "mainCode": "*610",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding Always To Voice Mail Activation",
          "mainCode": "*21",
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
          "featureAccessCodeName": "Call Forwarding Busy To Voice Mail Activation",
          "mainCode": "*40",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Call Anchoring Activation Per Call",
          "mainCode": "*23",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Automatic Callback Menu Access",
          "mainCode": "#9",
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
          "featureAccessCodeName": "Calling Line ID Delivery Blocking per Call",
          "mainCode": "*67",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Mobility Calling Line ID Activation Per Call",
          "mainCode": "*28",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Communication Barring User-Control Deactivation",
          "mainCode": "#33*",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Recording - Stop",
          "mainCode": "*45",
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
          "featureAccessCodeName": "Call Recording - Resume",
          "mainCode": "*49",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Hunt Group Busy Interrogation",
          "mainCode": "#53",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Advice Of Charge Activation",
          "mainCode": "*34",
          "alternateCode": "*3434",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Voice Mail Retrieval",
          "mainCode": "*86",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding Busy To Voice Mail Deactivation",
          "mainCode": "#40",
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
          "featureAccessCodeName": "Call Waiting Interrogation",
          "mainCode": "*53*",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Number Portability Announcement Activation",
          "mainCode": "*84",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Call Forwarding Always To Voice Mail Deactivation",
          "mainCode": "#21",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Number Portability Announcement Deactivation",
          "mainCode": "*85",
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
          "featureAccessCodeName": "Call Waiting Persistent Activation",
          "mainCode": "*43",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Do Not Disturb Deactivation",
          "mainCode": "*79",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Push Notification Retrieval",
          "mainCode": "#0322",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Automatic Callback Deactivation",
          "mainCode": "#8",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Push to Talk",
          "mainCode": "*50",
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
          "featureAccessCodeName": "Communication Barring User-Control Query",
          "mainCode": "*#33#",
          "enableFAC": "true"
        },
        {
          "featureAccessCodeName": "Directed Call Pickup with Barge-in",
          "mainCode": "*33",
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
        },
        {
          "featureAccessCodeName": "Call Forwarding No Answer To Voice Mail Activation",
          "mainCode": "*41",
          "enableFAC": "true"
        }
      ]
    },
    "Portal Passcode": {
      "isLoginDisabled": false,
      "expirationDays": 19,
      "passcode": "*****",
      "userId": "4001@parkbenchsolutions.com"
    },
    "Schedules": [
      {
        "name": "user schedule 1",
        "type": "Time",
        "level": "User",
        "userId": "4001@parkbenchsolutions.com",
        "events": [
          {
            "eventName": "event 1",
            "startTime": "2019-04-30T00:00:00",
            "endTime": "2019-04-30T23:59:59",
            "allDayEvent": true,
            "name": "user schedule 1",
            "type": "Time",
            "userId": "4001@parkbenchsolutions.com",
            "rrule": null
          }
        ]
      }
    ]
  },
  "OutgoingCallingPlan": {
    "Outgoing Calling Plan Authorization Code": {
      "settings": {
        "useCustomSettings": true,
        "userId": "4001@parkbenchsolutions.com",
        "serviceProviderId": "ent.odin",
        "groupId": "grp.odin",
        "isEnterprise": true
      },
      "codes": [
        {
          "code": "1001",
          "description": "1001"
        },
        {
          "code": "1002",
          "description": "1002"
        }
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Call Me Now": {
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
        "premiumServicesI": true,
        "premiumServicesII": true,
        "casual": true,
        "urlDialing": true,
        "unknown": true
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Digit Plan Call Me Now": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Digit Plan Originating": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Digit Plan Redirecting": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Originating": {
      "useCustomSettings": true,
      "userPermissions": {
        "group": "Allow",
        "local": "Allow",
        "tollFree": "Allow",
        "toll": "Allow",
        "international": "Allow",
        "operatorAssisted": "Allow",
        "chargeableDirectoryAssisted": "Allow",
        "specialServicesI": "Allow",
        "specialServicesII": "Allow",
        "premiumServicesI": "Allow",
        "premiumServicesII": "Allow",
        "casual": "Allow",
        "urlDialing": "Allow",
        "unknown": "Allow"
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Redirected": {
      "useCustomSettings": true,
      "userPermissions": {
        "outsideGroup": true
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Redirecting": {
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
        "premiumServicesI": true,
        "premiumServicesII": true,
        "casual": true,
        "urlDialing": true,
        "unknown": true
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Transfer Numbers": {
      "useCustomSettings": true,
      "userNumbers": {
        "phoneNumber01": "123",
        "phoneNumber02": "123",
        "phoneNumber03": "123"
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Pinhole Digit Plan Call Me Now": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Pinhole Digit Plan Originating": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outgoing Calling Plan Pinhole Digit Plan Redirecting": {
      "useCustomSettings": true,
      "userPermissions": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    }
  },
  "UserServices": {
    "servicesAssignment": {
      "userId": "4001@parkbenchsolutions.com",
      "userServices": [
        {
          "serviceName": "Anonymous Call Rejection",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Call Forwarding Always"
        },
        {
          "serviceName": "Call Forwarding Busy",
          "assigned": true,
          "tags": [],
          "alias": "Call Forwarding Busy"
        },
        {
          "serviceName": "Call Forwarding No Answer",
          "assigned": true,
          "tags": [],
          "alias": "Call Forwarding No Answer"
        },
        {
          "serviceName": "Call Notify",
          "assigned": true,
          "tags": [],
          "alias": "Call Notify"
        },
        {
          "serviceName": "Calling Line ID Delivery Blocking",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "CommPilot Call Manager"
        },
        {
          "serviceName": "Do Not Disturb",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Outlook Integration"
        },
        {
          "serviceName": "Priority Alert",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Selective Call Acceptance"
        },
        {
          "serviceName": "Call Forwarding Selective",
          "assigned": true,
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
          "assigned": true,
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
          "assigned": false,
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
          "assigned": true,
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
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Third-Party Voice Mail Support"
        },
        {
          "serviceName": "Directed Call Pickup with Barge-in",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "External Calling Line ID Delivery"
        },
        {
          "serviceName": "Internal Calling Line ID Delivery",
          "assigned": true,
          "tags": [],
          "alias": "Internal Calling Line ID Delivery"
        },
        {
          "serviceName": "Automatic Callback",
          "assigned": true,
          "tags": [],
          "alias": "Automatic Callback"
        },
        {
          "serviceName": "Call Waiting",
          "assigned": true,
          "tags": [],
          "alias": "Call Waiting"
        },
        {
          "serviceName": "Calling Line ID Blocking Override",
          "assigned": true,
          "tags": [],
          "alias": "Calling Line ID Blocking Override"
        },
        {
          "serviceName": "Calling Party Category",
          "assigned": true,
          "tags": [],
          "alias": "Calling Party Category"
        },
        {
          "serviceName": "Barge-in Exempt",
          "assigned": true,
          "tags": [],
          "alias": "Barge-in Exempt"
        },
        {
          "serviceName": "Video Add-On",
          "assigned": true,
          "tags": [],
          "alias": "Video Add-On"
        },
        {
          "serviceName": "Malicious Call Trace",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Push to Talk"
        },
        {
          "serviceName": "Basic Call Logs",
          "assigned": false,
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
          "assigned": true,
          "tags": [],
          "alias": "Hoteling Host"
        },
        {
          "serviceName": "Hoteling Guest",
          "assigned": true,
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
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Call Transfer"
        },
        {
          "serviceName": "Privacy",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Physical Location"
        },
        {
          "serviceName": "Charge Number",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Two-Stage Dialing"
        },
        {
          "serviceName": "Call Forwarding Not Reachable",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "External Custom Ringback"
        },
        {
          "serviceName": "In-Call Service Activation",
          "assigned": true,
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
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Advice Of Charge"
        },
        {
          "serviceName": "Prepaid",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Communication Barring User-Control"
        },
        {
          "serviceName": "Classmark",
          "assigned": true,
          "tags": [],
          "alias": "Classmark"
        },
        {
          "serviceName": "Calling Name Delivery",
          "assigned": true,
          "tags": [],
          "alias": "Calling Name Delivery"
        },
        {
          "serviceName": "Calling Number Delivery",
          "assigned": true,
          "tags": [],
          "alias": "Calling Number Delivery"
        },
        {
          "serviceName": "Virtual On-Net Enterprise Extensions",
          "assigned": false,
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
          "assigned": true,
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
          "assigned": true,
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
          "assigned": true,
          "tags": [
            "UC-One"
          ],
          "alias": "Integrated IMP"
        },
        {
          "serviceName": "Group Night Forwarding",
          "assigned": true,
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
          "assigned": false,
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
          "assigned": true,
          "tags": [],
          "alias": "Security Classification"
        },
        {
          "serviceName": "Flexible Seating Guest",
          "assigned": false,
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
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Call Forwarding Always Secondary"
        },
        {
          "serviceName": "Silent Alerting",
          "assigned": true,
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
          "assigned": true,
          "tags": [],
          "alias": "Sequential Ring"
        },
        {
          "serviceName": "Number Portability Announcement",
          "assigned": true,
          "tags": [],
          "alias": "Number Portability Announcement"
        },
        {
          "serviceName": "Direct Route",
          "assigned": true,
          "tags": [],
          "alias": "Direct Route"
        },
        {
          "serviceName": "Terminating Alternate Trunk Identity",
          "assigned": true,
          "tags": [],
          "alias": "Terminating Alternate Trunk Identity"
        }
      ],
      "servicePackServices": [
        {
          "assigned": false,
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
      ]
    },
    "servicesAssigned": {
      "userId": "4001@parkbenchsolutions.com",
      "userServices": [
        {
          "serviceName": "Advice Of Charge"
        },
        {
          "serviceName": "Anonymous Call Rejection",
          "isActive": true
        },
        {
          "serviceName": "Attendant Console"
        },
        {
          "serviceName": "Authentication"
        },
        {
          "serviceName": "Automatic Callback",
          "isActive": true
        },
        {
          "serviceName": "Automatic Hold/Retrieve",
          "isActive": true
        },
        {
          "serviceName": "Barge-in Exempt",
          "isActive": true
        },
        {
          "serviceName": "BroadWorks Mobility",
          "isActive": true
        },
        {
          "serviceName": "Busy Lamp Field"
        },
        {
          "serviceName": "Call Forwarding Always",
          "isActive": true
        },
        {
          "serviceName": "Call Forwarding Always Secondary",
          "isActive": true
        },
        {
          "serviceName": "Call Forwarding Busy",
          "isActive": true
        },
        {
          "serviceName": "Call Forwarding No Answer",
          "isActive": true
        },
        {
          "serviceName": "Call Forwarding Not Reachable",
          "isActive": true
        },
        {
          "serviceName": "Call Forwarding Selective",
          "isActive": true
        },
        {
          "serviceName": "Call Notify",
          "isActive": true
        },
        {
          "serviceName": "Call Recording",
          "isActive": true
        },
        {
          "serviceName": "Call Transfer"
        },
        {
          "serviceName": "Call Waiting",
          "isActive": true
        },
        {
          "serviceName": "Calling Line ID Blocking Override",
          "isActive": true
        },
        {
          "serviceName": "Calling Line ID Delivery Blocking",
          "isActive": true
        },
        {
          "serviceName": "Calling Name Delivery",
          "isActive": true
        },
        {
          "serviceName": "Calling Name Retrieval",
          "isActive": true
        },
        {
          "serviceName": "Calling Number Delivery",
          "isActive": true
        },
        {
          "serviceName": "Calling Party Category"
        },
        {
          "serviceName": "Charge Number"
        },
        {
          "serviceName": "Classmark"
        },
        {
          "serviceName": "CommPilot Call Manager"
        },
        {
          "serviceName": "CommPilot Express",
          "isActive": true
        },
        {
          "serviceName": "Communication Barring User-Control"
        },
        {
          "serviceName": "Connected Line Identification Restriction",
          "isActive": true
        },
        {
          "serviceName": "Direct Route"
        },
        {
          "serviceName": "Directed Call Pickup with Barge-in"
        },
        {
          "serviceName": "Do Not Disturb",
          "isActive": true
        },
        {
          "serviceName": "External Calling Line ID Delivery",
          "isActive": true
        },
        {
          "serviceName": "External Custom Ringback",
          "isActive": true
        },
        {
          "serviceName": "Fax Messaging",
          "isActive": true
        },
        {
          "serviceName": "Group Night Forwarding",
          "isActive": true
        },
        {
          "serviceName": "Hoteling Guest",
          "isActive": true
        },
        {
          "serviceName": "Hoteling Host",
          "isActive": true
        },
        {
          "serviceName": "In-Call Service Activation",
          "isActive": true
        },
        {
          "serviceName": "Integrated IMP",
          "isActive": true
        },
        {
          "serviceName": "Intercept User",
          "isActive": false
        },
        {
          "serviceName": "Internal Calling Line ID Delivery",
          "isActive": true
        },
        {
          "serviceName": "Malicious Call Trace",
          "isActive": true
        },
        {
          "serviceName": "Number Portability Announcement",
          "isActive": false
        },
        {
          "serviceName": "Outlook Integration",
          "isActive": true
        },
        {
          "serviceName": "Physical Location",
          "isActive": true
        },
        {
          "serviceName": "Prepaid",
          "isActive": true
        },
        {
          "serviceName": "Priority Alert",
          "isActive": true
        },
        {
          "serviceName": "Privacy"
        },
        {
          "serviceName": "Push to Talk"
        },
        {
          "serviceName": "Route List"
        },
        {
          "serviceName": "Security Classification",
          "isActive": true
        },
        {
          "serviceName": "Selective Call Acceptance",
          "isActive": true
        },
        {
          "serviceName": "Selective Call Rejection",
          "isActive": true
        },
        {
          "serviceName": "Sequential Ring",
          "isActive": true
        },
        {
          "serviceName": "Shared Call Appearance"
        },
        {
          "serviceName": "Silent Alerting",
          "isActive": true
        },
        {
          "serviceName": "Simultaneous Ring Personal",
          "isActive": true
        },
        {
          "serviceName": "Speed Dial 100"
        },
        {
          "serviceName": "Speed Dial 8"
        },
        {
          "serviceName": "Terminating Alternate Trunk Identity"
        },
        {
          "serviceName": "Third-Party Voice Mail Support",
          "isActive": true
        },
        {
          "serviceName": "Two-Stage Dialing",
          "isActive": true
        },
        {
          "serviceName": "Video Add-On",
          "isActive": true
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
      ]
    },
    "Advice Of Charge": {
      "isActive": true,
      "aocType": "During Call",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Anonymous Call Rejection": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Attendant Console": {
      "launchOnLogin": true,
      "allowUserConfigCallDetails": true,
      "allowUserViewCallDetails": true,
      "users": [
        {
          "userId": "4003@parkbenchsolutions.com",
          "lastName": 4003,
          "firstName": 4003,
          "hiraganaLastName": 4003,
          "hiraganaFirstName": 4003,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": "4003.ent.odin@lab.alliedtelecom.net"
        },
        {
          "userId": "4002@parkbenchsolutions.com",
          "lastName": 4002,
          "firstName": 4002,
          "hiraganaLastName": 4002,
          "hiraganaFirstName": 4002,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        }
      ],
      "displayColumns": [
        "Status",
        "Name",
        "Phone Number",
        "Extension",
        "Action",
        "Department",
        "Email",
        "Mobile",
        "Pager",
        "Title"
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Automatic Callback": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Automatic Hold/Retrieve": {
      "isActive": true,
      "recallTimerSeconds": 120,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Barge-in Exempt": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "BroadWorks Mobility": {
      "isActive": true,
      "phonesToRing": "Fixed",
      "mobilePhoneNumber": 5131114444,
      "alertClickToDialCalls": true,
      "alertGroupPagingCalls": true,
      "enableDiversionInhibitor": true,
      "requireAnswerConfirmation": true,
      "broadworksCallControl": true,
      "useSettingLevel": "Group",
      "denyCallOriginations": true,
      "denyCallTerminations": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Busy Lamp Field": {
      "listURI": "blf_4001@parkbenchsolutions.com",
      "enableCallParkNotification": true,
      "users": [
        {
          "userId": "4002@parkbenchsolutions.com",
          "lastName": 4002,
          "firstName": 4002,
          "hiraganaLastName": 4002,
          "hiraganaFirstName": 4002,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        },
        {
          "userId": "4003@parkbenchsolutions.com",
          "lastName": 4003,
          "firstName": 4003,
          "hiraganaLastName": 4003,
          "hiraganaFirstName": 4003,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": "4003.ent.odin@lab.alliedtelecom.net"
        },
        {
          "userId": "odin-user-2@parkbenchsolutions.com",
          "lastName": "odin-user-2",
          "firstName": "odin-user-2",
          "hiraganaLastName": null,
          "hiraganaFirstName": null,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        }
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding Always": {
      "isActive": true,
      "forwardToPhoneNumber": 1111,
      "isRingSplashActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding Always Secondary": {
      "isActive": true,
      "forwardToPhoneNumber": 1111,
      "isRingSplashActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding Busy": {
      "isActive": true,
      "forwardToPhoneNumber": 1111,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding No Answer": {
      "isActive": true,
      "forwardToPhoneNumber": 1111,
      "numberOfRings": 4,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding Not Reachable": {
      "isActive": true,
      "forwardToPhoneNumber": 1111,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Forwarding Selective": {
      "isActive": true,
      "defaultForwardToPhoneNumber": 1111,
      "playRingReminder": true,
      "userId": "4001@parkbenchsolutions.com",
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria1",
          "timeSchedule": "Every Day All Day",
          "blacklisted": false,
          "holidaySchedule": "None",
          "forwardTo": 1111,
          "callsToType": null,
          "callsToNumber": null,
          "callsToExtension": null,
          "callsFrom": [
            "All calls"
          ],
          "forwardToNumberSelection": "Forward To Specified Number",
          "forwardToPhoneNumber": 1111,
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Any",
            "includeAnonymousCallers": "false",
            "includeUnavailableCallers": "false",
            "phoneNumbers": []
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Notify": {
      "callNotifyEmailAddress": "developer@parkbenchsolutions.com",
      "userId": "4001@parkbenchsolutions.com",
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria1",
          "timeSchedule": null,
          "callFrom": "All calls",
          "blacklisted": true,
          "holidaySchedule": null,
          "callsToType": null,
          "callsToNumber": null,
          "callsToExtension": null,
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Any",
            "includeAnonymousCallers": "false",
            "includeUnavailableCallers": "false",
            "phoneNumbers": []
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Recording": {
      "recordingOption": "Always",
      "pauseResumeNotification": "Beep",
      "enableCallRecordingAnnouncement": true,
      "enableRecordCallRepeatWarningTone": true,
      "recordCallRepeatWarningToneTimerSeconds": 15,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Transfer": {
      "isRecallActive": true,
      "recallNumberOfRings": 4,
      "useDiversionInhibitorForBlindTransfer": true,
      "useDiversionInhibitorForConsultativeCalls": true,
      "enableBusyCampOn": true,
      "busyCampOnSeconds": 120,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Call Waiting": {
      "isActive": true,
      "disableCallingLineIdDelivery": false,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Line ID Blocking Override": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Line ID Delivery Blocking": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Name Delivery": {
      "isActiveForExternalCalls": true,
      "isActiveForInternalCalls": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Name Retrieval": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Number Delivery": {
      "isActiveForExternalCalls": true,
      "isActiveForInternalCalls": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Calling Party Category": {
      "category": "Special",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Charge Number": {
      "phoneNumber": 8135551001,
      "useChargeNumberForEnhancedTranslations": true,
      "sendChargeNumberToNetwork": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Classmark": {
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "CommPilot Call Manager": {
      "launchOnLogin": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "CommPilot Express": {
      "profile": "Available In Office",
      "availableInOffice": {
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
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Communication Barring User-Control": {
      "lockoutStatus": false,
      "profileTable": [],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Connected Line Identification Restriction": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Direct Route": {
      "outgoingDTGPolicy": "Trunk Group DTG",
      "outgoingTrunkIdentityPolicy": "Trunk Group Trunk Identity",
      "routes": {
        "dtgIdentity": [
          "1111"
        ],
        "trunkIdentity": []
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Directed Call Pickup with Barge-in": {
      "enableBargeInWarningTone": true,
      "enableAutomaticTargetSelection": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Do Not Disturb": {
      "isActive": true,
      "ringSplash": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "External Calling Line ID Delivery": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "External Custom Ringback": {
      "isActive": true,
      "useSettingLevel": "User",
      "sipRequestURI": "developer@parkbenchsolutions.com",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Fax Messaging": {
      "isActive": true,
      "phoneNumber": 8135551002,
      "extension": 1002,
      "userId": "4001@parkbenchsolutions.com",
      "aliases": [
        {
          "phoneNumber": "developer",
          "domain": "parkbenchsolutions.com"
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Group Night Forwarding": {
      "nightForwarding": "On",
      "groupNightForwarding": "Off",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Hoteling Guest": {
      "isActive": true,
      "enableAssociationLimit": true,
      "associationLimitHours": 12,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Hoteling Host": {
      "isActive": true,
      "enforceAssociationLimit": true,
      "associationLimitHours": 24,
      "accessLevel": "Group",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "In-Call Service Activation": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Integrated IMP": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Intercept User": {
      "isActive": false,
      "announcementSelection": "Default",
      "inboundCallMode": "Intercept All",
      "alternateBlockingAnnouncement": false,
      "exemptInboundMobilityCalls": false,
      "disableParallelRingingToNetworkLocations": false,
      "routeToVoiceMail": false,
      "playNewPhoneNumber": false,
      "transferOnZeroToPhoneNumber": false,
      "outboundCallMode": "Block All",
      "exemptOutboundMobilityCalls": false,
      "rerouteOutboundCalls": false,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Internal Calling Line ID Delivery": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Malicious Call Trace": {
      "isActive": true,
      "traceTypeSelection": "All Incoming",
      "traceForTimePeriod": true,
      "traceTimePeriod": {
        "startDateTime": "2019-04-30T08:54:00.321-04:00",
        "stopDateTime": "2019-05-01T08:54:00.321-04:00"
      },
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Number Portability Announcement": {
      "enable": false,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Outlook Integration": {
      "isActive": true,
      "contactRetrievalSelection": "Retrieve Default Contact Folder Only",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Physical Location": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Prepaid": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Priority Alert": {
      "userId": "4001@parkbenchsolutions.com",
      "isActive": true,
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria1",
          "timeSchedule": "Every Day All Day",
          "blacklisted": true,
          "holidaySchedule": "None",
          "callsToType": null,
          "callsToNumber": null,
          "callsToExtension": null,
          "callsFrom": [
            "1111"
          ],
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Specified Only",
            "includeAnonymousCallers": "false",
            "includeUnavailableCallers": "false",
            "phoneNumbers": [
              "1111"
            ]
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Privacy": {
      "enableDirectoryPrivacy": true,
      "enableAutoAttendantExtensionDialingPrivacy": true,
      "enableAutoAttendantNameDialingPrivacy": true,
      "enablePhoneStatusPrivacy": true,
      "permittedMonitors": [
        {
          "userId": "4003@parkbenchsolutions.com",
          "lastName": 4003,
          "firstName": 4003,
          "hiraganaLastName": 4003,
          "hiraganaFirstName": 4003,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": "4003.ent.odin@lab.alliedtelecom.net"
        },
        {
          "userId": "odin-user-2@parkbenchsolutions.com",
          "lastName": "odin-user-2",
          "firstName": "odin-user-2",
          "hiraganaLastName": null,
          "hiraganaFirstName": null,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        },
        {
          "userId": "4002@parkbenchsolutions.com",
          "lastName": 4002,
          "firstName": 4002,
          "hiraganaLastName": 4002,
          "hiraganaFirstName": 4002,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        }
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Push to Talk": {
      "allowAutoAnswer": false,
      "outgoingConnectionSelection": "One Way",
      "accessListSelection": "Allow Calls From Everyone Except Selected Users",
      "userId": "4001@parkbenchsolutions.com",
      "users": [
        {
          "userId": "4003@parkbenchsolutions.com",
          "lastName": 4003,
          "firstName": 4003,
          "hiraganaLastName": 4003,
          "hiraganaFirstName": 4003,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": "4003.ent.odin@lab.alliedtelecom.net"
        },
        {
          "userId": "odin-user-2@parkbenchsolutions.com",
          "lastName": "odin-user-2",
          "firstName": "odin-user-2",
          "hiraganaLastName": null,
          "hiraganaFirstName": null,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        },
        {
          "userId": "4002@parkbenchsolutions.com",
          "lastName": 4002,
          "firstName": 4002,
          "hiraganaLastName": 4002,
          "hiraganaFirstName": 4002,
          "phoneNumber": null,
          "extension": null,
          "department": null,
          "emailAddress": null,
          "iMPId": null
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Route List": {
      "treatOriginationsAndPBXRedirectionsAsScreened": true,
      "useRouteListIdentityForNonEmergencyCalls": true,
      "useRouteListIdentityForEmergencyCalls": true,
      "dns": [
        {
          "min": "+1-2123135000",
          "max": "+1-2123135999",
          "isActive": true
        }
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Security Classification": {
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Selective Call Acceptance": {
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria",
          "timeSchedule": "Every Day All Day",
          "callFrom": "All calls",
          "blacklisted": false,
          "holidaySchedule": "None",
          "callsToType": null,
          "callsToNumber": null,
          "callsToExtension": null,
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Any",
            "includeAnonymousCallers": false,
            "includeUnavailableCallers": false,
            "phoneNumbers": []
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ]
    },
    "Selective Call Rejection": {
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria",
          "timeSchedule": "Every Day All Day",
          "callsFrom": 1111,
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
              "1111"
            ]
          },
          "private": false,
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Sequential Ring": {
      "ringBaseLocationFirst": true,
      "baseLocationNumberOfRings": 4,
      "continueIfBaseLocationIsBusy": true,
      "callerMayStopSearch": true,
      "userId": "4001@parkbenchsolutions.com",
      "locations": [
        {
          "phoneNumber": "1111",
          "numberOfRings": 3,
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "2222",
          "numberOfRings": 3,
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "3333",
          "numberOfRings": 3,
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "4444",
          "numberOfRings": 3,
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "5555",
          "numberOfRings": 3,
          "answerConfirmationRequired": false
        }
      ],
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria1",
          "timeSchedule": "Every Day All Day",
          "blacklisted": false,
          "holidaySchedule": {
            "name": "Holidays",
            "level": "Group",
            "type": "Holiday"
          },
          "callsFrom": [
            "All calls"
          ],
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Any",
            "includeAnonymousCallers": "false",
            "includeUnavailableCallers": "false",
            "phoneNumbers": []
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
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
      "userId": "4001@parkbenchsolutions.com",
      "endpoints": [],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Silent Alerting": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Simultaneous Ring Personal": {
      "isActive": true,
      "doNotRingIfOnCall": true,
      "userId": "4001@parkbenchsolutions.com",
      "criteria": [
        {
          "isActive": true,
          "criteriaName": "criteria1",
          "timeSchedule": "Every Day All Day",
          "blacklisted": false,
          "holidaySchedule": "None",
          "callsFrom": [
            "All calls"
          ],
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Any",
            "includeAnonymousCallers": false,
            "includeUnavailableCallers": false,
            "phoneNumbers": []
          },
          "userId": "4001@parkbenchsolutions.com"
        },
        {
          "isActive": true,
          "criteriaName": "criteria2",
          "timeSchedule": "Every Day All Day",
          "blacklisted": false,
          "holidaySchedule": "None",
          "callsFrom": [
            "1111",
            "2222",
            "3333..."
          ],
          "fromDnCriteria": {
            "fromDnCriteriaSelection": "Specified Only",
            "includeAnonymousCallers": false,
            "includeUnavailableCallers": false,
            "phoneNumbers": [
              "1111",
              "2222",
              "3333",
              "4444"
            ]
          },
          "userId": "4001@parkbenchsolutions.com"
        }
      ],
      "locations": [
        {
          "phoneNumber": "1111",
          "answerConfirmationRequired": true
        },
        {
          "phoneNumber": "2222",
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "3333",
          "answerConfirmationRequired": false
        },
        {
          "phoneNumber": "4444",
          "answerConfirmationRequired": true
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Speed Dial 100": {
      "userId": "4001@parkbenchsolutions.com",
      "speedCodes": [
        {
          "speedCode": "0",
          "phoneNumber": "0000",
          "description": "0000"
        },
        {
          "speedCode": "1",
          "phoneNumber": "1111",
          "description": "1111"
        }
      ],
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Speed Dial 8": {
      "userId": "4001@parkbenchsolutions.com",
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
          "speedCode": "4",
          "phoneNumber": "444"
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
    "Terminating Alternate Trunk Identity": {
      "terminatingTrunkIdentity": 1111,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Third-Party Voice Mail Support": {
      "isActive": true,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "serverSelection": "Group Mail Server",
      "mailboxIdType": "User Or Group Phone Number",
      "noAnswerNumberOfRings": 4,
      "alwaysRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Two-Stage Dialing": {
      "isActive": true,
      "allowActivationWithUserAddresses": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Video Add-On": {
      "isActive": true,
      "maxOriginatingCallDelaySeconds": 5,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Voice Portal Calling": {
      "isActive": true,
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    },
    "Zone Calling Restrictions": {
      "homeZoneName": "Office",
      "userId": "4001@parkbenchsolutions.com",
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "isEnterprise": true
    }
  },
  "_eventId": 168
}
```
