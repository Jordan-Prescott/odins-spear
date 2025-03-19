# PUT - Group Hunt Groups Status

Updates a list of Hunt Groups (HG) status to either active or inactive.

### Parameters&#x20;

* service\_user\_ids (list): List of service user IDs of target HGs.&#x20;
* status (bool, optional): Status to apply to target HGs. Defaults to True.

### Returns

* None: This method does not return any specific value.

### How To Use:

```python
my_hunt_group_user_ids= [
    "hunt_group1@domain.com",
    "hunt_group2@domain.com"
]

my_api.hunt_groups.put_group_hunt_groups_status(
    call_centhunt_group_user_ids = my_hunt_group_user_ids,
    status = True
)
```
