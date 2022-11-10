import requests
import json
from rich.panel import Panel
from rich import print

from rich.traceback import install
install(show_locals=True)

from rich.layout import Layout

# ---------------------------------------------------- BACKEND TESTING --------------------------------------------
symbol = 'WHEAT' 
base_currency = 'AED'
endpoint = 'latest'
access_key = 'y4iu0e109o4u611xu6hkvh3vc2ylgf3vipa39j4zb3hp6aweqsnuu3snh340'
resp = requests.get(
    'https://commodities-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))


currency = {resp.json()['data']['base']}
vege_rate = {resp.json()['data']['rates'][str(symbol)]}
vegetable = symbol
units = {resp.json()['data']['unit']}
date = {resp.json()['data']['date']}

output = f" Currency : {currency}\n Rate : {vege_rate}\n Vegetable = {vegetable}\n Unit || per -- : {units}\n Date of response : {date}"


print(Panel(f"{output}", title="[b]PASSED ✅", border_style='Green'))

print("---------------------------------------------------------------------------------------------------------------------------")
#
print
print(resp)
#
#print("----------------------------------------------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------


# ------------------------------------------    weather API ----------------------------------------------

api_key = "0c4d43f1d3c12b565156847bb4db7717"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = "Sharjah"
 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
response = requests.get(complete_url)
 
x = response.json()
 
if x["cod"] != "404":
 
    y = x['main']
 
    current_temperature = y["temp"]
 
    current_pressure = y["pressure"]
 
    current_humidity = y["humidity"]
 
    z = x["weather"]
 
    weather_description = z[0]["description"]
 
    weather_info = f" [bold red]Temperature[/bold red] (in kelvin unit) = {str(current_temperature)} \n [bold red]atmospheric pressure[/bold red] (in hPa unit) =  {str(current_pressure)} \n [bold red]humidity[/bold red] (in percentage) =  {str(current_humidity)} \n [bold red]description[/bold red] =  {str(weather_description)}"
    

# ---------------------------------------------------------------------------------------------------------
# ------------------------------  LOOP THROUGH SYMBOLS  ---------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

all_symbols = ["RICE","WHEAT","CORN","COFFEE","RUBBER","COTTON"]
all_base_currency = "AED"

access_key_2 = "y4iu0e109o4u611xu6hkvh3vc2ylgf3vipa39j4zb3hp6aweqsnuu3snh340"
endpoint = 'latest'

api_data = dict()

for i in all_symbols:
    loop_output = requests.get('https://commodities-api.com/api/'+endpoint+'?access_key='+access_key_2+'&base='+all_base_currency+'&symbols='+i) 
    loop_currency = {loop_output.json()['data']['base']}
    loop_vege_rate = {loop_output.json()['data']['rates'][str(i)]}
    loop_vegetable = i
    loop_units = {loop_output.json()['data']['unit']}
    loop_date = {loop_output.json()['data']['date']}
    
    loop_output = f"{loop_vege_rate} per : {loop_units}" 
    
    api_data.update({i: loop_output}) 
    
prnt_api_output = "{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in api_data.items()) + "}"  

print(Panel(f"{prnt_api_output}", title=f"[b]LOOP API TEST ✅", border_style='Green'))
 

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

layout = Layout()

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)

layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)

def _right():
    api_panel = Panel(f"{output}", title = "[b green]API output", border_style = "Green")
    
    return api_panel

def _left():
    weather_panel = Panel(f"{weather_info}", title = "[b green]Weather output", border_style = "Green")
    
    return weather_panel

def _header():
    header = Panel("Welcome To AG ZONE backend", title = "[b red] AG ZONE | BACKEND", border_style = "green")
    
    return header


layout["upper"].size = 5
layout["lower"].size = 20

layout["right"].update(_right())
layout["left"].update(_left())
layout["upper"].update(_header())

print(layout)

