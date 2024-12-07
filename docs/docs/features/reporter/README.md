# Reporter

Reporter generates human friendly reports and graphs of your Broadworks instance. This can show Broadworks entity call volume over a period of time or a call flow chart showing how calls flow through your system when calling a specific number.&#x20;

To use Reporter import along with the API object and pass your API object as a parameter. 

{% hint style="info" %}
To make use of the features that generate graphs and charts such as Call Flow you will need to install Graphviz [here](https://graphviz.org/download/).
{% endhint %}

{% code overflow="wrap" %}
```python
from odins_spear import API, Reporter

my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
my_api.authenticate()

assistant = Reporter(my_api)

assistant.{report}
```
{% endcode %}

{% hint style="info" %}
For each script detail please see script documentation.
{% endhint %}