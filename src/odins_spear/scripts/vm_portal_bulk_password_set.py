def main(api, service_provider_id: str, group_id: str, new_password: str):

    logger = api.logger

    user_list = api.users.get_users(
        service_provider_id,
        group_id
    )

    assigned_password = new_password if new_password else api.get_sip_password_generate()

    logger.info(f"Defaulting To Default Bulk Portal Passcode Set Routine | Password -> {assigned_password} | Users Affected -> {user_list.__len__()}")
    for user in user_list:
        
        # Verify We Have Retrieved An Applicable User
        if user is None or user["userId"] is None:
            logger.error("Failed To Parse User Entry In User List")
            continue

        logger.info(f"Setting Portal Passcode For User -> {user["userId"]}")
        api.users.put_user_portal_passcode(
            user["userId"],
            assigned_password
        )

    logger.info("Successfully Set Group User Portal Passcodes")
        
    




