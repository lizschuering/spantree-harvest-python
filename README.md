# spantree-harvest-python
Interacting with the Harvest API - this time with Python!

## How to Run Locally

To run locally, you will need:
1. Access to a [Harvest account](https://www.getharvest.com/)
2. A Personal Access Token
3. The Account ID for the Harvest account you want to interac with and pull data from

### Step 1: Generate Your Personal Access Token & Account ID

To obtain your Personal Access Token & Account ID, go to the [Developers section](https://id.getharvest.com/developers) of the Harvest website. Harvest will generate both for you when you click 'Create New Personal Access Token'.

### Step 2: Create A .env File To Store Your Credentials

Create a .env file in the root of the project and add the following variables which will store your Personal Access Token and Account ID:

    HARVEST_ACCESS_TOKEN = "Your_Personal_Access_Token_Goes_Here"
    HARVEST_ACCOUNT_ID = "Your_Account_ID_Goes_Here"

Save the file and voila! You are ready to run this project locally.