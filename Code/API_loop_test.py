import json
import requests
from rich import print
from rich.panel import Panel

from rich.traceback import install
install(show_locals=True)

# ---------------------------------------------------------------------------------------------------------
# ------------------------------  LOOP THROUGH SYMBOLS  ---------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

all_symbols = ["RICE","WHEAT","CORN","COFFEE","RUBBER","COTTON"]
all_base_currency = "AED"

access_key_2 = "fd95o5yj28iz3ukff9no7o5bmqvii5nx3mjqdlcsktz5h4rf1v8o4hk76722"
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
