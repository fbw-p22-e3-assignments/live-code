# the requests module for intracting with APIs
import requests
import os
from dotenv import load_dotenv
import pprint

# Gathering all environment variables from the .env file
load_dotenv()

# # Endpoint for getting all models available on OpenAI
# url = "https://openai80.p.rapidapi.com/models"

# # Headers used to process your request
# # Dictionary
# headers = {
# 	"X-RapidAPI-Key": os.getenv('OPEN_AI_API_KEY'),
# 	"X-RapidAPI-Host": "openai80.p.rapidapi.com"
# }


# response = requests.get(url, headers=headers)

# print(response.json())

### Chat-GPT Mock
url = "https://openai80.p.rapidapi.com/chat/completions"

headers = {
	"X-RapidAPI-Key": os.getenv('OPEN_AI_API_KEY'),
	"X-RapidAPI-Host": "openai80.p.rapidapi.com",
	"content-type": "application/json",
}

prompt = True

while prompt:
    user_input = input("Do you have a question?")
    
    if user_input == "quit":
        prompt = False
    else:
        payload = {
		"model": "gpt-3.5-turbo",
		"messages": [
				{
					"role": "user",
					# Set content to the user input
					"content": user_input,
				}
			]
		}
        
        # Send request
        response = requests.post(url, json=payload, headers=headers)
        
        pprint.pprint(response.json()['choices'][0]['message']['content'])







