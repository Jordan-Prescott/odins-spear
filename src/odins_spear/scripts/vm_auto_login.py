def main(api, service_provider_id: str, group_id: str, service_pack_id: str = None):

    logger = api.logger

    user_list: list = []

    try:
        if service_pack_id:
            user_list = api.services.get_group_services_user_assigned(
                group_id,
                service_provider_id,
                service_pack_id,
                "servicePackName"
            )["users"]
        else:
            user_list = api.users.get_users(
                service_provider_id,
                group_id
            )
    except KeyError as ke:
        logger.info(f"Received Key Error Accessing Invalid Dictionary Entry -> {ke}")
        return
    except ValueError as ve:
        logger.info(f"Received Value Error Accessing Invalid Dictionary Entry -> {ve}")
        return
    except OSError as oe:
        logger.info(f"Received System Error Accessing Invalid Dictionary Entry -> {oe}")
        return

    for user in user_list:
        
        if user is None or user["userId"] is None:
            logger.error("Failed To Parse User Entry In User List")
            continue

        user_voice_messaging_portal = api.voice_messaging.get_user_voice_messaging_voice_portal(user["userId"])

        if user_voice_messaging_portal is None or type(user_voice_messaging_portal) is not dict:
            logger.error(f"Failed To Query Voice Messaging Portal For User -> {user["userId"]}")
            continue

        if not user_voice_messaging_portal["voicePortalAutoLogin"]:
            logger.info(f"Enabling Automatic Voice Portal Login For User -> {user["userId"]}")

            user_voice_messaging_portal["voicePortalAutoLogin"] = True # Flip Boolean Flag And Put Full Dict To Ensure No Data Corruption
            api.voice_messaging.put_user_voice_messaging_voice_portal(user["userId"], user_voice_messaging_portal)

    

