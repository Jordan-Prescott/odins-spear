from ..utils.filers import load_csv, pandas

def main(api, user_password_sheet_path: str):

    logger = api.logger
    
    logger.info(f"Initialising User/Passcode CSV Passcode Set Routine")
    data: pandas.DataFrame = None

    try:
        data = load_csv(
            user_password_sheet_path
        )
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
        user: dict = api.users.get_user_by_id(
            row["userId"]
        )

        if not user["userId"]:
            logger.error(f"Skipping Invalid User Entry | User -> {row["userId"]}")
            continue

        api.users.put_user_portal_passcode(
            user["userId"],
            row["newPasscode"]
        )

    logger.info(f"Successfully Set User Portal Passcodes")
    
    
        
    




