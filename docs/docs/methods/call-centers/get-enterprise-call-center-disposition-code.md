# GET - Enterprise Call Center Disposition Code

Retrieves a single disposition code of specified service provider.

### Parameters&#x20;

* service_provider_id (str): Target Service Provider ID
* disposition_code (str): Target Disposition Code

### Returns

* Dict: Details on disposition code..

### How To Use:

```python
my_api.call_centers.get_enterprise_call_center_disposition_code(
    service_provider_id="ent.odin",
    disposition_code="1001"
)
```
