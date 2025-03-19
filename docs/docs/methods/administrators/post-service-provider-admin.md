# POST - Service Provider Admin

Builds Service Provider level administrattor.

### Parameters&#x20;

* service\_provider\_id (str): Target service parovider to build account.
* user\_id (str): User ID of new account i.e. 'firstname.lastname@domain.com'
* password (str): Web access password user needs to log in.
* first\_name (str): First name.
* last\_name (str): Last name.
* language (str, optional): Find supported languages on your system. Defaults to "English".
* admin\_type (str, optional): Type of admin, options: 'normal', 'customer', 'password reset only'. Defaults to normal.
* payload (dict, optional): Payload sent to API. Defaults to empty dict and is formatted for you.

### Returns

* None

### How To Use:

```python
my_api.administrators.post_service_provider_admin(
	service_provider_id="serviceProvider", 
	user_id="user.id", 
	password="Adn67asdKNO29", 
	first_name="firstName", 
	last_name="lastName",
	language="English",
	admin_type="Password Reset Only"
)

```
{% endcode %}