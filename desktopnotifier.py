#DESKTOP NOTIFIER PROGRAM FOR COVID-19
import requests
from win10toast import ToastNotifier
import datetime
try:
 data = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("check your internet connecton")   #its url base program so we need internet connection
    data = None      #no value assigned to data

if data is not None:     #there is some value in data
    getData = data.json()
    covid_India = getData["Success"]       #certain data is created using django following the link and all data is stored in success

    title = """ Covid-19 India / {}""".format(datetime.date.today())
    
    message= """ In India covid-19 total cases is : {}, deaths : {}, recovered : {}, today-case is : {}"""
    covid_India["deaths"],covid_India["recovered"],covid_India["todayCases"]
    
    toaster = ToastNotifier()     #we imported a class
    toaster._show_toast(title, message,icon_path=".covid-19.ico", duration=10)