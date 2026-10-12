import requests
import os

JIRA_URL = "https://shameemmadala098.atlassian.net"
EMAIL = "shameemmadala098@gmail.com"
API_TOKEN = os.getenv("JIRA_API_TOKEN")

url = f"{JIRA_URL}/rest/api/3/project/search"

if not API_TOKEN:
    raise ValueError("JIRA_API_TOKEN is not set in PowerShell")

response = requests.get(
    url,
    auth=(EMAIL, API_TOKEN),
    headers={"Accept": "application/json"},
    params={"maxResults": 50}
)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    projects = data.get("values", [])

    if projects:
        for project in projects:
            print("Project name:", project["name"])
            print("Project key:", project["key"])
    else:
        print("No projects returned by the API.")
else:
    print("Error:", response.text)