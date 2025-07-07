# GET - Group Call Center Reporting

Retrieves the reporting of a call center.

### Parameters&#x20;

* call_center_user_id (str): User ID of the target call center.

### Returns

* Dict: Reporting details

### How To Use:

```python
my_api.call_centers.get_group_call_center_reporting(
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