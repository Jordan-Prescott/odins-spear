# Scripter

The Scripter object gives you access to pre-written scripts for common tasks and features not built in Odin's web portal such as locating an alias, building webex users, pulling useful data together.

To use the Scripter object you will need to import along side the API object.

Once imported and instantiated pass in your API object. 

{% code overflow="wrap" %}
```python
from odins_spear import API, Scripter

my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

assistant = Scripter(my_api)

assistant.{script}
```
{% endcode %}

{% hint style="info" %}
For each script detail please see script documentation.
{% endhint %}
