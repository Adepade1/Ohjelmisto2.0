import requests

#Tehtävä 1

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(f"{json_vastaus['value']}")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


#Tehtävä 2

hakusana = input("Hakusana")
pyyntöX = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + \
          "&appid=8ef406a6dbb491658bcb473f6242aa69&units=metric&lang=fi"
try:
    vastausX = requests.get(pyyntöX)
    if vastausX.status_code == 200:
        json_vastaus = vastausX.json()
    print(f"keli: {json_vastaus['weather'][0] ['description']}")
    print(f"Lämpötila: {json_vastaus['main']['temp']}C°")

except:
    print ("Hakua ei voitu suorittaa.")