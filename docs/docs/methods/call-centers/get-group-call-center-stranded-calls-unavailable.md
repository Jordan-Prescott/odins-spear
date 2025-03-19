# GET - Group Call Center Stranded Calls Unavailable

Retrieves the forwarding number for a user when a call center doesn't answer, along with the count of agents with an unavailable code in the call center.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID

### Returns

* Dict: Number to be Forwarded to, and Agents with an Unavailable Code set.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_centers.get_group_call_center_stranded_calls_unavailable(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceUserId": "TestCallCenter@domain.com",
  "action": "None",
  "transferPhoneNumber": null,
  "audioMessageSource": "File",
  "videoMessageSource": "Default",
  "audioUrlList": [],
  "videoUrlList": [],
  "audioFileList": [
    {
      "name": "StrandedCallsUnavailableAudio.wav",
      "mediaType": "WAV",
      "level": "User"
    }
  ],
  "videoFileList": []
}
```
