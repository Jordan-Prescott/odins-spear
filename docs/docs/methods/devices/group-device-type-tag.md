# PUT - Group Device Type Tag

Update tags applied to device types at the Group level.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider or Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where target device is located.&#x20;
* device\_type (str): The target device type to apply the updates.
* tag\_name (str): Name of the tag to add or update.
* tag\_value (str): Value of tag to add or update.

### Returns

* Dict: Python dictionary of the new state after updates have been applied.

### How To Use:

```python
my_api.devices.put_group_device_type_tag(
    "servivce_provider_id",
    "group_id",
    "device_type",
    tag_name= "tagName",
    tag_value= "tagValue"
)
```
