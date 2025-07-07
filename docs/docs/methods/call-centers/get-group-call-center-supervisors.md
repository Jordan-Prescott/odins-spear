# GET - Group Call Center Supervisors

Retrieves the supervisors of a call center.

### Parameters&#x20;

* call_center_user_id (str): User ID of the target call center.

### Returns

* Dict: Supervisors of call center.

### How To Use:

```python
my_api.call_centers.get_group_call_center_supervisors(
    call_center_user_id="basic_cc@domain.com"
)
```

### Example Returned Data (Formatted)
```python
{
    "serviceUserId": "mock.cc.1@microv-works.com",
    "supervisors": [
        {
            "userId": 9709580001,
            "lastName": "Mock1",
            "firstName": "Mock1",
            "hiraganaLastName": "Mock1",
            "hiraganaFirstName": "Mock1",
            "phoneNumber": "+1-9709580001",
            "extension": "0001",
            "department": "Odin Mock Dept (odin.mock.grp1)",
            "emailAddress": null
        },
        {
            "userId": 9709580002,
            "lastName": "User2last",
            "firstName": "User2first",
            "hiraganaLastName": "User2last",
            "hiraganaFirstName": "User2first",
            "phoneNumber": "+1-9709580002",
            "extension": "0002",
            "department": "Odin Mock Dept (odin.mock.grp1)",
            "emailAddress": null
        }
    ]
}
```