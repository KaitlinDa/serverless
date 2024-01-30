import requests
from urllib.parse import parse_qs, urlparse

def capital_finder(request):
    query = parse_qs(urlparse(request['path']).query)
    

    message = "Invalid request"
    status_code = 400


    if 'country' in query:
        country = query['country'][0]
        try:

            api_response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
            api_response.raise_for_status()  
            country_data = api_response.json()
            capital = country_data[0]['capital'][0]
            message = f"The capital of {country} is {capital}"
            status_code = 200
        except requests.RequestException:
            message = "Country not found or an error occurred"
            status_code = 404


    elif 'capital' in query:
        capital = query['capital'][0]
        try:

            api_response = requests.get(f"https://restcountries.com/v3.1/capital/{capital}")
            api_response.raise_for_status()  
            country_data = api_response.json()
            country = country_data[0]['name']['common']
            message = f"{capital} is the capital of {country}"
            status_code = 200
        except requests.RequestException:
            message = "Capital not found or an error occurred"
            status_code = 404

    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'text/plain'},
        'body': message
    }
