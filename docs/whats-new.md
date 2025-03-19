# What’s New in Odin’s Spear
**Date**: 19.03.25

# What's New in v2.2.0  

Welcome to the latest release of our tool. This update brings enhanced logging, streamlined authentication, new announcement endpoint capabilities, and a powerful ConfigManager. Read on to explore what’s new.  

---

## New Features & Improvements  

### Enhanced Logging  
- The tool now includes detailed logging to improve debugging and monitoring.  
- By default, it will use its own built-in logger.  
- Users can now supply their own logger as a parameter to the `API` object.  

### Streamlined Authentication  
- The `.authenticate()` method is no longer required after instantiating the `API` class.  
- Authentication is now handled internally, making integration simpler and more efficient.  

### Announcement Endpoint Added  
- Users can now upload, delete, and modify announcements via the new announcement endpoint.  
- Supported actions include:  
  - Uploading WAV files  
  - Updating or changing existing announcements  
  - Deleting outdated announcements  

### New ConfigManager for API Templates  
- Introducing ConfigManager, a new feature that provides template configurations for API calls.  
- Users can now:  
  - Retrieve sections or entire configs for common BroadWorks entities like:  
    - User  
    - Call Center  
    - Hunt Groups  
- This simplifies configuration management and improves workflow efficiency.  

