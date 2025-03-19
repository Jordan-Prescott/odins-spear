# GET - Service Provider

Retrieves a list of every Service Provider / Enterprise.

### Parameters&#x20;

* reseller_id (str): Only list the Service Provider IDs within the specified Reseller.&#x20;

### Returns

* List: A List of every Service Provider, alongside their resellerID

### How To Use:

The following code snippet demonstrates how to fetch a list of all Service Providers:

{% code overflow="wrap" %}
```python
my_api.service_providers.get_service_providers()
```
{% endcode %}

### Example Returned Data of Device (Formatted)

```json
[
  {
    "serviceProviderId": "SERVICE123",
    "serviceProviderName": "ServiceProv 1",
    "isEnterprise": true
  },
  {
    "serviceProviderId": "SERVICE321",
    "serviceProviderName": "ServiceProv 2",
    "isEnterprise": false
  }
]
```