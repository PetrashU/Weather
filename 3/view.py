import tkinter as tk
from tkinter import ttk
from view_model import ViewModel
import webbrowser
import threading
from Web import WebPage

class View(tk.Tk):
    def __init__(self, view_model: ViewModel, web: WebPage) -> None:
        super().__init__()
        self.view_model = view_model
        self.web = web
        self.title("Pogoda")
        self.geometry("1350x650")
        self.create_ui()

    def create_ui(self):
        self.entry = tk.Entry(self, justify="center",width = 30, font = "Georgia 15")
        self.entry.grid(column = 1, row = 0)
        self.entry.focus()
        self.entry.bind('<Return>', self.on_entry)

        self.but = tk.Button(self, text = "Pokaż prognozę", width=15)
        self.but.bind("<Button-1>", self.on_button_click)
        self.but.grid(column = 2, row = 0)

        self.btn = tk.Button(self, text = "Lista koszulek",width = 15, command=self.openweb)
        self.btn.grid(column=0, row = 0)

        #teraz
        self.label1 = tk.Label(self, font=("Arial", 25))
        self.label1.grid(column = 1, row = 1, rowspan=3)
        self.label1_1 = tk.Label(self, font =("Arial", 20))
        self.label1_1.grid(column = 0, row = 6, rowspan=2, padx = 20, pady = 10)
        self.label1_2 = tk.Label(self, font =("Arial", 20))
        self.label1_2.grid(column = 1, row = 6, rowspan=2, padx = 20, pady = 10)
        self.label1_3 = tk.Label(self, font =("Arial", 20))
        self.label1_3.grid(column = 2, row = 6, rowspan=2, padx = 20, pady = 10)


        #3 godziny
        self.label3h_1 = tk.Label(self, font=("Arial", 18))
        self.label3h_1.grid(column = 0, row = 9, rowspan=3, padx=15, pady=10)
        self.label3h_2 = tk.Label(self, font=("Arial", 18))
        self.label3h_2.grid(column = 1, row = 9, rowspan=3, padx=15, pady=10)
        self.label3h_3 = tk.Label(self, font=("Arial", 18))
        self.label3h_3.grid(column = 2, row = 9, rowspan=3, padx=15, pady=10)


        #3 dni
        self.label3d_1 = tk.Label(self, font=("Arial", 15))
        self.label3d_1.grid(column = 0, row = 13, rowspan=8, padx=10, pady=10)
        self.label3d_2 = tk.Label(self, font=("Arial", 15))
        self.label3d_2.grid(column = 1, row = 13, rowspan=8, padx=10, pady=10)
        self.label3d_3 = tk.Label(self, font=("Arial", 15))
        self.label3d_3.grid(column = 2, row = 13, rowspan=8, padx=10, pady=10)


    def on_entry(self, event= None) -> None:
        self.view_model.entry = self.entry.get()
        self.get_weather()

    def on_button_click(self, event=None) -> None:
        self.view_model.entry = self.entry.get()
        self.get_weather()

    def get_weather(self) -> None:
        #teraz
        cityname = self.view_model.getCity()
        weather, temp = self.view_model.getCurrentConditions()
        self.label1.config(text = cityname+"\n"+str(temp)+" C"+"\n"+weather)
        indices_today, indices3d = self.view_model.getIndices()
        self.label1_1.config(text = indices_today.iloc[0]['nazwa']+'\n'+indices_today.iloc[0]['wartosc'])
        self.label1_2.config(text = indices_today.iloc[1]['nazwa']+'\n'+indices_today.iloc[1]['wartosc'])
        self.label1_3.config(text = indices_today.iloc[2]['nazwa']+'\n'+indices_today.iloc[2]['wartosc'])
    
        ttk.Separator(self).place(x=0, y=230, relwidth=1)
        #3godziny
        forecast3h,forecast3d = self.view_model.getForecast()
        self.label3h_1.config(text = forecast3h.iloc[0]['godzina']+"\n"+str(forecast3h.iloc[0]['temperatura'])+" C"+"\n"+forecast3h.iloc[0]['opis'])
        self.label3h_2.config(text = forecast3h.iloc[1]['godzina']+"\n"+str(forecast3h.iloc[1]['temperatura'])+" C"+"\n"+forecast3h.iloc[1]['opis'])
        self.label3h_3.config(text = forecast3h.iloc[2]['godzina']+"\n"+str(forecast3h.iloc[2]['temperatura'])+" C"+"\n"+forecast3h.iloc[2]['opis'])

        ttk.Separator(self).place(x=0, y=340, relwidth=1)
        #3dni
        self.label3d_1.config(text = forecast3d.iloc[0]['data']+"\n"+str(forecast3d.iloc[0]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[0]["nazwa"]+ "\n" + indices3d.iloc[0]["wartosc"]+"\n"+"\n"+indices3d.iloc[1]["nazwa"]+ "\n" + indices3d.iloc[1]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[2]["nazwa"]+ "\n" + indices3d.iloc[2]["wartosc"])
        self.label3d_2.config(text = forecast3d.iloc[1]['data']+"\n"+str(forecast3d.iloc[1]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[3]["nazwa"]+ "\n" + indices3d.iloc[3]["wartosc"]+"\n"+"\n"+indices3d.iloc[4]["nazwa"]+ "\n" + indices3d.iloc[4]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[5]["nazwa"]+ "\n" + indices3d.iloc[5]["wartosc"])
        self.label3d_3.config(text = forecast3d.iloc[2]['data']+"\n"+str(forecast3d.iloc[2]["temperatura"])+" C"
                     +"\n"+"\n"+indices3d.iloc[6]["nazwa"]+ "\n" + indices3d.iloc[6]["wartosc"]+"\n"+"\n"+indices3d.iloc[7]["nazwa"]+ "\n" + indices3d.iloc[7]["wartosc"]
                            +"\n"+"\n"+indices3d.iloc[8]["nazwa"]+ "\n" + indices3d.iloc[8]["wartosc"])
        
    def run_api(self):
        self.web.run()

    def openweb(self):
        background_thread = threading.Thread(target=self.run_api, daemon=True)
        background_thread.start()
        webbrowser.open("http://localhost:81/page",new=1)