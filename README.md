Idealista Real Estate Data Scraper

This Python script fetches property listings from Idealista based on specified search criteria. It utilizes the Idealista API to retrieve data and saves the results in JSON format.

Requirements

Python 3 (tested with 3.x)
pandas (for potential future data manipulation)
requests (for making API requests)
base64 (for encoding API credentials)
json (for JSON parsing and saving)
Installation

Install the required libraries using pip:

Bash

pip install pandas requests base64 json
Clone or download this repository.

Usage

Obtain Idealista API Credentials:

Create an Idealista developer account
Generate an API key and secret from your developer dashboard.
Update API Credentials:

Replace the placeholders '' in API_KEY and SECRET variables with your actual credentials at the beginning of the script.
Run the Script:

Bash

python idealista_scraper.py
Explanation

Authentication:

Encodes and base64-encodes your API credentials for secure authorization.
Obtains an access token using the requests library for API interaction.
Data Fetching:

Defines default search parameters (country, locale, language, etc.) You can customize these parameters to filter listings according to your needs.
Iterates through multiple pages to retrieve a larger set of results (adjustable with limit).
Constructs API request headers and data with the access token and search parameters.
Makes POST requests to the Idealista API for property search.
Parses the JSON response to extract property data.
Saving Results:

Creates a list to store retrieved property data.
Appends data from each page to the list.
Saves the accumulated data in a JSON file named according to the search criteria (e.g., homes_sale_39.5172,3.3106.json).
Customization

Modify the default search parameters in the fetch_idealista_data function.
Add additional search filters (e.g., property size, number of bedrooms) by adjusting the search_data dictionary.
Implement data processing using pandas (if needed) to analyze or manipulate the retrieved data.
Disclaimer

This script is intended for educational purposes and personal use. Be mindful of Idealista's API usage limits and terms of service. 
