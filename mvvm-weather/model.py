import requests
import pandas as pd
import tkinter as tk

class Model:

    key = "ij8byQba9audqEvpB12IduN4iLyuyNWX"
    lang = "pl"
    url = "http://dataservice.accuweather.com"

    def __init__(self) -> None:
        self.city_key = ""

    def getCity(self, entry: tk.StringVar) -> str:
        city_endpoint = self.url + "/locations/v1/cities/autocomplete?apikey=" + self.key + "&q="+ entry.get() + "&language="+ self.lang
        json = requests.get(city_endpoint).json()
        city_name = json[0]['LocalizedName']
        self.city_key = json[0]['Key']
        return city_name
    
    def getForecast(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        forecast3h_endpoint = self.url + "/forecasts/v1/hourly/12hour/" + self.city_key + "?apikey=" + self.key + "&language=" + self.lang + "&metric=true"
        json = requests.get(forecast3h_endpoint).json()
        hours = []
        descrips = []
        temps = []
        for i in range(3):
           hours.append(json[i]['DateTime'][11:16])
           descrips.append(json[i]['IconPhrase'])
           temps.append(json[i]['Temperature']['Value'])
        forecast3hours = pd.DataFrame({'godzina':hours,'opis':descrips,'temperatura':temps})

        forecast_endpoint = self.url + "/forecasts/v1/daily/5day/" + self.city_key + "?apikey=" + self.key + "&language=" + self.lang + "&metric=true"
        json = requests.get(forecast_endpoint).json()
        dates = []
        temps_max = []
        for i in range(3):
            dates.append(json['DailyForecasts'][i]['Date'][0:10])
            temps_max.append(json['DailyForecasts'][i]['Temperature']['Maximum']['Value'])
        forecast3days = pd.DataFrame({'data':dates,'temperatura':temps_max})

        return forecast3hours, forecast3days
    
    def getCurrentConditions(self) -> tuple[str,float]:
        current_endpoint = self.url + "/currentconditions/v1/" + self.city_key + "?apikey=" + self.key + "&language="+ self.lang
        json = requests.get(current_endpoint).json()
        weather = json[0]['WeatherText']
        temp = json[0]['Temperature']['Metric']['Value']
        return weather, temp
    
    def getIndices(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        indices_endpoint = self.url + "/indices/v1/daily/1day/" + self.city_key + "?apikey=" + self.key + "&language=" + self.lang
        json = requests.get(indices_endpoint).json()
        names = []
        categories = []
        for i in range(3):
            names.append(json[i]['Name'])
            categories.append(json[i]['Category'])
        indices1Day = pd.DataFrame({'nazwa':names, 'wartosc':categories})  

        indices3_endpoint = self.url + "/indices/v1/daily/5day/" + self.city_key + "?apikey=" + self.key + "&language=" + self.lang
        json = requests.get(indices3_endpoint).json()
        names = []
        categories = []
        for j in range(3):
            for i in range(3):
                names.append(json[44*j+i]['Name'])
                categories.append(json[44*j+i]['Category'])
        indices3Days = pd.DataFrame({'nazwa':names, 'wartosc':categories})
        return indices1Day, indices3Days        