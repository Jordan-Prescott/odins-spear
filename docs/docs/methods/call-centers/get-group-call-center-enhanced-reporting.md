# GET - Group Call Center Enhanced Reporting

Retrieves the enhanced reporting of a call center.

### Parameters&#x20;

* call_center_user_id (str): Service user ID of the target call center.

### Returns

* Dict: Enhanced reporting details

### How To Use:

```python
my_api.call_centers.get_group_call_center_enhanced_reporting(
    call_center_user_id="basic_cc@domain.com"
)
```

### Example Returned Data (Formatted)
```python
{
    "generateDailyReport": false,
    "collectionPeriodMinutes": 30,
    "statisticsSource": "Application Server",
    "serviceUserId": "mock.cc.1@microv-works.com"
}
```