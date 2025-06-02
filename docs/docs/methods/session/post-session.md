# POST - Session

Creates new session - returns access token needed for additional calls

Note: API object handles this.

### Parameters

* username (str): Odin instance username
* password (str): Odin instance password

### Returns

* Dict: New token for additional calls

### How To Use:

```python
from odins_spear import API

api = API(
  "url",
  "username",
  "password"
)
```

### Example Data Returned (Formatted)

```python
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwYXJrYmVuY2hzb2x1dGlvbnMuY29tIiwiaWF0IjoxNTQ2ODg5NDU0LCJuYnAiOjE1NDY4ODk0NTQsImV4cCI6MTU0NjkzMjY1NCwiZGF0YSI6ImV5SnBkaUk2SWpoeFpVWnhjVEZITWxwVFNtODVhV2NySzB0VlQwRTlQU0lzSW5aaGJIVmxJam9pUzJGVFZWRjJObkJDZDFjeE5WQmNMMUJUUjBWTVdHTjRWRVpoV2pNclkwSk5iVEphU2pneFVURnpNVGc1TjBwYVdrNWFjVkZDV25od1ZUUlRaMHhvY0dReE5IRlVlVGswZHpWcGNsRjJSMnB6YkdKSE5rdzNhVzFYVVZkU2EydFlhR1Z3U1d0Wk1Gd3ZLMnN6WnowaUxDSnRZV01pT2lJMFlqRmhPREk0WTJVM05tRXdOR0prWm1Kak16azVNMk0xTkRVMk5qRXpaV015TlRBNE9EVTBNelprTXpFNFpUZ3pNV0ptWWpGbE56UTVPVFl4WkdNNUluMD0ifQ.6YCC4jVoWzzIjhOjgXC8dTQd7rGkFSwZBan-UlkzUy0"
}
```
