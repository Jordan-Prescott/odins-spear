# What's New

Welcome to the **What's New** page! Stay updated with the latest features, improvements, and changes in our package.

---

## v2.0.0

### 🆕 New Features

#### 1. Restructured Entity-Based Methods
- The code has been restructured from `api.get.method` to `api.entity.method`.
- For example, instead of `api.get.method`, you can now use `api.user.get_user_by_id`.
- This change aligns more closely with Odin's API documentation, making it easier for end users to work with.

#### 2. ConfigManager Class
- Introduced the `ConfigManager` class to manage and pull default configurations for core entities.
- Users can easily retrieve, update, and use these configurations in their workflows.

#### 3. Custom Logger Support
- The `API` class now includes a `logger` parameter.
- Users can pass in their preferred logger (e.g., `logging`, `loguru`, or `Sentry`) to customize logging throughout the package.

### 📚 Documentation

- The documentation has been **completely renewed** to reflect all updates in this release.
- Examples and usage patterns have been updated for consistency with the new structure.

### 🛠 Improvements

#### 1. Simplified Import Structure
- The internal structure has been updated for a better user experience.
- You can now simply import the API class with:
    ```python
    from odins_spear import API, Scripter, Reporter
    ```