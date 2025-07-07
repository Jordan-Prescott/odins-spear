# GET - Group Call Center Statistics

Retrieves the statistics of a call center.

### Parameters&#x20;

* call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
* start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
* end_date (str): End date of desired time period. Date must follow format 'YYYY-MM-DD'
* start_time (str): Start time of desired time period. Time must follow formate 'HH:MM:SS'.
* end_time (str): End time of desired time period. Time must follow formate 'HH:MM:SS'.
* time_zone (str): A specified time you would like to see call records in. Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).



### Returns

* Dict: Statistics of call center.

### How To Use:

```python
my_api.call_centers.get_group_call_center_statistics(
    call_center_user_id="basic_cc@domain.com",
    start_date="2025-01-01",
    end_date="2025-01-02",
    start_time="00:00:00",
    end_time="23:59:59",
    time_zone="Z"
)
```

### Example Returned Data (Formatted)
```python
{
    "statisticsRange": {
        "start": "2018-10-08T01:00:00.000-06:00",
        "end": "2018-10-09T01:00:00.000-06:00"
    },
    "queueStatistics": {
        "numberOfBusyOverflows": "0",
        "numberOfCallsAnswered": "0",
        "numberOfCallsAbandoned": "0",
        "numberOfCallsTransferred": "0",
        "numberOfCallsTimedout": "0",
        "averageNumberOfAgentsTalking": "0.0",
        "averageNumberOfAgentsStaffed": "0.0",
        "averageWaitSeconds": "0",
        "averageAbandonmentSeconds": "0"
    },
    "agentStatistics": {
        "agentUserId": "9709580001",
        "agentDisplayNames": {
            "lastName": "Mock1",
            "firstName": "Mock1",
            "hiraganaLastName": "Mock1",
            "hiraganaFirstName": "Mock1"
        },
        "available": "false",
        "statistics": {
            "numberOfCallsHandled": "0",
            "numberOfCallsUnanswered": "0",
            "averageCallSeconds": "0",
            "totalTalkSeconds": "0",
            "totalStaffedSeconds": "0"
        }
    }
}
```