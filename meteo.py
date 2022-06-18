import requests
import os
import hug


@hug.get('/echo')
def echo(lat:hug.types.text, lon:hug.types.text):

    url = "http://api.openweathermap.org/data/2.5/weather?"

    url = url + "lat=" + lat + "&lon=" + lon + "&appid=" + str(os.environ.get('API_KEY'))
    
    response = requests.get(url).json()

    
    if response["cod"] == "404":
        return ("erreur")
    else:
        return response
"""    
@hug.get('/health')
def health(lat:hug.types.text, lon:hug.types.text):
    url = 'http://devops-20180532.francecentral.azurecontainer.io/echo?lat=' + lat + "&lon=" + lon
    health_api_response = requests.get(url, verify=False)

    if not health_api_response:
        api_test_fail = True
        logger.error(f"Could not get /health response, the test has been failed!")
    elif health_api_response.status_code != 200:
        api_test_fail = True
        logger.error(f"Bad /health response, the test has been failed!")
    elif health_api_response.status_code == 200:
        logger.debug(f"Success /health API test,")
"""
 
hug.API(__name__).http.serve(port=80) 
