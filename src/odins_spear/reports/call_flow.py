from tqdm import tqdm

from .report_utils.graphviz_module import GraphvizModule
from .report_utils.helpers import find_entity_with_number_type
from .report_utils.parsing import call_flow_module


from ..store import DataStore
from ..store import broadwork_entities as bre


def main(
    api,
    service_provider_id: str,
    group_id: str,
    number: str,
    number_type: str,
    broadworks_entity_type: str,
):
    logger = api.logger
    # Creates data store for use later
    data_store = DataStore()

    logger.info("Fetching Service Provider & Group details")
    # Gather entities
    service_provider = bre.ServiceProvider.from_dict(
        data=api.service_providers.get_service_provider(service_provider_id)
    )
    group = bre.Group.from_dict(
        service_provider=service_provider,
        data=api.groups.get_group(service_provider_id, group_id),
    )

    data_store.store_objects(service_provider, group)

    logger.info("Fetching group auto attendants")
    auto_attendants = api.auto_attendants.get_auto_attendants(
        service_provider_id, group_id
    )
    for aa in auto_attendants:
        auto_attendant = bre.AutoAttendant.from_dict(
            group=group,
            data=api.auto_attendants.get_auto_attendant(aa["serviceUserId"]),
        )
        data_store.auto_attendants.append(auto_attendant)

    logger.info("Fetching all users this may take a couple of minutes")
    users = api.users.get_users(service_provider_id, group_id, extended=True)

    # Captures users with the forward fucntionality
    logger.info("Fetching call forward always users")
    call_forward_always_users = [
        item["user"]["userId"]
        for item in api.call_forwarding_always.get_bulk_call_forwarding_always(
            service_provider_id, group_id
        )
        if item["service"]["assigned"] and item["data"]["isActive"]
    ]

    logger.info("Fetching call forward busy users")
    call_forward_busy_users = [
        item["user"]["userId"]
        for item in api.call_forwarding_busy.get_bulk_call_forwarding_busy(
            service_provider_id, group_id
        )
        if item["service"]["assigned"] and item["data"]["isActive"]
    ]

    logger.info("Fetching call forward no answer users")
    call_forward_no_answer_users = [
        item["user"]["userId"]
        for item in api.call_forwarding_no_answer.get_bulk_call_forwarding_no_answer(
            service_provider_id, group_id
        )
        if item["service"]["assigned"] and item["data"]["isActive"]
    ]

    logger.info("Fetching call forward not reachable users")
    call_forward_not_reachable = [
        item["user"]["userId"]
        for item in api.call_forwarding_not_reachable.get_bulk_call_forwarding_not_reachable(
            service_provider_id, group_id
        )
        if item["service"]["assigned"] and item["data"]["isActive"]
    ]

    logger.info("Analysing all users pulling call forwarding numbers")
    for u in users:
        user = bre.User.from_dict(group=group, data=u)

        if user.id in call_forward_always_users:
            user.call_forwarding_always = str(
                api.call_forwarding_always.get_user_call_forwarding_always(user.id)[
                    "forwardToPhoneNumber"
                ]
            )
        if user.id in call_forward_busy_users:
            user.call_forwarding_busy = str(
                api.call_forwarding_busy.get_user_call_forwarding_busy(user.id)[
                    "forwardToPhoneNumber"
                ]
            )
        if user.id in call_forward_no_answer_users:
            user.call_forwarding_no_answer = str(
                api.call_forwarding_no_answer.get_user_call_forwarding_no_answer(
                    user.id
                )["forwardToPhoneNumber"]
            )
        if user.id in call_forward_not_reachable:
            user.call_forwarding_not_reachable = str(
                api.call_forwarding_not_reachable.get_user_call_forwarding_not_reachable(
                    user.id
                )["forwardToPhoneNumber"]
            )

        data_store.users.append(user)

    logger.info("Fetching call centers")
    call_centers = api.call_centers.get_group_call_centers(
        service_provider_id, group_id
    )

    logger.info("Analysing call centers")
    for cc in call_centers:
        call_center = api.call_centers.get_group_call_center(cc["serviceUserId"])
        call_center["agents"] = api.call_centers.get_group_call_center_agents(
            cc["serviceUserId"]
        )["agents"]

        call_center = bre.CallCenter.from_dict(group=group, data=call_center)

        try:
            overflow_settings = api.call_centers.get_group_call_center_overflow(
                call_center.service_user_id
            )
            call_center.overflow_calls_action = overflow_settings["action"]
            call_center.overflow_calls_transfer_to_phone_number = (
                overflow_settings["transferPhoneNumber"]
                if call_center.overflow_calls_action == "Transfer"
                else None
            )
            logger.info(f"Fetched call center {cc['serviceUserId']} overflow details")
        except Exception:
            logger.error(f"Call center {cc['serviceUserId']} has no overflow")
            call_center.overflow_calls_action = None
            call_center.overflow_calls_transfer_to_phone_number = None

        try:
            stranded_calls_settings = (
                api.call_centers.get_group_call_center_stranded_calls(
                    call_center.service_user_id
                )
            )
            call_center.stranded_calls_action = stranded_calls_settings["action"]
            call_center.stranded_calls_transfer_to_phone_number = (
                stranded_calls_settings["transferPhoneNumber"]
                if call_center.stranded_calls_action == "Transfer"
                else None
            )
            logger.info(
                f"Fetched call center {cc['serviceUserId']} stranded call details"
            )
        except Exception:
            logger.error(
                f"Call center {cc['serviceUserId']} has no stranded calls action"
            )
            call_center.stranded_calls_action = None
            call_center.stranded_calls_transfer_to_phone_number = None

        try:
            stranded_calls_unavailable_settings = (
                api.call_centers.get_group_call_center_stranded_calls_unavailable(
                    call_center.service_user_id
                )
            )
            action_value = stranded_calls_unavailable_settings["action"]
            call_center.stranded_call_unavailable_action = (
                None if action_value == "None" else action_value
            )
            call_center.stranded_call_unavailable_transfer_to_phone_number = (
                stranded_calls_unavailable_settings["transferPhoneNumber"]
                if call_center.stranded_call_unavailable_action == "Transfer"
                else None
            )
            logger.info(
                f"Fetched call center {cc['serviceUserId']} stranded calls unavailable details"
            )
        except Exception:
            logger.error(
                f"Call center {cc['serviceUserId']} has no stranded calls unavailable action"
            )
            call_center.stranded_call_unavailable_action = None
            call_center.stranded_call_unavailable_transfer_to_phone_number = None

        try:
            forced_forwarding_settings = (
                api.call_centers.get_group_call_center_forced_forwarding(
                    call_center.service_user_id
                )
            )
            call_center.forced_forwarding_enabled = forced_forwarding_settings[
                "enabled"
            ]
            call_center.forced_forwarding_forward_to_phone_number = (
                forced_forwarding_settings["forwardToPhoneNumber"]
                if call_center.forced_forwarding_enabled
                else None
            )
            logger.info(
                f"Fetched call center {cc['serviceUserId']} forced forwarding details"
            )
        except Exception:
            logger.error(
                f"Call center {cc['serviceUserId']} has no forced forwarding action"
            )
            call_center.forced_forwarding_enabled = False
            call_center.forced_forwarding_forward_to_phone_number = None

        data_store.call_centers.append(call_center)

    logger.info("Fetching hunt groups")
    hunt_groups = api.hunt_groups.get_group_hunt_groups(service_provider_id, group_id)
    for hg in tqdm(hunt_groups, desc="Fetching all Hunt Groups."):
        hunt_group = bre.HuntGroup.from_dict(
            group=group, data=api.hunt_groups.get_group_hunt_group(hg["serviceUserId"])
        )
        data_store.hunt_groups.append(hunt_group)

    # locate number using broadworks_entity_type to zone in on correct location
    call_flow_start_node = find_entity_with_number_type(
        number, number_type.lower(), getattr(data_store, broadworks_entity_type + "s")
    )
    call_flow_start_node._start_node = True
    logger.info("Call flow start node found")

    # Nodes used in the graph
    logger.info("Parsing nodes for call flow")
    bre_nodes = call_flow_module(call_flow_start_node, data_store)

    logger.info("Generating report")
    # build, generate, save graph
    graph = GraphvizModule("./os_reports/")
    graph.generate_call_flow_graph(bre_nodes, number)
    graph._save_graph(f"Calls To {number}")
    logger.info("Report saved")

    return True
