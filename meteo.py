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
        


hug.API(__name__).http.serve(port=80) 
