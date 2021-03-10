import urllib.request
import json
import os
from dotenv import load_dotenv
load_dotenv()
import datetime

# Harvest API Documenation: https://help.getharvest.com/api-v2/

### Invoices Report Endpoint (Invoices API) ###

#Only show me invoices that have a status of 'open' (ie. have not been paid yet)
open_invoices = "/v2/invoices?state=open"

url = "https://api.harvestapp.com" + open_invoices
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
# print(responseBody)

# List all currently unpaid invoies
for invoice in jsonResponse["invoices"]:
    print(invoice["client"]["name"] + " | Invoice #" + invoice["number"] + ": $" + str(invoice["amount"]))

# Total up all the unpaid invoice amounts
total_unpaid = 0

for invoice in jsonResponse["invoices"]:
    print(invoice["client"]["name"] + " | Invoice #" + invoice["number"] + ": $" + str(invoice["amount"]))
    total_unpaid += invoice["amount"]

print("Total Outstanding Invoices: $" + str(total_unpaid))