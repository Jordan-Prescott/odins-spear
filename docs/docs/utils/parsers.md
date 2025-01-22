
# Parsers Documentation

The `parsers.py` module provides utility functions for working with JSON data, simplifying the process of converting JSON strings to dictionaries and vice versa.

## **Available Functions**

### **1. json_to_dictionary**
Converts a JSON string into a Python dictionary.

**Signature:**
```python
def json_to_dictionary(json_data: str) -> dict
```

**Parameters:**
- `json_data` (str): JSON data in string format.

**Returns:**
- `dict`: A Python dictionary representation of the JSON data.
- `None`: If an error occurs during decoding.

**Usage Example:**
```python
from odins_spear.utils.parsers import json_to_dictionary

json_string = '{"key": "value"}'
python_dict = json_to_dictionary(json_string)

print(python_dict)  # Output: {'key': 'value'}
```

### **2. dictionary_to_json**
Converts a Python dictionary into a JSON string.

**Signature:**
```python
def dictionary_to_json(python_dict: dict) -> str
```

**Parameters:**
- `python_dict` (dict): A Python dictionary.

**Returns:**
- `str`: JSON data in string format.
- `None`: If an error occurs during encoding.

**Usage Example:**
```python
from odins_spear.utils.parsers import dictionary_to_json

python_dict = {"key": "value"}
json_string = dictionary_to_json(python_dict)

print(json_string)  # Output: {"key": "value"}
```

## **Error Handling**
- **`json_to_dictionary`**: Returns `None` and prints an error message if the JSON string is invalid.
- **`dictionary_to_json`**: Returns `None` and prints an error message if the dictionary cannot be converted.

---

## Summary

The `parsers.py` module provides essential utilities for handling JSON data. It simplifies conversion tasks, making it easier to integrate JSON handling into your BroadWorks workflows.

For further assistance or suggestions, feel free to reach out!
