import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd

key = "k2PvqBP6ycGDCbCb4lZcbIJohfnTLzv4"
lang = "pl"
url = "http://dataservice.accuweather.com"

city_key = ""

def getCity():
    city = entry.get()
    city_endpoint = url + "/locations/v1/cities/autocomplete?apikey=" + key + "&q="+ city + "&language="+lang
    json = requests.get(city_endpoint).json()
    city_name = json[0]['LocalizedName']
    global city_key
    city_key = json[0]['Key']
    label1.config(text = city_name+"\n"+city_key)
    return city_name

def getForecast3Days():
    forecast_endpoint = url + "/forecasts/v1/daily/5day/" + city_key + "?apikey=" + key + "&language=" + lang + "&metric=true"
    json = requests.get(forecast_endpoint).json()
    dates = []
    temps_max = []
    for i in range(3):
        dates.append(json['DailyForecasts'][i]['Date'][0:10])
        temps_max.append(json['DailyForecasts'][i]['Temperature']['Maximum']['Value'])
    forecast3days = pd.DataFrame({'data':dates,'temperatura':temps_max})
    return forecast3days


def getForecast3Hours():
    forecast3h_endpoint = url + "/forecasts/v1/hourly/12hour/" + city_key + "?apikey=" + key + "&language=" + lang + "&metric=true"
    json = requests.get(forecast3h_endpoint).json()
    hours = []
    descrips = []
    temps = []
    for i in range(3):
        hours.append(json[i]['DateTime'][11:16])
        descrips.append(json[i]['IconPhrase'])
        temps.append(json[i]['Temperature']['Value'])
    forecast3hours = pd.DataFrame({'godzina':hours,'opis':descrips,'temperatura':temps})
    return forecast3hours

def getCurrentConditions():
    current_endpoint = url + "/currentconditions/v1/" + city_key + "?apikey=" + key + "&language="+lang
    json = requests.get(current_endpoint).json()
    weather = json[0]['WeatherText']
    temp = json[0]['Temperature']['Metric']['Value']
    label1.config(text = str(temp)+"C"+"\n"+weather)
    return weather, temp


def getIndices1Day():
    indices_endpoint = url + "/indices/v1/daily/1day/" + city_key + "?apikey=" + key + "&language=" + lang
    json = requests.get(indices_endpoint).json()
    names = []
    categories = []
    for i in range(3):
       names.append(json[i]['Name'])
       categories.append(json[i]['Category'])
    indices1Day = pd.DataFrame({'nazwa':names, 'wartosc':categories})
    return indices1Day
    

def getIndices3Days():
    indices3_endpoint = url + "/indices/v1/daily/5day/" + city_key + "?apikey=" + key + "&language=" + lang
    json = requests.get(indices3_endpoint).json()
    names = []
    categories = []
    for j in range(3):
        for i in range(3):
            names.append(json[44*j+i]['Name'])
            categories.append(json[44*j+i]['Category'])
    indices3Days = pd.DataFrame({'nazwa':names, 'wartosc':categories})
    return indices3Days


def calculate():
    #teraz
    cityname = getCity()
    weather, temp = getCurrentConditions()
    label1.config(text = cityname+"\n"+str(temp)+" C"+"\n"+weather)
    indices_today = getIndices1Day()
    label1_1.config(text = indices_today.iloc[0]['nazwa']+'\n'+indices_today.iloc[0]['wartosc'])
    label1_2.config(text = indices_today.iloc[1]['nazwa']+'\n'+indices_today.iloc[1]['wartosc'])
    label1_3.config(text = indices_today.iloc[2]['nazwa']+'\n'+indices_today.iloc[2]['wartosc'])
    
    ttk.Separator(window).place(x=0, y=230, relwidth=1)
    #3godziny
    
    forecast3h = getForecast3Hours()
    label3h_1.config(text = forecast3h.iloc[0]['godzina']+"\n"+str(forecast3h.iloc[0]['temperatura'])+" C"+"\n"+forecast3h.iloc[0]['opis'])
    label3h_2.config(text = forecast3h.iloc[1]['godzina']+"\n"+str(forecast3h.iloc[1]['temperatura'])+" C"+"\n"+forecast3h.iloc[1]['opis'])
    label3h_3.config(text = forecast3h.iloc[2]['godzina']+"\n"+str(forecast3h.iloc[2]['temperatura'])+" C"+"\n"+forecast3h.iloc[2]['opis'])

    ttk.Separator(window).place(x=0, y=340, relwidth=1)
    #3dni
    forecast3d = getForecast3Days()
    indices3d = getIndices3Days()
    label3d_1.config(text = forecast3d.iloc[0]['data']+"\n"+str(forecast3d.iloc[0]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[0]["nazwa"]+ "\n" + indices3d.iloc[0]["wartosc"]+"\n"+"\n"+indices3d.iloc[1]["nazwa"]+ "\n" + indices3d.iloc[1]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[2]["nazwa"]+ "\n" + indices3d.iloc[2]["wartosc"])
    label3d_2.config(text = forecast3d.iloc[1]['data']+"\n"+str(forecast3d.iloc[1]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[3]["nazwa"]+ "\n" + indices3d.iloc[3]["wartosc"]+"\n"+"\n"+indices3d.iloc[4]["nazwa"]+ "\n" + indices3d.iloc[4]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[5]["nazwa"]+ "\n" + indices3d.iloc[5]["wartosc"])
    label3d_3.config(text = forecast3d.iloc[2]['data']+"\n"+str(forecast3d.iloc[2]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[6]["nazwa"]+ "\n" + indices3d.iloc[6]["wartosc"]+"\n"+"\n"+indices3d.iloc[7]["nazwa"]+ "\n" + indices3d.iloc[7]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[8]["nazwa"]+ "\n" + indices3d.iloc[8]["wartosc"])
    

window = tk.Tk()
window.geometry("1350x650")
window.title("Pogoda")

entry = tk.Entry(window, justify="center", width=30, font = "Georgia 15")
entry.grid(column = 1, row = 0)
entry.focus()
entry.bind('<Return>', lambda e: calculate())

but = tk.Button(window, text = "Pokaż", command = calculate, width=15)
but.grid(column = 2, row = 0)

#teraz
label1 = tk.Label(window, font=("Arial", 25))
label1.grid(column = 1, row = 1, rowspan=3)
label1_1 = tk.Label(window, font =("Arial", 20))
label1_1.grid(column = 0, row = 6, rowspan=2, padx = 20, pady = 10)
label1_2 = tk.Label(window, font =("Arial", 20))
label1_2.grid(column = 1, row = 6, rowspan=2, padx = 20, pady = 10)
label1_3 = tk.Label(window, font =("Arial", 20))
label1_3.grid(column = 2, row = 6, rowspan=2, padx = 20, pady = 10)


#3 godziny
label3h_1 = tk.Label(window, font=("Arial", 18))
label3h_1.grid(column = 0, row = 9, rowspan=3, padx=15, pady=10)
label3h_2 = tk.Label(window, font=("Arial", 18))
label3h_2.grid(column = 1, row = 9, rowspan=3, padx=15, pady=10)
label3h_3 = tk.Label(window, font=("Arial", 18))
label3h_3.grid(column = 2, row = 9, rowspan=3, padx=15, pady=10)


#3 dni
label3d_1 = tk.Label(window, font=("Arial", 15))
label3d_1.grid(column = 0, row = 13, rowspan=8, padx=10, pady=10)
label3d_2 = tk.Label(window, font=("Arial", 15))
label3d_2.grid(column = 1, row = 13, rowspan=8, padx=10, pady=10)
label3d_3 = tk.Label(window, font=("Arial", 15))
label3d_3.grid(column = 2, row = 13, rowspan=8, padx=10, pady=10)


window.mainloop()