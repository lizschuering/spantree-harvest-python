# spantree-harvest-python
Interacting with the Harvest API - this time with Python!

## How to Run Locally

To run locally, you will need:
    1. Access to a Harvest account
    2. A Personal Access Token
    3. The Account ID for the Harvest account you are interacting with

### Obtaining a Personal Access Token & Account ID

To obtain your Personal Access Token & Account ID, go to the [Developers section](https://id.getharvest.com/developers) of the Harvest website. Harvest will generate both for you when you click 'Create New Personal Access Token'

### Create a .env file

Create a .env file in the root of the project and add the following variables:

    HARVEST_ACCESS_TOKEN = "Your_Token_Goes_Here"
    HARVEST_ACCOUNT_ID = "Your_Account_ID_Goes_Here"

Voila! You are ready to run this project locally on your machine.