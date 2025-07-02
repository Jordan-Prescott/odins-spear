# User Service Report (Filtered)

This script will pull certain information from a user report, including active Line Ports and Service Packs.


### How To Use:

{% code overflow="wrap" %}
```python
from odins_spear import API
import pandas as pd

magic = API(
    base_url="https://base_url/api/vx"",
    username="john.smith",
    password="password",
)

scripter = Scripter(my_api)
reporter = Reporter(my_api)

# CHANGE ME
Service_Provider_ID = ""
Group_ID = ""
Output_Path = "./excel.xlsx"


report = my_api.reports.get_group_report(Service_Provider_ID, Group_ID)

columns = [
    "Extension",
    "First Name",
    "Last Name",
    "Device Name",
    "MAC",
    "Lineport",
    "Service Pack",
]

data = [
    (
        user.get("extension"),
        user.get("firstName"),
        user.get("lastName"),
        user.get("accessDeviceEndpoint", {}).get("accessDevice", {}).get("deviceName"),
        user.get("accessDeviceEndpoint", {}).get("accessDevice", {}).get("macAddress"),
        user.get("userLinePorts", []),
        user.get("servicePacks"),
    )
    for user in report
]

df = pd.DataFrame(data, columns=columns)

df.to_excel(Output_Path)
```
{% endcode %}
