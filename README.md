# ⚔️ Odin's Spear

Officially adopted by [Fourteen IP Communications](https://fourteenip.com/) leading supplier of hosted telephony in the hospitality industry. 

![Odin's Spear Logo](https://github.com/Jordan-Prescott/odins_spear/blob/main/assets/images/logo.svg)
[![Downloads](https://static.pepy.tech/badge/odins-spear)](https://pepy.tech/project/odins-spear)
[![Downloads](https://static.pepy.tech/badge/odins-spear/month)](https://pepy.tech/project/odins-spear)
[![Downloads](https://static.pepy.tech/badge/odins-spear/week)](https://pepy.tech/project/odins-spear)
[![pypi version](https://img.shields.io/pypi/v/odins-spear.svg)](https://pypi.python.org/pypi/odins-spear)
## Overview

Odin's Spear is a Python library designed to streamline and enhance your experience with Odin's API by [Rev.io](https://www.rev.io/blog/solutions/rev-io-odin-api). If you've worked with BroadWorks for years and struggled with its outdated interface and limitations, Odin's API feels like a breath of fresh air—offering a modern user interface, automation, and comprehensive API access.

With Odin's Spear, managing users, hunt groups, call centers, and other telecom operations becomes significantly easier. This library encapsulates Odin's API functionality, making it accessible, efficient, and user-friendly.

## Features

- **Bulk User Management:** Create and manage thousands of users, hunt groups, and call centers in minutes.
- **Error Handling:** Automatically manage authentication, request design, and error handling.
- **Advanced Tools:** Features like call flow visualization, group audit reports, and bulk management of telecom entities.
- **Alias Assignment Locator:** The first feature release addresses a long-standing issue by allowing you to easily locate where an alias is assigned within BroadWorks—saving you time and frustration.

## Why Odin's Spear?

Working with BroadWorks for over five years was a challenge, with its 90s-style UI and rigid functionality. When Rev.io introduced Odin, with its modern interface and API, it revolutionized how telecom management could be done. However, even with these advancements, some tasks remained cumbersome, like locating alias assignments. 

Odin's Spear is the solution. It simplifies your workflow by automating repetitive tasks, handling errors, and making API interactions as smooth as possible. Whether you're managing 10 users or 10,000, Odin's Spear has you covered.

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- An Odin account

### Installation

Install Odin's Spear using pip:

```bash
pip install odins-spear
```

### Basic Usage

Here's a simple example to get you started:

```python
from odins_spear import API, Scripter, Reporter

# Initialize the API with your credentials
my_api = API(base_url="https://base_url/api/vx", username="john.smith", password="Your Password")
my_api.authenticate()

my_assistant = Scripter(my_api)
# Locate an alias assignment
alias_info = my_assistant.find_alias('ServiceProviderID', 'GroupID', alias=0)

my_assitant = Reporter(my_api)
# Generate call flow visual
my_assistant.call_flow(
    'serviceProviderId',
    'groupId',
    '3001',
    'extension',
    'auto_attendant'
)
```

For more detailed usage and examples, check out our [Documentation](#-documentation).

## 📖 Documentation

We provide extensive documentation to help you get started quickly and take full advantage of Odin's Spear's capabilities:

- [Odin's Spear Documentation](https://docs.jordan-prescott.com/odins_spear)

## Contributing

We welcome contributions! If you'd like to contribute, please fork the project, make your changes then submit a pull request. 
For issues to work on please see our [project](https://github.com/users/Jordan-Prescott/projects/2).

## License

This project is licensed under the MIT License—see the [LICENSE.md](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub.

## Acknowledgements

Special thanks to the developers at Rev.io for creating the Odin API and to the engineers who provided invaluable feedback and feature suggestions.

