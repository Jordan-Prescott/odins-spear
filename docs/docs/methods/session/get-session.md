# GET - Session

Fetches session information for currently logged in user

### Returns

* Dict: Session details

### How To Use:

```python
my_api.session.get_session()
```

### Example Data Returned (Formatted)

```python
{
  "userId": "mock.user@as3.xdp.broadsoft.com",
  "groupId": null,
  "serviceProviderId": null,
  "isEnterprise": false,
  "loginType": "Provisioning",
  "userDomain": "as3.xdp.broadsoft.com",
  "passwordExpiresDays": 2147483647,
  "local": "en_US",
  "encoding": null,
  "systemDomain": "as3.xdp.broadsoft.com",
  "softwareVersion": "21sp1",
  "isSystemAdmin": true,
  "readOnly": false,
  "policy": [],
  "version": "latest"
}
```
