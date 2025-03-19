# GET - Group Call Center Forced Forwarding

Retrieves the forwarding number for a call center if it is set to forward calls, along with any associated audio messages.

### Parameters&#x20;

* service_user_id (str): Target Call Center ID

### Returns

* Dict: Number to be Forwarded to, alongside any Audio Messages.

### How To Use:

{% code overflow="wrap" %}
```python
my_api.call_centers.get_group_call_center_forced_forwarding(
    service_user_id="TestCallCenter@domain.com"
)
```
{% endcode %}

### Example Returned Data (Formatted)
```json
{
  "serviceUserId": "TestCallCenter@domain.com",
  "enabled": false,
  "forwardToPhoneNumber": null,
  "allowEnableViaFAC": true,
  "playAnnouncementBeforeForwarding": false,
  "audioMessageSource": "File",
  "videoMessageSource": "Default",
  "audioUrlList": [],
  "videoUrlList": [],
  "audioFileList": [
    {
      "name": "HandoverMusic.wav",
      "mediaType": "WAV",
      "level": "User"
    }
  ],
  "videoFileList": []
}
```
