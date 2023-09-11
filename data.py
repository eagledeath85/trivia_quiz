import requests

URL_ENDPOINT = "https://opentdb.com/api.php"
# amount=10&type=boolean
parameters = {
    "amount": 10,
    "type": "boolean",
    # "category": 23,
    "difficulty": "easy",
}

def build_url(parameters, endpoint=URL_ENDPOINT):
    url_parameters = "&".join(f"{key}={value}" for key, value in parameters.items())
    url = endpoint + "?" + url_parameters
    return url

def get_response_from_api(url):
    response = requests.get(url=url)

    # Raise exception if error
    response.raise_for_status()

    return response.json()


############## Main Flow ##############
# Build the URL
url = build_url(parameters=parameters)

# Get the JSON response from the API
all_data = get_response_from_api(url)

# Get the questions in a list of dictionaries
question_data = all_data["results"]
