# GET - User SIP Contacts 

Updates a users SIP contacts

NOTE: 5 is the max amount of sip contats a user can have

### Parameters&#x20;

* service_provider_id (str): Service Provider ID which hosts Group
* group_id (str): Group ID which hosts User
* user_id (str): Target User ID
* sip_contact (list): List of sip contact details to add. 5 max.

### Returns

* None

### How To Use:

```python
my_api.users.put_user_sip_contacts(
    "service_provider_id",
    "group_id",
    "user_id",
    ["contact1@domain.com", "contact2@domain.com", "contact3@domain.com"]
)
```