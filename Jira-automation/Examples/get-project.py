# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import config

url = "https://{config.JIRA_DOMAIN}/rest/api/3/project"

API_TOKEN= config.JIRA_API_TOKEN

auth = HTTPBasicAuth("config.JIRA_EMAIL", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
