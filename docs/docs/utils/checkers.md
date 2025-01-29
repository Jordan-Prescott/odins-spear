# Checkers Documentation

The `checkers.py` module provides validation functions to ensure that filters and filter types used in API requests are supported. It prevents unsupported queries by raising appropriate exceptions.

## **Functions**

### **check_type_filter**
Validates whether a given filter attribute and filter type are supported.

#### **Function Signature**
```python
def check_type_filter(filter_by: str, filter_type: str) -> None
```

#### **Parameters**
- `filter_by` (*str*): The attribute to filter by (e.g., `"firstName"`, `"emailAddress"`).
- `filter_type` (*str*): The filter operation to apply (e.g., `"contains"`, `"equals"`).

#### **Raises**
- `OSUnsupportedFilter`: Raised if the `filter_by` attribute is not in the supported filters list.
- `OSUnsupportedFilterType`: Raised if the `filter_type` is not in the supported filter types list.

#### **Supported Filters**
The following attributes can be used as filters:
```python
supported_filters = [
    "macAddress",
    "lastName",
    "firstName",
    "dn",
    "emailAddress",
    "userId",
    "extension",
]
```

#### **Supported Filter Types**
The following operations are supported for filtering:
```python
supported_filter_types = [
    "contains",
    "startsWith",
    "endsWith",
    "equals",
]
```

## **Usage Example**
To validate a filter before making an API request:
```python
from odins_spear.utils.checkers import check_type_filter

# Example: Checking a valid filter and type
try:
    check_type_filter("firstName", "contains")
    print("Filter is valid.")
except (OSUnsupportedFilter, OSUnsupportedFilterType) as e:
    print(f"Invalid filter: {e}")

# Example: Checking an invalid filter
try:
    check_type_filter("age", "equals")  # 'age' is not in supported_filters
except OSUnsupportedFilter as e:
    print(f"Error: {e}")  # Raises OSUnsupportedFilter
```

This module ensures that only valid filters and filter types are used, reducing the risk of API errors.

