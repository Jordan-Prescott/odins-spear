# API Class Documentation

The `API` class is the main interface for interacting with the Odin API. It provides authentication, session management, and access to various entities within the API.

---

## Initialization

### Constructor
```python
API(base_url: str, username: str, password: str, rate_limit: bool = True)
```

#### Parameters:
- `base_url` (`str`): The base URL of your Odin instance API.
- `username` (`str`): The username used for authentication.
- `password` (`str`): The password used for authentication.
- `rate_limit` (`bool`): Enables (True) or disables (False) rate limiting to 5 calls per second. Defaults to `True`.

---

## Attributes

- `base_url`: The base URL of the API.
- `username`: The username used for authentication.
- `rate_limit`: Indicates if rate limiting is enabled.
- `authorised`: Boolean indicating if the API is authenticated.
- `token`: The token string returned from the Odin API upon successful authentication.

---

## Rate Limiting

The `API` class includes built-in rate limiting functionality to ensure compliance with API usage policies and prevent overloading the server. By default, the rate limit is set to **5 calls per second**.

### Enabling or Disabling Rate Limiting

The `rate_limit` functionality can be controlled through the `rate_limit` parameter when initializing the `API` class or by updating the configuration later.

---

### **Enable Rate Limiting**
To enable rate limiting (default behavior):
```python
from odins_spear import API

api = API(
    base_url="https://api.odin.com",
    username="my_user",
    password="my_pass",
    rate_limit=True  # Enable rate limiting
)
```

---

## Methods

### 1. `_authenticate`
```python
_authenticate() -> bool
```
Private method that authenticates the session with the provided `username` and `password`.

#### Raises:
- `OSApiAuthenticationFail`: If authentication fails.

#### Returns:
- `bool`: `True` if authentication is successful.

---

### 2. `refresh_authorisation`
```python
refresh_authorisation() -> bool
```
Re-authenticates the session to refresh the API token.

#### Raises:
- `OSSessionRefreshFail`: If re-authentication fails.

#### Returns:
- `bool`: `True` if re-authentication is successful.

---

### 3. `get_auth_details`
```python
get_auth_details() -> dict
```
Retrieves the current session details.

#### Raises:
- `OSFailedToLocateSession`: If session details cannot be retrieved.

#### Returns:
- `dict`: The session details.

---

### 4. `update_api`
```python
update_api(
    base_url: str = None, 
    username: str = None, 
    password: str = None, 
    rate_limit: bool = None,
    logger: object = None
)
```
Updates the API instance with new configuration details.

#### Parameters:
- `base_url` (`str`, optional): The new base URL.
- `username` (`str`, optional): The new username.
- `password` (`str`, optional): The new password.
- `rate_limit` (`bool`, optional): The new rate limit setting.
- `rate_limit` (`object`, optional): The new logger object.

---

## Example Usage

### Initializing the API:
```python
from odins_spear import API

# create your own logger 

api = API(
    base_url="https://api.odin.com",
    username="my_user",
    password="my_pass",
    rate_limit=True,
    logger=logger
)
```

### Authenticating:
```python
if api.authenticate():
    print("Authentication successful!")
```

### Updating API Configuration:
```python
api.update_api(base_url="https://new.api.odin.com", username="new_user")
```

---

## Notes
- Ensure your credentials and API endpoint are correct before initializing the `API` object.
- Use the provided methods to interact with various entities like users, call records, and administrators.
