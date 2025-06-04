# DELETE - Group Trunk Group

Deletes a single trunk group

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is located.&#x20;
* group\_id (str): Group ID where the target Trunk Group is located.&#x20;
* trunk\_group\_name (str): Target Trunk Group Name.

### Returns

* None 

### How To Use:

```python
my_api.trunk_groups.delete_group_trunk_group(
    "ServiceProviderID",
    "GroupID",
    "trunkGroupName"
)
```