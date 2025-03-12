import re

from ..exceptions import OSAliasNotFound


def locate_alias(alias, aliases: list):
    for a in aliases:
        if re.fullmatch(
            r"^[A-Za-z0-9\-_.!~*()']+$", alias
        ):  # As per Odin Spec: User alias cannot contain any characters except A-Z, a-z, 0-9, -_.!~*() or single quotes.
            return True


def main(api, service_provider_id: str, group_id: str, alias: str):
    RETRY_QUEUE = []
    MAX_RETRIES = 2
    OBJECT_WITH_ALIAS = []

    auto_attendants = api.auto_attendants.get_auto_attendants(
        service_provider_id, group_id
    )
    hunt_groups = api.hunt_groups.get_group_hunt_groups(service_provider_id, group_id)
    call_centers = api.call_centers.get_group_call_centers(
        service_provider_id, group_id
    )

    broadwork_entities_user_ids = []

    # save logger from api
    logger = api.logger

    for aa in auto_attendants:
        broadwork_entities_user_ids.append(["AA", aa["serviceUserId"]])

    for hg in hunt_groups:
        broadwork_entities_user_ids.append(["HG", hg["serviceUserId"]])

    for cc in call_centers:
        broadwork_entities_user_ids.append(["CC", cc["serviceUserId"]])

    logger.info("Fetching aa, hg, and cc")
    for broadwork_entity in broadwork_entities_user_ids:
        logger.info(f"Fetching '{broadwork_entity[1]}'")
        formatted = {
            "type": broadwork_entity[0],
            "service_user_id": broadwork_entity[1],
        }

        temp_object = ""

        try:
            if broadwork_entity[0] == "AA":
                temp_object = api.auto_attendants.get_auto_attendant(
                    broadwork_entity[1]
                )
            elif broadwork_entity[0] == "HG":
                temp_object = api.hunt_groups.get_group_hunt_group(broadwork_entity[1])
            else:
                temp_object = api.call_centers.get_group_call_center(
                    broadwork_entity[1]
                )

            formatted["name"] = temp_object["serviceInstanceProfile"]["name"]
            formatted["aliases"] = temp_object["serviceInstanceProfile"]["aliases"]

            OBJECT_WITH_ALIAS.append(formatted)

        except Exception:
            # add a retry count and add this entity to retry queue
            logger.error(
                f"Failed to fetch bre '{broadwork_entity[1]}' added to retry queue"
            )
            broadwork_entity.append(0)
            RETRY_QUEUE.append(broadwork_entity)

    # objects failed in first instance
    if RETRY_QUEUE:
        logger.info("Going through retry queue")
    while RETRY_QUEUE:
        entity_type, service_user_id, retry_count = RETRY_QUEUE.pop(
            0
        )  # Get the first item from the queue

        formatted = {}
        formatted["type"] = entity_type
        temp_object = ""

        try:
            if entity_type == "AA":
                temp_object = api.auto_attendants.get_auto_attendant(service_user_id)
            elif entity_type == "HG":
                temp_object = api.hunt_groups.get_group_hunt_group(service_user_id)
            else:
                temp_object = api.call_centers.get_group_call_center(service_user_id)

            formatted["name"] = temp_object["serviceInstanceProfile"]["name"]
            formatted["aliases"] = temp_object["serviceInstanceProfile"]["aliases"]

            OBJECT_WITH_ALIAS.append(formatted)

        except Exception:
            if retry_count < MAX_RETRIES:
                RETRY_QUEUE.append(
                    (entity_type, service_user_id, retry_count + 1)
                )  # Increment retry count and re-add to the queue
            else:
                logger.error(
                    f"Failed to process {entity_type} - {service_user_id} after {MAX_RETRIES} retries - skipping"
                )

    logger.info("Searching through aa, hg, and cc")
    for broadwork_entity in OBJECT_WITH_ALIAS:
        logger.info(f"Checking bre '{broadwork_entity['name']}'")
        if locate_alias(alias, broadwork_entity["aliases"]):
            logger.info(
                f"Alias found, type: user, service_user_id: {broadwork_entity['name']}, alias: {alias}"
            )
            return broadwork_entity
    logger.info(f"Alias '{alias}' not found in aa, hg, cc")

    logger.info("Fetching users")
    users = api.users.get_users(service_provider_id, group_id, extended=True)
    logger.info("Users successfully fetched")

    logger.info("Searching users")
    for user in users:
        logger.info(f"Checking {user['userId']}")
        if locate_alias(alias, user["aliases"]):
            logger.info(
                f"Alias found, type: user, user_id: {user['userId']}, alias: {alias}"
            )
            return {"type": "user", "user_id": user["userId"], "alias": alias}

    return OSAliasNotFound
