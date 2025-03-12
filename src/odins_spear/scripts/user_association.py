def main(api, service_provider_id: str, group_id: str, user_id: str):
    """identify a user's associations with Call Centers (CC), Hunt Groups (HG),
    and Pick Up Groups.

    Args:
        service_provider_id (str): Service Provider where the group is hosted.
        group_id (str): Group where the User is located.
        user_id (str): Target user ID.

    Returns:
        str: Formatted output of the user showing all CC, HG, and Pick Up user is assigned to.
    """

    logger = api.logger

    USER_DATA = {
        "userId": user_id,
        "firstName": None,
        "lastName": None,
        "extension": None,
        "phoneNumber": None,
        "aliases": None,
        "services": None,
        "featurePacks": None,
        "huntGroups": [],
        "callCenters": [],
        "pickUpGroup": None,
    }

    # fetch user, returns error if not found
    logger.info(f"Fetching user {user_id}")
    user = api.reports.get_user_report(user_id)

    USER_DATA["firstName"] = user["firstName"]
    USER_DATA["lastName"] = user["lastName"]
    USER_DATA["extension"] = user["extension"]
    USER_DATA["phoneNumber"] = user["phoneNumber"]
    USER_DATA["services"] = user["userServices"]
    USER_DATA["featurePacks"] = user["servicePacks"]
    USER_DATA["aliases"] = user["aliases"]

    logger.info("Fetching users pick up group")
    pick_up_group = api.call_pickup.get_call_pickup_group_user(
        service_provider_id, group_id, user_id
    )

    try:
        USER_DATA["pickUpGroup"] = pick_up_group[0]["name"]
    except IndexError:
        logger.error("User has no pickup group")
        USER_DATA["pickUpGroup"] = None

    logger.info("Fetching hunt groups")
    hunt_groups = api.hunt_groups.get_group_hunt_group_user(
        service_provider_id, group_id, user_id
    )
    for hg in hunt_groups:
        USER_DATA["huntGroups"].append(hg["serviceUserId"])

    # if the user does not have a license for CC this call errors
    try:
        logger.info("Fetching users call centers")
        call_centers = api.call_centers.get_user_call_center(user_id)
        for cc in call_centers["callCenters"]:
            USER_DATA["callCenters"].append(cc["serviceUserId"])
    except Exception:
        logger.error("user is not assigned to any call centers")
        USER_DATA["callCenters"] = None

    return USER_DATA
