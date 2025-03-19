# PUT - User Do Not Disturb

This method updates the Do Not Disturb (DND) and Ring Splash (RS) status of a single. It takes a single User ID of the target user you would like to retrieve the status of.&#x20;

### Parameters&#x20;

* user\_id (str): Target user id of user you would like to update the state of.
* dnd\_active (bool): True to enable DND and False to disable DND. Defaults to False.
* ring\_splash\_active (bool): True to enable Ring Splash and False to disable Ring Splash. Defaults to False

### Returns

* Dict: Target users DND/ RS status. True is enabled and False disabled.

### How To Use:

```python
my_api.do_not_disturb.put_user_do_not_disturb(
        user_id='UserID',
        dnd_active= True
        ring_splash_active= True     
)
```

## Examples Data (Formatted)

```python
{
  "isActive": true,
  "ringSplash": true,
  "userId": "9709580001@microv-works.com"
}
```
