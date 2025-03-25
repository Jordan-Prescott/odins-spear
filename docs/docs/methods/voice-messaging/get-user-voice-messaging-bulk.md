# GET - User Voice Messaging Bulk

Retrieves Bulk Voice Messaging Settings For A Group

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Group is located.&#x20;

### Returns

* Dict: Bulk Voice Messaging Settings

### How To Use:

{% code overflow="wrap" %}
```python
my_api.voice_messaging.get_user_voice_messaging_bulk(
    "ServiceProviderID",
    "GroupID",
)
```
{% endcode %}

### Example Data Returned (Formatted)

```json
[
  {
    "service": {
      "assigned": true,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "4002@parkbenchsolutions.com",
      "lastName": 4002,
      "firstName": 4002,
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": 4002,
      "hiraganaFirstName": 4002,
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {
      "isActive": true,
      "processing": "Unified Voice and Email Messaging",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "4002@parkbenchsolutions.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "5135564000@parkbenchsolutions.com",
      "lastName": "Demo user",
      "firstName": "Marc",
      "department": null,
      "phoneNumber": "+1-5135564000",
      "phoneNumberActivated": true,
      "emailAddress": null,
      "hiraganaLastName": "Demo user",
      "hiraganaFirstName": "Marc",
      "inTrunkGroup": false,
      "extension": "64000",
      "countryCode": 1,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {
      "isActive": true,
      "processing": "Unified Voice and Email Messaging",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "5135564000@parkbenchsolutions.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "6106424235X4020@parkbenchsolutions.com",
      "lastName": 4003,
      "firstName": 4003,
      "department": null,
      "phoneNumber": "+1-5134004003",
      "phoneNumberActivated": true,
      "emailAddress": "developer@parkbenchsolutions.com",
      "hiraganaLastName": 4003,
      "hiraganaFirstName": 4003,
      "inTrunkGroup": false,
      "extension": "04003",
      "countryCode": 1,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {
      "isActive": true,
      "processing": "Unified Voice and Email Messaging",
      "voiceMessageDeliveryEmailAddress": "developer@parkbenchsolutions.com",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "6106424235X4020@parkbenchsolutions.com"
    }
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "user4@parkbenchsolutions.com",
      "lastName": "Sonkar",
      "firstName": "Animesh",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "Sonkar",
      "hiraganaFirstName": "Animesh",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "sandesh@parkbenchsolutions.com",
      "lastName": "dixit",
      "firstName": "sandesh",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "dixit",
      "hiraganaFirstName": "sandesh",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "odin-device-test-1@parkbenchsolutions.com",
      "lastName": "odin-device-test-1",
      "firstName": "odin-device-test-1",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "odin-device-test-1",
      "hiraganaFirstName": "odin-device-test-1",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "4001@parkbenchsolutions.com",
      "lastName": 4001,
      "firstName": 4001,
      "department": null,
      "phoneNumber": "+1-8595551401",
      "phoneNumberActivated": true,
      "emailAddress": "developer@parkbenchsolutions.com",
      "hiraganaLastName": 4001,
      "hiraganaFirstName": 4001,
      "inTrunkGroup": false,
      "extension": "51401",
      "countryCode": 1,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {
      "isActive": true,
      "processing": "Unified Voice and Email Messaging",
      "voiceMessageDeliveryEmailAddress": "developer@parkbenchsolutions.com",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "4001@parkbenchsolutions.com"
    }
  },
  {
    "service": {
      "assigned": true,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "ddoris@parkbenchsolutions.com",
      "lastName": "doris",
      "firstName": "dusty",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "doris",
      "hiraganaFirstName": "dusty",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {
      "isActive": false,
      "processing": "Unified Voice and Email Messaging",
      "usePhoneMessageWaitingIndicator": true,
      "sendVoiceMessageNotifyEmail": false,
      "sendCarbonCopyVoiceMessage": false,
      "transferOnZeroToPhoneNumber": false,
      "alwaysRedirectToVoiceMail": false,
      "busyRedirectToVoiceMail": true,
      "noAnswerRedirectToVoiceMail": true,
      "outOfPrimaryZoneRedirectToVoiceMail": false,
      "serviceProviderId": "ent.odin",
      "groupId": "grp.odin",
      "userId": "ddoris@parkbenchsolutions.com"
    }
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "1.grp.odin@parkbenchsolutions.com",
      "lastName": "1.grp.odin",
      "firstName": "1.grp.odin",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "1.grp.odin",
      "hiraganaFirstName": "1.grp.odin",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "2.grp.odin@parkbenchsolutions.com",
      "lastName": "2.grp.odin",
      "firstName": "2.grp.odin",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "2.grp.odin",
      "hiraganaFirstName": "2.grp.odin",
      "inTrunkGroup": false,
      "extension": "",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "grp.odin4000@parkbenchsolutions.com",
      "lastName": "grp.odin4000",
      "firstName": "grp.odin4000",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "grp.odin4000",
      "hiraganaFirstName": "grp.odin4000",
      "inTrunkGroup": false,
      "extension": "04000",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "grp.odin4001@parkbenchsolutions.com",
      "lastName": "grp.odin4001",
      "firstName": "grp.odin4001",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "grp.odin4001",
      "hiraganaFirstName": "grp.odin4001",
      "inTrunkGroup": false,
      "extension": "04001",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "grp.odin6001@parkbenchsolutions.com",
      "lastName": "grp.odin6001",
      "firstName": "grp.odin6001",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "grp.odin6001",
      "hiraganaFirstName": "grp.odin6001",
      "inTrunkGroup": false,
      "extension": "06001",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  },
  {
    "service": {
      "assigned": false,
      "serviceName": "Voice Messaging User"
    },
    "user": {
      "userId": "grp.odin6002@parkbenchsolutions.com",
      "lastName": "grp.odin6002",
      "firstName": "grp.odin6002",
      "department": null,
      "phoneNumber": "",
      "phoneNumberActivated": null,
      "emailAddress": null,
      "hiraganaLastName": "grp.odin6002",
      "hiraganaFirstName": "grp.odin6002",
      "inTrunkGroup": false,
      "extension": "06002",
      "countryCode": null,
      "nationalPrefix": null,
      "domain": "parkbenchsolutions.com"
    },
    "data": {}
  }
]
```
