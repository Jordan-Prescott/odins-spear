# GET - Group Trunk Available Hosted Users

Fetches a list of users available to assign to the trunk group

### Parameters&#x20;

* service_provider_id (str): Target service provider id
* group_id (str): Target group id where trunk group is hosted
* trunk_name (str): Target trunk grou

### Returns

* Dict: List of available users for assigning to trunk group

### How To Use:

```python
my_api.trunk_groups.get_group_trunk_available_hosted_users(
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
      "userId": "odin.mock.sp.user1",
      "lastName": "odin.mock.sp.user1",
      "firstName": "odin.mock.sp.user1",
      "hiraganaLastName": null,
      "hiraganaFirstName": null,
      "phoneNumber": null,
      "extension": null,
      "department": null,
      "emailAddress": null
    },
    {
      "userId": "odin.mock.sp1.user2",
      "lastName": "odin.mock.sp1.user2",
      "firstName": "odin.mock.sp1.user2",
      "hiraganaLastName": "odin.mock.sp1.user2",
      "hiraganaFirstName": "odin.mock.sp1.user2",
      "phoneNumber": null,
      "extension": null,
      "department": null,
      "emailAddress": null
    }
  ]
}
```