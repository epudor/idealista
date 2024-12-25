import pandas as pd
import json
import requests
import base64

# Your API Key and Secret
API_KEY = ''
SECRET = ''

# Encode and base64-encode the API key and secret
api_key_secret = f"{API_KEY}:{SECRET}"
base64_credentials = base64.b64encode(api_key_secret.encode("utf-8")).decode("ascii")

# Set the headers for token request
token_headers = {
    "Authorization": f"Basic {base64_credentials}",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
}

# Data for token request
token_data = {
    "grant_type": "client_credentials",
    "scope": "read"
}

# API endpoint for token request
token_url = "https://api.idealista.com/oauth/token"

# Make the POST request to obtain the token
token_response = requests.post(token_url, headers=token_headers, data=token_data)

if token_response.status_code == 200:
    token_data = token_response.json()
    access_token = token_data.get("access_token")
    print("Access Token:", access_token)

    def fetch_idealista_data():
        country = 'es'
        locale = 'es'
        language = 'es'
        max_items = '50'
        minPrice = '400000'
        operation = 'sale'
        property_type = 'homes'
        order = 'publicationDate'
        center = '39.5172,3.3106'
        distance = '1000'
        sort = 'desc'
        bankOffer = 'false'

        limit = 10

        data_list = []  # Create an empty list to store data

        try:
            for i in range(1, limit):
                    
                # Define the request headers for property search
                search_headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
                }

                # Define the request data for property search
                search_data = {
                    "locale": locale,
                    "maxItems": max_items,
                    "numPage": i,
                    "minPrice": minPrice,
                    "operation": operation,
                    "propertyType": property_type,
                    "order": order,
                    "center": center,
                    "distance": distance,
                    "sort": sort,
                    "bankOffer": bankOffer
                    # Add other filters and parameters as needed
                }

                # Make a POST request for property search
                search_url = f'https://api.idealista.com/3.5/{country}/search'
                search_response = requests.post(search_url, headers=search_headers, data=search_data)

                # Parse the JSON response for property search
                response_data = search_response.json()
                print(response_data)

                # Append the data to the list
                data_list.extend(response_data.get('elementList', []))

            # Save the data to a JSON file
            with open(f'C:\\Users\\z\\Desktop\\Real Estate\\Idealista\\{property_type}_{operation}_{center}.json', 'w') as json_file:
                json.dump(data_list, json_file)
        except Exception as e:
            print(e)

fetch_idealista_data()
