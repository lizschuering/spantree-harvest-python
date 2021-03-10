import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Harvest API Documenation: https://help.getharvest.com/api-v2/

### Project Budget Reports Endpoint (Reports API) ###

project_budget = "/v2/reports/project_budget"

url = "https://api.harvestapp.com" + project_budget
headers = {
    "User-Agent": "Python Harvest API Sample",
    "Authorization": "Bearer " + os.environ.get("HARVEST_ACCESS_TOKEN"),
    "Harvest-Account-ID": os.environ.get("HARVEST_ACCOUNT_ID")
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)
# print(jsonResponse)

# See a list of all active projects using the Project Budget API
for result in jsonResponse["results"]:
    if result["is_active"] == True:
        print(result["client_name"] + " " + result["project_name"] + " " + str(result["budget"]))

