import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()
import datetime

# Harvest API Documenation: https://help.getharvest.com/api-v2/

# Time Period You're Looking At...
start_date = 20210301
end_date = 20210307

### Uninvoiced Report Endpoint (Reports API) ###

uninvoiced_reports = "/v2/reports/uninvoiced"

url = "https://api.harvestapp.com" + uninvoiced_reports + \
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
print(jsonResponsePretty)

# See uninvoiced amount for each client
for result in jsonResponse["results"]:
    if result["uninvoiced_amount"] > 0:
        print(result["project_name"] + " uninvoiced amount: $" + str(result["uninvoiced_amount"]) + " for the period " + str(start_date) + " to " + str(end_date))


# Total up all uninvoiced amounts
total_uninvoiced = 0

for result in jsonResponse["results"]:
    if result["uninvoiced_amount"] > 0:
        total_uninvoiced += result["uninvoiced_amount"]

print("Total Univoiced Amount: $" + str(total_uninvoiced) + " for the period " + str(start_date) + " to " + str(end_date))