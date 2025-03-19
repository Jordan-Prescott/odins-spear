# PUT - Group Call Center Agents Levels

Update a list of agents' skill levels in a single Call Center (CC).

### Parameters&#x20;

* call\_center\_user\_id (str): Service user ID of the call center users belong to.&#x20;
* agent\_user\_ids (list): List of the target users. skill\_level (int):&#x20;
* Skill level that will be applied to the list of users in the target call center.

### Returns

* Dict: CC ID and list of the agent and their updated skill level.

### How To Use:

{% code overflow="wrap" %}
```python
my_call_center = "call_center_user_id@domain.com"
my_agents = ["userid_1@domain.com", "userid_2@domain.com", "userid_3@domain.com"]

my_api.call_centers.put_group_call_center_agents_levels(
    call_center_user_id = my_call_center,
    agent_user_ids = my_agents,
    skill_level = 10
)
```
{% endcode %}
