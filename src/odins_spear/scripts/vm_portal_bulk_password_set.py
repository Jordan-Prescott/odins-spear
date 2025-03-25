def main(api, service_provider_id: str, group_id: str, new_password: str):

    logger = api.logger

    user_list: list = api.users.get_users(
        service_provider_id,
        group_id
    )

    logger.info(f"Defaulting To Default Bulk Portal Passcode Set Routine | Password -> {new_password} | Users Affected -> {user_list.__len__()}")
    for user in user_list:
        
        if user is None or user["userId"] is None:
            logger.error("Failed To Parse User Entry In User List")
            continue

        logger.info(f"Setting Portal Passcode For User -> {user["userId"]}")
        api.users.put_user_portal_passcode(
            user["userId"],
            new_password
        )

    logger.info(f"Successfully Set Group User Portal Passcodes")
        
    




