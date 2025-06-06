# PUT - Extensions

Updates extension settings for a group.

### Parameters&#x20;

*  service_provider_id (str): The service provider ID.
*  group_id (str): The group ID.
*  min_ext_length (int): The minimum extension length. Defaults to None.
*  max_ext_lenth (int): The maximum extension length. Defaults to None.
*  default_ext_length (int): The default extension length.Defaults to None.*

### Returns

* Dict: Updated extension settings.

### How To Use:

```python
my_api.extensions.put_group_extensions(
    service_provider_id = "my_service_proviider_id", 
    group_id = "my_group_id",
    min_ext_length = 2,
    max_ext_length = 6,
    default_ext_length = 4
)
```

### Example Data Returned (Formatted)

```python
{
  "minExtensionLength": 2,
  "maxExtensionLength": 6,
  "defaultExtensionLength": 4,
  "serviceProviderId": "ent.odin",
  "groupId": "grp.odin"
}
```