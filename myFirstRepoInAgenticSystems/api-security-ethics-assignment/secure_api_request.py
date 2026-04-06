import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("My_API_KEY")

# Define the request details
url = "https://api.example.com/data"
headers = {"Authorization": f"Bearer {api_key}"}
try: 
     # Send GET request to the API  
     response = requests.get(url, headers=headers)

     # Handle the status code of the response
     if response.status_code == 200:
          print("Request successful!")
          print(response.json())
     elif response.status_code == 429:
          print("Rate limit exceeded. Please try again later.")
     else:
          print(f"Request failed with status code: {response.status_code}")
          
except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

     