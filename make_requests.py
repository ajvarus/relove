import requests 

# Template function - not to be used in production.
def get_crypt_type_from_interferon():
    url = "http://interferon:3000/api/encryption_types"
    
    # Headers to be sent with the request
    custom_headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
        'Content-Type': 'application/json'
    }

    # Parameters to be sent with the query string
    query_params = {
        'key1': 'value1',
        'key2': 'value2'
    }

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {
            "error": "Failed to fetch data"
        }