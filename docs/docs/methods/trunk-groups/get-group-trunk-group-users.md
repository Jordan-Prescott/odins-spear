# GET - Group Trunk Group Users

Fetches a list of users assigned to a specific trunk.

### Parameters&#x20;

* service_provider_id (str): Target service provider id
* group_id (str): Target group id where trunk group is hosted
* trunk_name (str): Target trunk group

### Returns

* Dict: Trunk group and list of users assigned

### How To Use:

```python
my_api.trunk_groups.get_group_trunk_group_users(
    "ServiceProviderID",
    "groupId",
    "trunkName"
)
```

### Example Data Returned (Formatted)
```python
{
  "serviceProviderId": "odin.mock.sp1",
  "groupId": "odin.mock.sp.grp1",
  "name": "odin.mock.trunk2",
  "users": [
    {
      "userId": "trunk2-user-1",
      "lastName": "asdf",
      "firstName": "asdf",
      "department": null,
      "phoneNumber": null,
      "hiraganaLastName": null,
      "hiraganaFirstName": null,
      "extension": null,
      "emailAddress": null
    },
    {
      "userId": "trunk2-user-2",
      "lastName": "asdf",
      "firstName": "asdf",
      "department": null,
      "phoneNumber": null,
      "hiraganaLastName": null,
      "hiraganaFirstName": null,
      "extension": null,
      "emailAddress": null
    }
  ]
}
```