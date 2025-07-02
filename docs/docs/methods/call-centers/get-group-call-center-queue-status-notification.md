# GET - Group Call Center Queue Status Notification

Retrieves the queue status notifications of a call center.

### Parameters&#x20;

* call_center_user_id (str): Service user ID of the target call center.

### Returns

* Dict: Queue status notifications of the call center.

### How To Use:

```python
my_api.call_centers.get_group_call_center_queue_status_notification(
    call_center_user_id="basic_cc@domain.com"
)
```

### Example Returned Data (Formatted)
```python
{
    "enableQueueStatusNotification": true,
    "enableQueueDepthThreshold": true,
    "enableWaitingTimeThreshold": true,
    "numberOfCallsThreshold": 100,
    "waitingTimeOfCallsThreshold": 1200,
    "serviceUserId": "mock.cc.1"
}
```