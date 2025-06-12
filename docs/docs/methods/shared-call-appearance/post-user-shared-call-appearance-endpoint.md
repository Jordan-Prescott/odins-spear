# POST - User Shared Call Appearance Endpoint

Creates a new Shared Call Apprance (SCA) on a single user.

### Parameters&#x20;

* service\_provider\_id (str): Service Provider/ Enterprise ID where Group is hosted.&#x20;
* group\_id (str): Target Group ID where users are located.
* device\_name (str): Device to add for SCA from available devices.

### Returns

* Dict: New SCA details applied to user.

### How To Use:

```python
my_api.post_user_shared_call_appearance_endpoint(
        "user@domain.com, 
        "line1", 
        "dev1"
    ):
```

### Example Data Returned (Formatted)

```python
{
	"userId":"user@domain.com",
	"linePort":"line@domain",
	"isActive":true,
  "allowOrigination":true,
	"allowTermination":true,
	"deviceName":"dev1",
	"deviceLevel":"Group"
}
```
