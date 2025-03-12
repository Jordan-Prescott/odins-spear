def main(
    api,
    service_provider_id,
    group_id,
    user_id,
    device_type,
    email,
    primary_device,
    webex_feature_pack_name,
    enable_integarated_imp,
):
    logger = api.logger

    # Update the email & alt user id
    email_alt_userid = {
        "emailAddress": email,
        "alternateUserId": [{"alternateUserId": email, "description": "Webex"}],
    }

    try:
        api.users.put_user(
            service_provider_id, group_id, user_id, updates=email_alt_userid
        )
        logger.info("Updated email and alt user ID.")
    except Exception as e:
        logger.error(f"Failed to update users email and alt user ID, detail: {e}")

    # Assign feature pack
    try:
        if webex_feature_pack_name:
            api.services.put_user_services(
                user_id=user_id, service_packs=[webex_feature_pack_name]
            )
        logger.info(f"Added feature {webex_feature_pack_name}")
    except Exception as e:
        logger.error(f"Failed to add feature {webex_feature_pack_name}, detail: {e}")

    # enable IMP in service settings
    if enable_integarated_imp:
        enable_IMP = {"Integrated IMP": {"isActive": True}}
        try:
            api.services.put_user_service_settings(user_id=user_id, settings=enable_IMP)
            logger.info("Enabled integrated IMP")
        except Exception as e:
            logger.info(f"Failed to enable Integrated IMP, detail: {e}")

    # build device
    device_name = f"{user_id.split('@')[0]}_WBX"
    device_password = api.password_generate.get_password_generate(
        service_provider_id, group_id
    )["password"]

    device_payload = {
        "useCustomUserNamePassword": "true",
        "accessDeviceCredentials": {
            "userName": device_name,
            "password": device_password,
        },
        "userName": device_name,
    }

    try:
        api.devices.post_group_device(
            service_provider_id=service_provider_id,
            group_id=group_id,
            device_name=device_name,
            device_type=device_type,
            payload=device_payload,
        )
        logger.info("Built device")
    except Exception as e:
        logger.error(f"Failed to build device, detail: {e}")

    # Add device to user based on primary flag - JP
    if primary_device:
        primary_device_configuration = {
            "endpointType": "accessDeviceEndpoint",
            "accessDeviceEndpoint": {
                "accessDevice": {
                    "deviceType": device_type,
                    "deviceName": device_name,
                    "serviceProviderId": service_provider_id,
                    "groupId": group_id,
                    "deviceLevel": "Group",
                },
                "linePort": user_id,
            },
        }
        try:
            api.users.put_user(
                service_provider_id, group_id, user_id, primary_device_configuration
            )
            logger.info("Added device to user as primary")
        except Exception as e:
            logger.error(f"failed to add device as primary, detail: {e}")
    else:
        try:
            api.shared_call_appearance.post_user_shared_call_appearance_endpoint(
                user_id, user_id.replace("@", "_WBX@"), device_name
            )
            logger.info("Added device as shared call appearance")
        except Exception as e:
            logger.error(f"Failed to add devie as shared call appearance, detail: {e}")

    # Get webex password
    try:
        password = api.password_generate.get_password_generate(
            service_provider_id, group_id
        )["password"]
        api.authentication.put_user_web_authentication_password(user_id, password)
        logger.info("Set webex password")
    except Exception as e:
        logger.error(f"Failed to set webex password, Detail {e}")

    # Return formatted data
    webex_user_details = {
        "username": email,
        "password": password,
        "primary_device": primary_device,
        "device_type": device_type,
    }

    return webex_user_details
