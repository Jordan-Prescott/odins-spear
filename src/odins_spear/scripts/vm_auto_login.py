def main(api, service_provider_id: str, group_id: str, users: list[str]):

    logger = api.logger

    user_list: list = []

    try:

        if not users:
            user_list = api.users.get_users(
                service_provider_id,
                group_id
            )
        else:
            user_list = users

    except KeyError as ke:
        logger.error(f"Received Key Error Accessing Invalid Dictionary Entry -> {ke}")
        return
    except ValueError as ve:
        logger.error(f"Received Value Error Accessing Invalid Dictionary Entry -> {ve}")
        return
    except OSError as oe:
        logger.error(f"Received System Error Accessing Invalid Dictionary Entry -> {oe}")
        return
    
    failed_users = []

    for user in user_list:
        
        # Verify We Have Retrieved An Applicable User
        if user is None or user["userId"] is None:
            logger.error("Failed To Parse User Entry In User List")
            continue

        user_voice_messaging_portal = api.voice_messaging.get_user_voice_messaging_voice_portal(user["userId"])

        if user_voice_messaging_portal is None or type(user_voice_messaging_portal) is not dict:
            logger.error(f"Failed To Query Voice Messaging Portal For User -> {user["userId"]}")
            failed_users.append(user)
            continue

        if not user_voice_messaging_portal["voicePortalAutoLogin"]:
            logger.info(f"Enabling Automatic Voice Portal Login For User -> {user["userId"]}")

            user_voice_messaging_portal["voicePortalAutoLogin"] = True # Flip Boolean Flag And Put Full Dict To Ensure No Data Corruption
            api.voice_messaging.put_user_voice_messaging_voice_portal(user["userId"], user_voice_messaging_portal)

    # Return A List Of Failed Users If Present | Bool If Routine Ran Successfully
    return failed_users if failed_users else True

