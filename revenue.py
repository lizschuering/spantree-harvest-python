import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import date

# Harvest API Documenation: https://help.getharvest.com/api-v2/

# Time Period You're Looking At...
start_date = 20210101
end_date = 20210131

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

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)
# print(responseBody)

# See revenue per client for a given time period
for result in jsonResponse["results"]:
    if result["billable_amount"] > 0:
        print(result["client_name"] + " Revenue for the Period " + str(start_date) + " to " + str(end_date) + ": $" + str(result["billable_amount"]))

# See total revenue for a given time period
total_revenue = 0

for result in jsonResponse["results"]:
    total_revenue += result["billable_amount"]

print("Total Revenue for the Period " + str(start_date) + " to " + str(end_date) + ": $" + str(total_revenue))
