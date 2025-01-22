# What’s New in Odin’s Spear v2.0.0
**Date**: 22.01.25

We’re thrilled to announce the release of Odin’s Spear v2.0.0! This major update introduces significant enhancements, including a restructured codebase, refined features, and an improved import structure. Below, we’ve outlined the key changes and improvements in this release.

---

## Key Updates

### 1. Codebase Restructuring
- The codebase has been restructured to improve maintainability and modularity.
- API calls have been reorganised for better readability and usage.
  - Example: The previous call `api.get.users` is now accessed as `api.users.get_users`.

### 2. Refined Feature List
- Certain features, including `aa_cc_hg_audit` and `service_pack_audit`, have been removed from the core library.
- These features are now documented in detail in our **Docs** for reference.

### 3. Improved Import Structure
- Importing the library has been simplified:
  - **Old:** `from odins_spear.Api import Api`
  - **New:** `from odins_spear import API, Scripter, Reporter`
- **Scripter** and **Reporter** now require the `API` object to be passed in as a parameter.

### 4. Password Handling
- Passwords are no longer stored as environment variables. Instead, they are passed directly as the user’s password.
- **Security Tip:** We strongly recommend securing your password appropriately when using it with the API.

### 5. New `api.update_api` Method
- A new method, `api.update_api`, has been introduced to allow you to dynamically update:
  - `base_url`
  - `username`
  - `password`
  - `rate_limit`
- This ensures that all dependent components are updated seamlessly.

### 6. Keyword Arguments for Scripter and Reporter
- **Scripter** and **Reporter** now support keyword-only arguments for improved clarity and flexibility.

### 7. Extended Utilities
- **Constants:** A new `utils.constants` module has been added, containing predefined service packs and services for BWKS.
- **Configurations:** The `utils/configs` module now includes JSON configurations for common BWKS entities:
  - `user`
  - `hunt group`
  - `call centre`
- These configurations can be easily read and customised before sending API requests.
