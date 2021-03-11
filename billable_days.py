import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import date

# Harvest API Documenation: https://help.getharvest.com/api-v2/

# Time Period You're Looking At...
start_date = 20210301
end_date = 20210307

### Time Reports Endpoint (Reports API) - Client Report ###

# Python Basic Date & Time Types: https://docs.python.org/3/library/datetime.html

time_reports = "/v2/reports/time/clients"

url = "https://api.harvestapp.com" + time_reports + \
    "?from=" + str(start_date) + "&to=" + str(end_date)
headers = {
    "User-Agent": "Python Harvest API Sample",
    "Authorization": "Bearer " + os.environ.get("HARVEST_ACCESS_TOKEN"),
    "Harvest-Account-ID": os.environ.get("HARVEST_ACCOUNT_ID")
}

# How JSON is decoded by Python see 'Enccoders and Decoders' section in: https://docs.python.org/3/library/json.html
# Working with JSON in Python: https://youtu.be/9N6a-VLBa2I

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)
# print(jsonResponse)

# See a list of all projects and billable days used for a given time period
print("### Billable Days Used Per Project For the Period " + str(start_date) + " to " + str(end_date) + " ###")
for result in jsonResponse["results"]:
    if result["billable_hours"] > 0:
        print(result["client_name"] + ": " +
              str(result["billable_hours"] / 8) + " billable days.")

### Time Reports Endpoint (Reports API) - Team Report ###

team_reports = "/v2/reports/time/team"

url = "https://api.harvestapp.com" + team_reports + \
    "?from=" + str(start_date) + "&to=" + str(end_date)
headers = {
    "User-Agent": "Python Harvest API Sample",
    "Authorization": "Bearer " + os.environ.get("HARVEST_ACCESS_TOKEN"),
    "Harvest-Account-ID": os.environ.get("HARVEST_ACCOUNT_ID")
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)
jsonResponsePretty = json.dumps(jsonResponse, indent=2)
# print(jsonResponsePretty)

# See a list of billable days used by team member for a given time period
print("### Billable Days Per Team Member For the Period " + str(start_date) + " to " + str(end_date) + " ###")
for result in jsonResponse["results"]:
    if result["billable_hours"]:
        print(result["user_name"] + ": " + str(result["billable_hours"] / 8) + " billable days.")