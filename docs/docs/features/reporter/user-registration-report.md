# User Registration Report

Generates an Excel Xlsx file which contains the User Id, Device Name, and Registration status of all Users within the specified group.

{% hint style="info" %}
This feature can be run without the output of an Excel sheet: api.scripter.user_registration()&#x20;
{% endhint %}


### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise where group is hosted.&#x20;
* group\_id (str): Target Group you would like to pull the registration of users for.&#x20;

### Return

* None: This will generate an Xlsx File into .os_reports/ named "Registration_report_for_(GroupID)"

The script makes use of the following methods:

```python
api.scripter.user_registration()
```

### How To Use:
{% hint style="info" %}
This method requires keyword arguments i.e. group_id="group_id"
{% endhint %}

{% code overflow="wrap" %}
```python
from odins_spear import API, Reporter

my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()


assistant = Reporter(my_api)

assistant.user_registration_report(
    service_provider_id="serviceProviderID",
    group_id="groupID",
)

```
{% endcode %}

