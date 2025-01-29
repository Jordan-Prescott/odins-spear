# Formatters Documentation

The `formatters.py` module provides utility functions for formatting filter values, phone numbers, and service instance profiles. These functions ensure consistency when handling formatted data within the API.

## **Functions**

### **format_filter_value**
Formats a filter value according to the specified filter type by adding the appropriate wildcards.

#### **Function Signature**
```python
def format_filter_value(filter_type: str, filter_value: str) -> str
```

#### **Parameters**
- `filter_type` (*str*): The type of filter operation (`"equal to"`, `"contains"`, `"starts with"`).
- `filter_value` (*str*): The value to filter for.

#### **Raises**
- `OAUnsupportedFilter`: Raised when an unsupported filter type (e.g., `"ends with"`) is requested.

#### **Returns**
- (*str*): The formatted filter value with the appropriate wildcard(s).

#### **Example Usage**
```python
from odins_spear.utils.formatters import format_filter_value

formatted_value = format_filter_value("contains", "example")
print(formatted_value)  # Output: *example*
```

---

### **format_int_list_of_numbers**
Formats a list of integer phone numbers by prepending a specified country code.

#### **Function Signature**
```python
def format_int_list_of_numbers(country_code: int, numbers: List[int]) -> List[str]
```

#### **Parameters**
- `country_code` (*int*): The country code to prepend to each number.
- `numbers` (*List[int]*): A list of phone numbers (integers) without a country code.

#### **Returns**
- (*List[str]*): A list of formatted phone numbers with the country code prepended.

#### **Example Usage**
```python
from odins_spear.utils.formatters import format_int_list_of_numbers

formatted_numbers = format_int_list_of_numbers(44, [123456789, 987654321])
print(formatted_numbers)  # Output: ["44-123456789", "44-987654321"]
```

---

### **format_service_instance_profile**
Ensures that the `serviceInstanceProfile` key exists in the given dictionary, initializing it as an empty dictionary if absent.

#### **Function Signature**
```python
def format_service_instance_profile(data: Dict) -> Dict[str, Any]
```

#### **Parameters**
- `data` (*Dict*): The input dictionary to check for the `serviceInstanceProfile` key.

#### **Returns**
- (*Dict[str, Any]*): The original dictionary with `serviceInstanceProfile` ensured as a key.

#### **Example Usage**
```python
from odins_spear.utils.formatters import format_service_instance_profile

data = {"user": "John Doe"}
formatted_data = format_service_instance_profile(data)
print(formatted_data)  # Output: {"user": "John Doe", "serviceInstanceProfile": {}}
```

---

This module ensures that formatted values adhere to expected structures, reducing the likelihood of errors when interacting with the API.

