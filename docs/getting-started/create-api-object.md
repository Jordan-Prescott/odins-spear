# Create API Object

The API object is the core object of the package, all functionality is accessed through this object. The first step is to create the object and pass it the base URL of the API, your username, and password.

{% code overflow="wrap" lineNumbers="true" %}
```python
from odins_spear import API

my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="your_password")
```
{% endcode %}

Once you have built the object the next step is to authenticate it, this authorizes the object to interact with the Odin API it is the equivalent of you logging in through the web portal. To authenticate this call the .authenticate() method on the object.

<pre class="language-python" data-overflow="wrap" data-line-numbers><code class="lang-python"><strong>from odins_spear import API
</strong>
<strong>my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")
</strong>my_api.authenticate()
</code></pre>

This method can raise an OAApiAuthenticationFail error, which means that the API has failed to authenticate and it will give you some details on potential issues. If this does not raise an error the API object is authenticated and now authorized to use all other methods.

{% hint style="info" %}
More than one object can be built for multiple odin instances.
{% endhint %}

#### Check out API object details:

{% content-ref url="../docs/api-object.md" %}
[api-object.md](../docs/api-object.md)
{% endcontent-ref %}

