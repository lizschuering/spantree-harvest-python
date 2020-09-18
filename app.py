import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Harvest API Documenation: https://help.getharvest.com/api-v2/

### Project Budget API ###
# project_budget = "/v2/reports/project_budget"

# url = "https://api.harvestapp.com" + project_budget
# headers = {
#     "User-Agent": "Python Harvest API Sample",
#     "Authorization": "Bearer " + os.environ.get("HARVEST_ACCESS_TOKEN"),
#     "Harvest-Account-ID": os.environ.get("HARVEST_ACCOUNT_ID")
# }

# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request, timeout=5)
# responseBody = response.read().decode("utf-8")
# jsonResponse = json.loads(responseBody)
# # print(jsonResponse)

# # See a list of all active clients and projects using the Project Budget API
# for result in jsonResponse["results"]:
#     if result["is_active"] == True:
#         print(result["client_name"] + " " + result["project_name"])

### Time Reports API ###

# Python Basic Date & Time Types: https://docs.python.org/3/library/datetime.html

time_reports = "/v2/reports/time/clients"

start_date = 20200907
end_date = 20200913

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

# See a list of all projects and engineering days used in a given time frame using the Time Report's API
for result in jsonResponse["results"]:
    if result["billable_hours"] > 0:
        print(result["client_name"] + ": " +
              str(result["billable_hours"] / 8) + " engineering days used.")

# Additional APIs to review
# Projects: https://help.getharvest.com/api-v2/projects-api/projects/projects/
# User Project Assigments: https://help.getharvest.com/api-v2/projects-api/projects/projects/
# Users: https://help.getharvest.com/api-v2/users-api/users/users/
# Time Report - Team Report API: https://help.getharvest.com/api-v2/reports-api/reports/time-reports/
