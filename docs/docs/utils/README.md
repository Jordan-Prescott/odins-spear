# Utils Module Overview

Welcome to the `utils` module! This module is designed to provide essential utilities that simplify and enhance your workflow with Odin's Spear. Whether you're managing configurations, handling JSON data, or working with predefined constants, the `utils` module offers a set of tools to make your development experience more efficient.

---

## **What’s Inside the Utils Module?**

The `utils` module is structured to support various common operations required when interacting with BroadWorks APIs. Here's what you’ll find:

### **1. Constants**
The `constants.py` file contains predefined lists of:
- Supported filters and filter types for searches.
- Group services and user services in BroadWorks.

These constants help ensure consistency and reduce the need for hardcoding values.

### **2. Parsers**
The `parsers.py` file provides utility functions for:
- Converting JSON strings to Python dictionaries.
- Converting Python dictionaries to JSON strings.

These functions make it easier to handle and manipulate data in JSON format, a key requirement for interacting with APIs.

### **3. Configurations (Coming Soon)**
Predefined JSON templates for common BroadWorks entities. These configurations will help you structure API requests with ease. Stay tuned for details on how to use them effectively!

---

## **Why Use the Utils Module?**

The `utils` module is here to:
- Save you time by offering ready-to-use constants and templates.
- Provide reliable tools for working with JSON data.
- Standardise your workflows with BroadWorks APIs.

---

## **Getting Started**

To use the `utils` module, you simply need to import the required components into your project. Examples and detailed documentation for each utility are provided in their respective sections.

### Example:
Here’s how you might import and use a utility:
```python
from odins_spear.utils.parsers import json_to_dictionary
from odins_spear.utils.constants import supported_filters

# Convert a JSON string to a dictionary
json_data = '{"key": "value"}'
data = json_to_dictionary(json_data)

# Print supported filters
print(supported_filters)
