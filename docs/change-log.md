# Change Log

## v2.2.0 
**Date**: 19.03.25

### Added 
- Enhanced Logging 
  - The tool now includes detailed logging to improve debugging and monitoring.  
  - By default, it will use its own built-in logger.  
  - Users can now supply their own logger as a parameter to the `API` object.  

- Streamlined Authentication
  - The `.authenticate()` method is no longer required after instantiating the `API` class.  
  - Authentication is now handled internally, making integration simpler and more efficient.  

- Announcement Endpoint Added
  - Users can now upload, delete, and modify announcements via the new announcement endpoint.  
  - Supported actions include:  
    - Uploading WAV files  
    - Updating or changing existing announcements  
    - Deleting outdated announcements  

- New ConfigManager for API Templates  
  - Introducing ConfigManager, a new feature that provides template configurations for API calls.  
  - Users can now:  
    - Retrieve sections or entire configs for common BroadWorks entities like:  
      - User  
      - Call Center  
      - Hunt Groups  
  - This simplifies configuration management and improves workflow efficiency.  

### Fixed
- Find Alias Now Handles All Characters
  - Previously, searching for aliases containing special characters (e.g., `*3`) would fail.  
  - This issue has been resolved, and the search function now correctly processes all characters.  

---

### v2.0.0 
**Date**: 22.01.25

#### Added
- `api.update_api` method for updating core API settings dynamically.
- `utils.constants` with service packs and services for BWKS.
- `utils/configs` for predefined JSON configurations of common BWKS entities.

#### Changed
- Codebase restructured for modularity:
  - API calls reorganised (e.g., `api.get.users` → `api.users.get_users`).
- Import structure improved:
  - New import format: `from odins_spear import API, Scripter, Reporter`.
- **Scripter** and **Reporter** now require keyword-only arguments.
- Password handling updated to use the user’s password directly (no longer an environment variable).

#### Removed
- `aa_cc_hg_audit` and `service_pack_audit` features moved to documentation for reference.
