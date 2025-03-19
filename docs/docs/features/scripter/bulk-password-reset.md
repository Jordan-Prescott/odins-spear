# Bulk Password Reset

Resets a list of users SIP passwords, Voicemail passcodes, or Web Authentication Password. Specifify in password\_type with the options of SIP = 'SIP', Voicemail = 'VM', or Web = "WEB" and the script will perform the necessary actions.

{% hint style="warning" %}
```
This script ONLY updates SIP passwords, Voicemail passcodes, or Web Authentication password..
```
{% endhint %}

The script makes use of the following methods:

```python
api.password_generate.get_passwords_generate()
api.authentication.put_user_authentication_service()
api.password_generate.get_passcodes_generate()
api.authentication.put_user_portal_passcode()
api.password_generate.get_passwords_generate()
api.authentication.put_user_web_authentication_password()
```

### Parameters

* service\_provider\_id (str): Service Provider ID where group is hosted.
* group\_id (str): Group ID where target users are located.
* users (list): List of User IDs of the target users to reset the password.
* password\_type (str): Type of password to reset either 'SIP', 'VM', or 'WEB'. Only accepts these two options.

### Raises:

* OSInvalidPasswordType: Only valid password options are SIP, VM, WEB. If another is requested this will be raised.

### Return

* dict: Returns dictionary containing user ID and new password set.

### How To Use:
{% hint style="info" %}
This method requires keyword arguments i.e. group_id="group_id"
{% endhint %}

```python
assistant = Scripter(my_api)

users = [
    "testuser1@domain.com",
    "testuser2@domain.com",
    "testuser3@domain.com"
]

# changes SIP password for users
assistant.bulk_password_reset(
        service_provider_id="ServiceProviderID",
        group_id="GroupID",
        users=users,
        password_type="SIP"   
    )
    
# changes Voicemail passcode for users
assistant.bulk_password_reset(
        service_provider_id="ServiceProviderID",
        group_id="GroupID",
        users=users,
        password_type="VM"   
    )
    
# changes Web Authentication password for users
assistant.bulk_password_reset(
        service_provider_id="ServiceProviderID",
        group_id="GroupID",
        users=users,
        password_type="WEB"   
    )
```

### Example Returned Data of SIP Passwords (Formatted)

```json
[
   {
      "userId":"User1@domain.com",
      "newPassword":"3h1U[-"
   },
   {
      "userId":"User2@domain.com",
      "newPassword":"e^Bv4c"
   },
   {
      "userId":"User3@domain.com",
      "newPassword":"4WK#:y"
   }
   {
      "userId":"User1@domain.com",
      "newPassword":"3h1U[-"
   },
   {
      "userId":"User2@domain.com",
      "newPassword":"e^Bv4c"
   },
   {
      "userId":"User3@domain.com",
      "newPassword":"4WK#:y"
   }
]
```
