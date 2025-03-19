# Find Alias

Locates alias if assigned to Broadworks entity.

The script searches through various entity types including Auto Attendants (AA), Hunt Groups (HG), and Call Centers (CC), as well as individual Users. It employs a retry mechanism for instances where initial attempts to fetch entity details fail.

The search is conducted in two phases:

1. Collecting details of AAs, HGs, and CCs and checking for the aliases.
2. If not found, search through the users for the alias.

If the alias is found, the method returns a dict specifying the type of entity and its name or userID. If the alias is not found after checking all entities, an AOAliasNotFound exception is raised.
If the alias is found, the method returns a dict specifying the type of entity and its name or userID. If the alias is not found after checking all entities, an AOAliasNotFound exception is raised.

The script makes use of the following methods:

```python
api.auto_attendants.get_auto_attendants()
api.auto_attendants.get_auto_attendant()
api.hunt_groups.get_group_hunt_groups()
api.hunt_groups.get_group_hunt_group()
api.call_centers.get_call_centers()
api.call_centers.get_call_center()
api.users.get_users()
```

### Parameters&#x20;

* service\_provider\_id: Service Prodiver where group is hosted.
* group\_id: Group where alias is located.
* alias: Alias number to identify e.g. 0

### Return

* dict: Returns dictionary with type, userserviceid, name and alias.

### Raise

* AOALiasNotFound: If the alias is not found AOAliasNotFound error raised

### How To Use:

{% hint style="info" %}
This method requires keyword arguments i.e. group_id="group_id"
{% endhint %}

{% code overflow="wrap" %}
```python
assistant = Scripter(my_api)

# find alias method
print(assistant.find_alias(
   service_provider_id='Service Provider ID', 
   group_id='Group ID', 
   alias=12
   )
)
```
{% endcode %}

### Formatted Output

```json
{
   "type":"HG",
   "service_user_id":"TESTHG",
   "name":"Test HG",
   "aliases":[
      "12@PROXYADDRESS"
   ]
}
```
### Formatted Output

```json
{
   "type":"HG",
   "service_user_id":"TESTHG",
   "name":"Test HG",
   "aliases":[
      "12@PROXYADDRESS"
   ]
}
```