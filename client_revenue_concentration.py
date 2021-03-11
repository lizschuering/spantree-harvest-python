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
print("### Revenue By Client for the Period " + str(start_date) + " to " + str(end_date) + "###")
for result in jsonResponse["results"]:
    if result["billable_amount"] > 0:
        print(result["client_name"] + " Revenue for the Period " + ": $" + str(result["billable_amount"]))

# See total revenue for a given time period
total_revenue = 0

for result in jsonResponse["results"]:
    total_revenue += result["billable_amount"]

print("Total Revenue for the Period " + str(start_date) + " to " + str(end_date) + ": $" + str(total_revenue))

# See client revenue as percent of total for a given time period
client_percent_of_revenue = 0
client_revenues = {} #Empty dictionary to gather client & revenue percentages for a given period

print("### Percent of Revenue By Client for the Period " + str(start_date) + " to " + str(end_date) + "###")
for result in jsonResponse["results"]:
    if result["billable_amount"] > 0:
        client_percent_of_revenue = result["billable_amount"] / total_revenue
        client_revenues[result["client_name"]] = client_percent_of_revenue
        print(result["client_name"] + ": " + "{:.0%}".format(client_percent_of_revenue))

#print(client_revenues)

# Check for client with highest percentage of revenue for a given time period (largest client concentration ratio)
max_value = 0
max_key = []

for k, v in client_revenues.items():
    if v >= max_value:
        if v > max_value:
            max_value = v
            max_key = [k]
        else:
            max_key.append(k)

largest_client = max_key[0]

find_largest_client = [val for key, val in client_revenues.items() if largest_client in key]
largest_client_concentration = find_largest_client[0]

print("Highest Client Concentration Ratio - " + largest_client + ": " + "{:.0%}".format(largest_client_concentration))