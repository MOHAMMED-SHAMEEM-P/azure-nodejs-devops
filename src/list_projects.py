# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shameemmadala098.atlassian.net/rest/api/3/project"

import os

API_TOKEN = os.getenv("JIRA_API_TOKEN")

auth = HTTPBasicAuth("shameemadala098@gmail.com", "<API_TOKEN>")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))