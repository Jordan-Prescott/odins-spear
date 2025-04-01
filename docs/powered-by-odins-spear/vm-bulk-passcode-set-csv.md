# Voice Messaging Passcode Bulk Set

A specialised version of odins-spear's VM Portal Bulk Password Set Script Designed To Load A CSV Container User-Passcode Pairs

CSV Columns Must be [userId, newPasscode]

### How To Use:

```python
from odins_spear import API
import pandas

my_api= API(base_url="https://base_url/api/vx", username="john.smith", password="ODIN_INSTANCE_1")

logger = my_api.logger

logger.info(f"Initialising User/Passcode CSV Passcode Set Routine")
data: pandas.DataFrame = None

try:
    data = pandas.read_csv(user_password_sheet_path, sep=",", encoding="utf-8")
except OSError as ose:
    logger.error(f"Exception Raised When Attempting To Load CSV | Info -> {ose}")
    return

if data.empty:
    logger.info(f"Specified Sheet Is Empty | Path -> {user_password_sheet_path}")
    return

required_columns = {"userId", "newPasscode"}

if not required_columns.issubset(data.columns):
    logger.error(f"Missing Required Headers | Columns -> {required_columns - set(data.columns)}")
    return

for index, row in data.iterrows():
    
    # Sanity Check Valid User
    user: dict = my_api.users.get_user_by_id(
        row["userId"]
    )

    if not user["userId"]:
        logger.error(f"Skipping Invalid User Entry | User -> {row["userId"]}")
        continue

    my_api.users.put_user_portal_passcode(
        user["userId"],
        row["newPasscode"]
    )

logger.info(f"Successfully Set User Portal Passcodes\n")

```

    




