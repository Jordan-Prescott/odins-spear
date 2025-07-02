# GET - Group Call Center Queue Status

Retrieves the queue status of a call center.

### Parameters&#x20;

* call_center_user_id (str): Service user ID of the target call center.

### Returns

* Dict: Queue status of the call center.

### How To Use:

```python
my_api.call_centers.get_group_call_center_queue_status(
    call_center_user_id="basic_cc@domain.com"
)
```

### Example Returned Data (Formatted)
```python
{
    "numberOfCallsQueuedNow": 0,
    "agentsCurrentlyStaffed": [],
    "serviceUserId": "mock.cc.1@microv-works.com"
}
```