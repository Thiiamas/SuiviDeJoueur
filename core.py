
import requests

#Creds TO CHANGE
api_key = 'TOCHANGE'
document_id = 'TOCHANGE'
summoner_name = 'TOCHANGE'

def callAPI(url):
    print(f"calling {url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response
    else:
        print(f"Error: {response.status_code} - {response.text}")