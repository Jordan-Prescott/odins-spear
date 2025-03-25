# VM Portal Bulk Password Set CSV

using CSV as input, it will iterate through all the UserIDs and set the VM password specified in the CSV against the user.

### Parameters&#x20;

* user\_password\_sheet\_path (str): Filepath to dedicated CSV/Spreadsheet containing user/password pairs for setting

### Return

* None: This routine has no specified return type

### How To Use:

{% code overflow="wrap" %}
```python
assistant = Scripter(my_api)

assistant.vm_portal_bulk_password_set_csv(
    "folder1/folder2/userpasswords.csv"
)
```
{% endcode %}
