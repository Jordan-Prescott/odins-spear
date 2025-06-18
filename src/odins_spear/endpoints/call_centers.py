from .base_endpoint import BaseEndpoint


class CallCenters(BaseEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # GET

    def get_group_call_centers(self, service_provider_id: str, group_id: str):
        """Retrieves a list of active call centers within a specified group, along with their settings.

        Args:
            service_provider_id (str): Target Service Provider where group is hosted
            group_id (str): Target Group ID

        Returns:
            List: List of Call Centers and their settings.
        """

        endpoint = "/groups/call-centers"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center(self, service_user_id: str):
        """Retrieves deatiled information on a single Call Center.

        Args:
            service_user_id (str): Target Call Center's ID

        Returns:
            Dict: Target Call Centers details.
        """

        endpoint = "/groups/call-centers"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center(self, user_id: str):
        """Retrieves a list of call centers that the specified user is currently associated with.

        Args:
            user_id (str): Target User ID

        Returns:
            Dict: Agents Call Centers setting and a list of the User's associated Call Centers.
        """

        endpoint = "/users/call-center"

        params = {"userId": user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_agents(self, service_user_id: str):
        """Returns list of agents assigned to the target call center.

        Args:
            service_user_id (str): Service user ID of target call center.

        Returns:
            Dict: List of agents assigned to call center
        """

        endpoint = "/groups/call-centers/agents"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_bounced_calls(self, service_user_id: str):
        """Retrieves the number of rings before a call is bounced from the specified call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Amount of Rings before a call is Bounced
        """

        endpoint = "/groups/call-centers/bounced-calls"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_forced_forwarding(self, service_user_id: str):
        """Retrieves the forwarding number for a call center if it is set to forward calls, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, alongside any Audio Messages.
        """

        endpoint = "/groups/call-centers/forced-forwarding"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_overflow(self, service_user_id):
        """Retrieves the forwarding number for a user when all call center agents are busy, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Dict: Call Centers overflow configuration.
        """

        endpoint = "/groups/call-centers/overflow"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_stranded_calls(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with any associated audio messages.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Call Centers stranded call configuration.
        """

        endpoint = "/groups/call-centers/stranded-calls"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_stranded_calls_unavailable(self, service_user_id):
        """Retrieves the forwarding number for a user when a call center doesn't answer, along with the count of agents with an unavailable code in the call center.

        Args:
            service_user_id (str): Target Call Center ID

        Returns:
            Dict: Number to be Forwarded to, and Agents with an Unavailable Code set.
        """
        endpoint = "/groups/call-centers/stranded-calls-unavailable"

        params = {"serviceUserId": service_user_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center(self, service_provider_id: str):
        """Retrieves call center settings that are hosted by the specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Call Centers and their settings.

            TOOD: Docs
        """
        endpoint = "/enterprises/call-centers"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_routing_policy(self, service_provider_id: str):
        """Retrieves call center call routing settings that are hosted by the specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Call Centers and their settings.

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_agent_unavailable_codes(
        self, service_provider_id: str
    ):
        """Retrieves call center agent unavailable codes that are hosted by the specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Call Centers and their settings.

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/agent-unavailable-codes"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_agent_unavailable_codes_settings(
        self, service_provider_id: str
    ):
        """Retrieves call center agent unavailable codes that are hosted by the specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Call Centers and their settings.

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/agent-unavailable-codes-settings"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_enhanced_reporting(self, service_provider_id: str):
        """Enables/ retrieves enhanced reporting for specified service provider.

        NOTE: Not fully understood. Use with caution.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/enhanced-reporting"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_enhanced_reporting_branding(
        self, service_provider_id: str
    ):
        """Enables/ retrieves enhanced reporting for specified service provider.

        NOTE: Not fully understood. Use with caution.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/enhanced-reporting-branding"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_enhanced_reporting_scheduled_reports(
        self, service_provider_id: str
    ):
        """Retrieves list of all scheduled reports for specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/enhanced-reporting/scheduled-reports"

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_enhanced_reporting_scheduled_report(
        self, service_provider_id: str, schedule_name: str
    ):
        """Retrieves a single scheduled report for specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID
            schedule_name (str): Target Schedule Name

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = "/enterprises/call-centers/enhanced-reporting/scheduled-reports"

        params = {
            "serviceProviderId": service_provider_id,
            "scheduleName": schedule_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_enhanced_reporting_scheduled_report_call_centers(
        self, service_provider_id: str, schedule_name: str
    ):
        """Retrieves a detailed single scheduled report for specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID
            schedule_name (str): Target Schedule Name

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = (
            "/enterprises/call-centers/enhanced-reporting/scheduled-report-call-centers"
        )

        params = {
            "serviceProviderId": service_provider_id,
            "scheduleName": schedule_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_threshold_profile(
        self, service_provider_id: str, profile_name: str
    ):
        """Retrieves a threshold profile of specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID
            profile_name (str): Target Profile Name

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = (
            "/enterprises/call-centers/enhanced-reporting/scheduled-report-call-centers"
        )

        params = {
            "serviceProviderId": service_provider_id,
            "scheduleName": profile_name,
        }

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_threshold_profiles(self, service_provider_id: str):
        """Retrieves threshold profiles of specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = (
            "/enterprises/call-centers/enhanced-reporting/scheduled-report-call-centers"
        )

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_call_disposition_codes(
        self, service_provider_id: str
    ):
        """Retrieves disposition codes of specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID

        Returns:
            Dict: Service Provider enhanced reporting

            TODO: Docs
        """
        endpoint = (
            "/enterprises/call-centers/enhanced-reporting/scheduled-report-call-centers"
        )

        params = {"serviceProviderId": service_provider_id}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_call_disposition_code(
        self, service_provider_id: str, disposition_code: str
    ):
        """Retrieves a single disposition code of specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID
            disposition_code (str): Target Disposition Code

        Returns:
            Dict: Details on disposition code.
        """
        endpoint = "/enterprises/call-centers/call-disposition-code"

        params = {"serviceProviderId": service_provider_id, "code": disposition_code}

        return self._requester.get(endpoint, params=params)

    def get_enterprise_call_center_call_disposition_code_usage(
        self, service_provider_id: str, disposition_code: str
    ):
        """Retrieves the usage of asingle disposition code of specified service provider.

        Args:
            service_provider_id (str): Target Service Provider ID
            disposition_code (str): Target Disposition Code

        Returns:
            Dict: Details on disposition code.
        """
        endpoint = "/enterprises/call-centers/call-disposition-code-usage"

        params = {"serviceProviderId": service_provider_id, "code": disposition_code}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_queue_status(self, call_center_user_id: str):
        """Retrieves the queue status of a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.

        Returns:
            Dict: Queue status of the call center. #TODO: docs
        """
        endpoint = "/groups/call-centers/status"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_queue_status_notifications(
        self, call_center_user_id: str
    ):
        """Retrieves the queue status notifications of a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.

        Returns:
            Dict: Queue status notifications of the call center. #TODO: docs
        """
        endpoint = "/groups/call-centers/queue-status-notifications"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_enhanced_reporting(
        self, service_provider_id: str, group_id: str
    ):
        """Retrieves the enhanced reporting of a call center.

        Args:
            service_provider_id (str): Target Service Provider ID. Can't be Enterprise ID.
            group_id (str): Target Group ID

        Returns:
            Dict: Enhanced reporting details
        """
        endpoint = "/groups/call-centers/enhanced-reporting"

        params = {"serviceProviderId": service_provider_id, "groupId": group_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_reporting(self, call_center_user_id: str):
        """Retrieves the reporting details of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Reporting details of call center.
        """
        endpoint = "/groups/call-centers/reporting"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_group_call_center_statistics(
        self,
        call_center_user_id: str,
        start_date: str,
        end_date: str,
        start_time: str = "00:00:00",
        end_time: str = "23:59:59",
        time_zone: str = "Z",
    ):
        """Retrieves the statistics of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            start_date (str): Start date of desired time period. Date must follow format 'YYYY-MM-DD'
            end_date (str): End date of desired time period. Date must follow format 'YYYY-MM-DD'
            start_time (str): Start time of desired time period. Time must follow formate 'HH:MM:SS'.
            end_time (str): End time of desired time period. Time must follow formate 'HH:MM:SS'.
            time_zone (str): A specified time you would like to see call records in.
                Time zone must follow format 'GMT', 'EST', 'PST'. Defaults to "Z" (UTC Time Zone).

        Returns:
            Dict: Statistics of call center.
        """
        endpoint = "/groups/call-centers/statistics"

        params = {
            "serviceUserId": call_center_user_id,
            "start": f"{start_date}T{start_time}{time_zone}",
            "end": f"{end_date}T{end_time}{time_zone}",
        }

        return self._requester.get(endpoint, params=params)

    def get_call_center_stranded_calls(self, call_center_user_id: str):
        """Retrieves the stranded calls settings of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Stranded calls settings of call center.
        """
        endpoint = "/groups/call-centers/stranded-calls"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_call_center_stranded_calls_unavailable(self, call_center_user_id: str):
        """Retrieves the stranded calls unavailable settings of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Stranded calls unavailable settings of call center.
        """
        endpoint = "/groups/call-centers/stranded-calls-unavailable"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_call_center_supervisors(self, call_center_user_id: str):
        """Retrieves the supervisors of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Supervisors of call center.
        """
        endpoint = "/groups/call-centers/supervisors"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_call_center_supervisor_agents(
        self, call_center_user_id: str, supervisor_user_id: str
    ):
        """Retrieves the agents of a supervisor of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            supervisor_user_id (str): Target Supervisor User ID

        Returns:
            Dict: Agents of supervisor of call center.
        """
        endpoint = "/groups/call-centers/supervisors/agents"

        params = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_call_center_thresholds(self, call_center_user_id: str):
        """Retrieves the thresholds of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Thresholds of call center.
        """
        endpoint = "/groups/call-centers/thresholds"

        params = {
            "serviceUserId": call_center_user_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_dnis(self, call_center_user_id: str):
        """Retrieves the DNIS of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: DNIS of call center.
        """
        endpoint = "/users/call-centers/dnis"

        params = {"userId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_disposition_codes(self, call_center_user_id: str):
        """Retrieves the disposition codes of a call center agent.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Disposition codes of call center agent.
        """
        endpoint = "/users/call-centers/disposition-codes"

        params = {"userId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_monitoring(self, call_center_user_id: str):
        """Retrieves the monitoring settings of a call center agent.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Monitoring settings of call center agent.
        """
        endpoint = "/users/call-centers/monitoring"

        params = {"userId": call_center_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_agents(self, agent_user_id: str):
        """Retrieves the agents of a call center agent.

        Args:
            agent_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Agents of call center agent.
        """

        endpoint = "/user/call-centers/agents"

        params = {"agentUserId": agent_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_agent(self, agent_user_id: str):
        """Retrieves the details of a call center agent.

        Args:
            agent_user_id (str): Target Service Provider ID. Can't be Enterprise ID.

        Returns:
            Dict: Details of call center agent.
        """

        endpoint = "/user/call-centers/agents"

        params = {"agentUserId": agent_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_supervisors(
        self, agent_user_id: str, supervisor_user_id: str
    ):
        """Retrieves the supervisors of a call center agent.

        Args:
            agent_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            supervisor_user_id (str): Target Supervisor User ID

        Returns:
            Dict: Supervisors of call center agent. #TODO: docs
        """
        endpoint = "/user/call-centers/agents/supervisors"

        params = {"agentUserId": agent_user_id, "supervisorUserId": supervisor_user_id}

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_supervisors_all_agents(
        self, call_center_user_id: str, supervisor_user_id: str
    ):
        """Retrieves all agents of a supervisor of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            supervisor_user_id (str): Target Supervisor User ID

        Returns:
            Dict: All agents of a supervisor of a call center. #TODO: docs
        """
        endpoint = "/user/call-centers/agents/supervisors"

        params = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
        }

        return self._requester.get(endpoint, params=params)

    def get_user_call_center_supervisor_call_centers(self, supervisor_user_id: str):
        """Retrieves the call centers of a supervisor.

        Args:
            supervisor_user_id (str): Target Supervisor User ID

        Returns:
            Dict: Call centers of a supervisor. #TODO: docs
        """
        endpoint = "/user/call-centers/supervisor/call-centers"

        params = {"supervisorUserId": supervisor_user_id}

        return self._requester.get(endpoint, params=params)

    # POST

    def post_enterprise_call_center_agent_unavailable_codes(
        self,
        service_provider_id: str,
        code: int,
        description: str,
        is_active: bool,
    ):
        """Creates a new agent unavailable code for a call center.

        Args:
            service_provider_id (str): Target Service Provider ID.
            code (int): The code of the unavailable code.
            description (str): The description of the unavailable code.
            is_active (bool): Whether the unavailable code is active.

        Returns:
            Dict: The new agent unavailable code.
        """
        endpoint = "/enterprise/call-centers/agent-unavailable-codes"

        data = {
            "serviceProviderId": service_provider_id,
            "code": code,
            "description": description,
            "isActive": is_active,
        }

        return self._requester.post(endpoint, data=data)

    def post_enterprise_call_center_enhanced_reporting_scheduled_report(
        self, service_provider_id: str, name: str, description: str, payload: dict = {}
    ):
        """Creates a new scheduled report for a call center.

        Args:
            service_provider_id (str): Target Service Provider ID.
            name (str): The name of the scheduled report.
            description (str): The description of the scheduled report.
            payload (dict): The payload of the scheduled report.

        Returns:
            Dict: The new scheduled report.
        """
        endpoint = "/enterprise/call-centers/enhanced-reporting/scheduled-reports"

        payload["serviceProviderId"] = service_provider_id
        payload["scheduleName"] = name
        payload["description"] = description

        return self._requester.post(endpoint, data=payload)

    def post_enterprise_call_center_threshold_profile(
        self, service_provider_id: str, name: str, description: str, payload: dict = {}
    ):
        """Creates a new threshold profile for a call center.

        Args:
            service_provider_id (str): Target Service Provider ID.
            name (str): The name of the threshold profile.
            description (str): The description of the threshold profile.
            payload (dict): The payload of the threshold profile.

        Returns:
            Dict: The new threshold profile.
        """
        endpoint = "/service-providers/call-centers/threshold-profile"

        params = {
            "serviceProviderId": service_provider_id,
            "profileName": name,
        }

        payload["profileDescription"] = description

        return self._requester.post(endpoint, data=payload, params=params)

    def post_enterprise_call_center_call_disposition_code(
        self, service_provider_id: str, code: int, description: str, is_active: bool
    ):
        """Creates a new call disposition code for a call center.

        Args:
            service_provider_id (str): Target Service Provider ID.
            code (int): The code of the call disposition code.
            description (str): The description of the call disposition code.
            is_active (bool): Whether the call disposition code is active.

        Returns:
            Dict: The new call disposition code.
        """
        endpoint = "/enterprises/call-centers/call-disposition-code"

        data = {
            "code": code,
            "description": description,
            "isActive": is_active,
            "serviceProviderId": service_provider_id,
        }

        return self._requester.post(endpoint, data=data)

    def post_group_call_center(
        self,
        service_provider_id: str,
        group_id: str,
        name: str,
        call_center_user_id: str,
        policy: str = "Circular",
        type: str = "Standard",
        payload: dict = {},
    ):
        """Creates a new call center.

        Args:
            service_provider_id (str): Target Service Provider ID.
            group_id (str): Target Group ID.
            name (str): The name of the call center.
            call_center_user_id (str): The user ID of the call center.
            policy (str): The policy of the call center. Defaults to Circular.
            type (str): The type of the call center. Defaults to Standard.
            payload (dict): The payload of the call center. Remainder of settings.

        Returns:
            Dict: The new call center.
        """
        endpoint = "/groups/call-centers"

        payload["serviceProviderId"] = service_provider_id
        payload["groupId"] = group_id
        payload["serviceInstanceProfile"]["name"] = name
        payload["serviceUserId"] = call_center_user_id
        payload["policy"] = policy
        payload["type"] = type

        return self._requester.post(endpoint, data=payload)

    def post_group_call_center_agents(
        self, call_center_user_id: str, agent_user_ids: list
    ):
        """Adds agents to a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            agent_user_ids (list): List of user IDs to be added to call center.

        Returns:
            None
        """
        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.post(endpoint, data=data)

    def post_group_call_center_dnis_instance(
        self, service_user_id: str, name: str, payload: dict = {}
    ):
        """Creates a new DNIS instance for a call center.

        Args:
            service_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            name (str): The name of the DNIS instance.
            payload (dict): The payload of the DNIS instance.

        Returns:
            None
        """
        endpoint = "/groups/call-centers/dnis/instances"

        payload["serviceUserID"] = service_user_id
        payload["name"] = name

        return self._requester.post(endpoint, data=payload)

    def post_group_call_center_queue_disposition_code(
        self, call_center_user_id: str, code: str, description: str, is_active: bool
    ):
        """Creates a new queue disposition code for a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            code (str): The code of the queue disposition code.
            description (str): The description of the queue disposition code.
            is_active (bool): Whether the queue disposition code is active.

        Returns:
            None
        """
        endpoint = "/groups/call-centers/disposition-codes/codes"

        data = {
            "serviceUserId": call_center_user_id,
            "code": code,
            "description": description,
            "isActive": is_active,
        }

        return self._requester.post(endpoint, data=data)

    def post_group_call_center_supervisors(
        self, call_center_user_id: str, supervisor_user_ids: list
    ):
        """Adds supervisors to a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            supervisor_user_ids (list): List of user IDs to be added to call center.

        Returns:
            None
        """
        endpoint = "/groups/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisors": [
                {"userId": supervisor_id} for supervisor_id in supervisor_user_ids
            ],
        }

        return self._requester.post(endpoint, data=data)

    def post_user_call_center_supervisor_agents(
        self, call_center_user_id: str, supervisor_user_id: str, agent_user_ids: list
    ):
        """Adds agents to a supervisor of a call center.

        Args:
            call_center_user_id (str): Target Service Provider ID. Can't be Enterprise ID.
            supervisor_user_id (str): Target Supervisor User ID
            agent_user_ids (list): List of user IDs to be added to call center.

        Returns:
            Dict: The new agents.
        """
        endpoint = "/user/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.post(endpoint, data=data)

    # PUT

    def put_group_call_centers_status(
        self, call_center_user_ids: list, status: bool = True
    ):
        """Updates a list of call centers (CC) status to either active or inactive.

        Args:
            call_center_user_ids(list): List of service user IDs (CC IDs), the status given will be applied to these.
            status (bool): Boolean value of True (Activate) or False (Deactivate) which will be applied to list of AAs.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/status"

        data = {
            "instances": [
                {"serviceUserId": call_center_user_id, "isActive": status}
                for call_center_user_id in call_center_user_ids
            ]
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center(self, call_center_user_id: str, updates: dict):
        """Allows you to update a specific call center.

        Args:
            call_center_user_id (str): Service user id of the target call center.
            updates (dict): Updates to apply in in a dictionary format.

        Returns:
            Dict: The call center with the new applied updates.
        """

        endpoint = "/groups/call-centers"

        updates["serviceUserId"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_agents(
        self, call_center_user_id: str, agent_user_ids: list
    ):
        """Add or remove agents to a call center.

        Note: Leave the agent_user_ids blank to remove all users and to remove some only include
        the users you would like to include in this call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            agent_user_ids (list): List of user IDs to be added to call center.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center_agents_levels(
        self, call_center_user_id: str, agent_user_ids: list, skill_level: int
    ):
        """Update a list of agents skill level in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the call center users belong to.
            agent_user_ids (list): List of the target users.
            skill_level (int): Skill level that will be applied to the list of users in the target call center.

        Returns:
            Dict: CC ID and list of the agent and their updated skill level.
        """

        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [
                {"userId": agent_id, "skillLevel": skill_level}
                for agent_id in agent_user_ids
            ],
        }

        return self._requester.put(endpoint, data=data)

    def put_group_call_center_bounced_calls(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the bounced call settings of a single Call Center (CC)

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/bounced-calls"

        updates["serviceUserId"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_dnis_instance(
        self, call_center_user_id: str, updates: dict
    ):
        """Update a DNIS instance of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/dnis/instances"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_forced_forwarding(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the forced forwarding settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/forced-forwarding"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_overflow(self, call_center_user_id: str, updates: dict):
        """Update the overflow settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/overflow"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_stranded_calls(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the stranded calls settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/stranded-calls"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_stranded_calls_unavailable(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the stranded calls unavailable settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to apply to target CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/stranded-calls-unavailable"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_announcements(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the announcements of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to be applied to the CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/announcements"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_group_call_center_comfort_message_bypass(
        self, call_center_user_id: str, updates: dict
    ):
        """Update the comfort message bypass settings of a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            updates (dict): Updates to be applied to the CC.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/comfort-message-bypass"

        updates["serviceUserID"] = call_center_user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_call_center_supervised_agents(
        self, call_center_user_id: str, supervisor_user_id: str, agent_ids: list
    ):
        """Update the list of agents a supervisor has in a single Call Center (CC).

        Args:
            call_center_user_id (str): Service user ID of the target CC.
            supervisor_user_id (str): User ID of the supervisor.
            agent_ids (list): List of user IDs of agents to apply to supervisor.

        Returns:
            Dict: Superivor ID and list of agents they supervise.
        """

        endpoint = "/groups/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "supervisors": [{"userId": agent_id} for agent_id in agent_ids],
        }

        return self._requester.put(endpoint, data=data)

    def put_user_call_center(self, user_id: str, updates: dict):
        """Update an agent's status in a Call Center (CC).

        Args:
            user_id (str): User ID of the target user.
            updates (dict): Updates to be applied to the user.

        Returns:
            Dict: Agents ACD status and status in each CC they are assigned to.
        """

        endpoint = "/users/call-center"

        updates["userId"] = user_id

        return self._requester.put(endpoint, data=updates)

    def put_user_call_center_agents_update(
        self, user_id: str, call_center_service_ids: list
    ):
        """Update the Call Centers (CC) a user is assigned to.

        Args:
            user_id (str): User ID of the target user.
            call_center_service_ids (list): List of CC service user IDs to update the user with.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/user/call-centers/agents"

        data = {
            "agentUserId": user_id,
            "callCenters": [
                {"userId": call_center_id} for call_center_id in call_center_service_ids
            ],
        }

        return self._requester.put(endpoint, data=data)

    def put_user_call_center_agent_sign_out(self, user_id: str):
        """Sign the user out of their assigned Call Centers (CC).

        Args:
            user_id (str): User ID of the target user.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/user/call-centers/agents/sign-out"

        data = {
            "agentUserId": user_id,
        }

        return self._requester.put(endpoint, data=data)

    def put_enterprise_call_center(self, service_provider_id: str, updates: dict = {}):
        """Update an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            updates (dict): Updates to be applied to the enterprise call center.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/enterprise/call-centers"

        updates["serviceProviderId"] = service_provider_id

        return self._requester.put(endpoint, data=updates)

    def put_enterprise_call_center_routing_policy(
        self, service_provider_id: str, updates: dict = {}
    ):
        """Update the routing policy of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            updates (dict): Updates to be applied to the enterprise call center.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/enterprise/call-centers/routing-policy"

        updates["serviceProviderId"] = service_provider_id

        return self._requester.put(endpoint, data=updates)

    def put_enterprise_call_center_agent_unavailable_codes(
        self, service_provider_id: str, code: int, description: str, is_active: bool
    ):
        """Update an agent unavailable code in an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            code (int): Code of the agent unavailable code to update.
            description (str): Description of the agent unavailable code to update.
            is_active (bool): Whether the agent unavailable code is active.

        Returns:
            Dict: Dictionary of the new state of the code.
        """

        endpoint = "/enterprise/call-centers/agent-unavailable-codes"

        params = {
            "serviceProviderId": service_provider_id,
        }

        data = {
            "code": code,
            "description": description,
            "isActive": is_active,
        }

        return self._requester.put(endpoint, params=params, data=data)

    def put_enterprise_call_center_agent_unavailable_codes_settings(
        self, service_provider_id: str, updates: dict = {}
    ):
        """Update the agent unavailable code settings of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            updates (dict): Updates to be applied to the enterprise call center.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/enterprise/call-centers/agent-unavailable-codes-settings"

        params = {
            "serviceProviderId": service_provider_id,
        }

        return self._requester.put(endpoint, params=params, data=updates)

    def put_enterprise_call_center_enhanced_reporting(
        self, service_provider_id: str, reporting_server: str
    ):
        """Update the enhanced reporting settings of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            reporting_server (str): Reporting server of the enterprise call center.

        Returns:
            Dict: Dictionary of the new state of the reporting.
        """

        endpoint = "/enterprise/call-centers/enhanced-reporting"

        params = {
            "serviceProviderId": service_provider_id,
        }

        data = {
            "reportingServer": reporting_server,
            "serviceProviderId": service_provider_id,
        }

        return self._requester.put(endpoint, params=params, data=data)

    def put_enterprise_call_center_enhanced_reporting_branding(
        self,
        service_provider_id: str,
        branding_choice: str,
        description: str,
        content: str,
    ):
        """Update the branding of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            branding_choice (str): Choice of branding to update.
            description (str): Description of the branding to update.
            content (str): Content of the branding to update.

        Returns:
            Dict: Dictionary of the new state of the branding.
        """

        endpoint = "/enterprise/call-centers/enhanced-reporting-branding"

        params = {
            "serviceProviderId": service_provider_id,
        }

        data = {
            "serviceProviderId": service_provider_id,
            "brandingChoice": branding_choice,
            "description": description,
            "content": content,
        }

        return self._requester.put(endpoint, params=params, data=data)

    def put_enterprise_call_center_enhanced_reporting_branding_filename(
        self, service_provider_id: str, branding_choice: str, filename: str
    ):
        """Update the filename of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            branding_choice (str): Choice of branding to update.
            filename (str): Filename of the branding to update.

        Returns:
            Dict: Dictionary of the new state of the branding.
        """

        endpoint = "/enterprise/call-centers/enhanced-reporting-branding"

        params = {
            "serviceProviderId": service_provider_id,
        }

        data = {
            "serviceProviderId": service_provider_id,
            "brandingChoice": branding_choice,
            "filename": filename,
        }

        return self._requester.put(endpoint, params=params, data=data)

    def put_enterprise_call_center_threshold_profile(
        self, service_provider_id: str, profile_name: str, updates: dict = {}
    ):
        """Update a threshold profile of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            profile_name (str): Name of the threshold profile to update.
            updates (dict): Updates to be applied to the threshold profile.

        Returns:
            Dict: Dictionary of the new state of the threshold profile.
        """

        endpoint = "/service-providers/call-centers/threshold-profiles"

        params = {
            "serviceProviderId": service_provider_id,
            "profileName": profile_name,
        }

        return self._requester.put(endpoint, params=params, data=updates)

    def put_enterprise_call_center_disposition_code(
        self, service_provider_id: str, code: int, description: str, is_active: bool
    ):
        """Update a disposition code of an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            code (int): Code of the disposition code to update.
            description (str): Description of the disposition code to update.
            is_active (bool): Whether the disposition code is active.

        Returns:
            Dict: Dictionary of the new state of the disposition code.
        """

        endpoint = "/enterprises/call-centers/call-disposition-code"

        data = {
            "serviceProviderId": service_provider_id,
            "code": code,
            "description": description,
            "isActive": is_active,
        }

        return self._requester.put(endpoint, data=data)

    # DELETE

    def delete_enterprise_call_center_agent_unavailable_codes(
        self, service_provider_id: str, code: int
    ):
        """Delete an agent unavailable code from an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            code (int): Code of the agent unavailable code to delete.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/enterprise/call-centers/agent-unavailable-codes"

        params = {
            "serviceProviderId": service_provider_id,
            "code": code,
        }

        return self._requester.delete(endpoint, params=params)

    def delete_enterprise_call_center_threshold_profile(
        self, service_provider_id: str, profile_name: str
    ):
        """Delete an agent unavailable code from an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            profile_name (str): Name of the threshold profile to delete.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/enterprise/call-centers/threshold-profiles"

        params = {
            "serviceProviderId": service_provider_id,
            "profileName": profile_name,
        }

        return self._requester.delete(endpoint, params=params)

    def delete_enterprise_call_center_call_disposition_code(
        self, service_provider_id: str, code: int
    ):
        """Delete a call disposition code from an enterprise call center.

        Args:
            service_provider_id (str): Service provider ID of the target enterprise call center.
            code (int): Code of the call disposition code to delete.

        Returns:
            Dict: Dictionary of the new state of the CC.
        """

        endpoint = "/enterprise/call-centers/call-disposition-codes"

        params = {
            "serviceProviderId": service_provider_id,
            "code": code,
        }

        return self._requester.delete(endpoint, params=params)

    def delete_group_call_center(self, call_center_user_id: str):
        """Delete a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers"

        params = {"serviceUserId": call_center_user_id}

        return self._requester.delete(endpoint, params=params)

    def delete_group_call_center_agents(
        self, call_center_user_id: str, agent_user_ids: list
    ):
        """Delete a list of agents from a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            agent_user_ids (list): List of user IDs of agents to delete.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/agents"

        data = {
            "serviceUserId": call_center_user_id,
            "agents": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.delete(endpoint, data=data)

    def delete_group_call_center_dnis_instance(
        self, call_center_user_id: str, name: str
    ):
        """Delete a DNIS instance from a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            name (str): Name of the DNIS instance to delete.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/dnis/instances"

        params = {
            "serviceUserId": call_center_user_id,
            "name": name,
        }

        return self._requester.delete(endpoint, params=params)

    def delete_group_call_center_queue_disposition_code(
        self, call_center_user_id: str, code: str
    ):
        """Delete a queue disposition code from a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            code (str): Code of the queue disposition code to delete.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/disposition-codes/codes"

        params = {
            "serviceUserId": call_center_user_id,
            "code": code,
        }

        return self._requester.delete(endpoint, params=params)

    def delete_group_call_center_supervisors(
        self, call_center_user_id: str, supervisor_user_ids: list
    ):
        """Delete a list of supervisors from a call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            supervisor_user_ids (list): List of user IDs of supervisors to delete.

        Returns:
            None: This method does not return any specific value.
        """

        endpoint = "/groups/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisors": [
                {"userId": supervisor_id} for supervisor_id in supervisor_user_ids
            ],
        }

        return self._requester.delete(endpoint, data=data)

    def delete_user_call_center_supervised_agents(
        self, call_center_user_id: str, supervisor_user_id: str, agent_user_ids: list
    ):
        """Delete a list of agents from a supervisor's call center.

        Args:
            call_center_user_id (str): Service user ID of the target call center.
            supervisor_user_id (str): User ID of the supervisor.
            agent_user_ids (list): List of user IDs of agents to delete.

        Returns:
            None: This method does not return any specific value.
        """
        endpoint = "/users/call-centers/supervisors"

        data = {
            "serviceUserId": call_center_user_id,
            "supervisorUserId": supervisor_user_id,
            "supervisors": [{"userId": agent_id} for agent_id in agent_user_ids],
        }

        return self._requester.delete(endpoint, data=data)
