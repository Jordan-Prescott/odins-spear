# GET - Extensions

Gets extension settings for a group.

### Parameters&#x20;

* service_provider_id (str): The service provider ID.
* group_id (str): The group ID.

### Returns

* Dict: Extension settings.

### How To Use:

```python
my_api.extensions.get_group_extensions(
    service_provider_id = "my_service_proviider_id", 
    group_id = "my_group_id"
)
```

### Example Data Returned (Formatted)

```python
{
  "minExtensionLength": 3,
  "maxExtensionLength": 5,
  "defaultExtensionLength": 4,
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin"
}
```