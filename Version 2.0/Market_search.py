import requests
from rich import print, box
from rich.panel import Panel
from datetime import datetime
from rich.traceback import install
install(show_locals=True)

# Define the commodities and their seasonal demand
commodities = {
    "Apples": ["Fall"],
    "Pumpkins": ["Fall"],
    "Corn": ["Summer"],
    "Tomatoes": ["Summer"],
    "Strawberries": ["Spring"],
    "Watermelons": ["Summer"],
}

# Define additional factors for market research
additional_factors = {
    "Weather": {
        "API_URL": "https://api.weatherapi.com/v1/current.json",
        "location": "New York",  # Specify the desired location
    },
    "Population Growth": {
        "API_URL": "https://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?format=json",
    },
}

# Determine the current season
current_month = datetime.now().month
seasons = {
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Fall",
    10: "Fall",
    11: "Fall",
    12: "Winter",
}
current_season = seasons.get(current_month)

# Perform market research based on the current season
high_demand_commodities = [
    commodity for commodity, seasons in commodities.items() if current_season in seasons
]

# Display the results using Rich library
print("[bold]Market Research: High-Demand Commodities[/bold]")

# Current Season Panel
current_season_panel = Panel(f"[underline]Current Season[/underline]: {current_season}")
print(current_season_panel)

# High-Demand Commodities Panel
high_demand_panel_content = "\n".join(f"• {commodity}" for commodity in high_demand_commodities)
high_demand_panel = Panel(high_demand_panel_content, title="High-Demand Commodities")
print(high_demand_panel)

api_key = "0c4d43f1d3c12b565156847bb4db7717"
    
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_names = ["Sharjah"]
for i in city_names:
    loop_API_output = base_url + "appid=" + api_key + "&q=" + i

    response = requests.get(loop_API_output)
    
    x = response.json()
    
    if x["cod"] != "404":
    
        y = x['main']
    
        loop_current_temperature = y["temp"]
    
        loop_current_pressure = y["pressure"]
    
        loop_current_humidity = y["humidity"]
    
        z = x["weather"]
    
        loop_weather_description = z[0]["description"]
    
        weather_panel_content = f"Temperature: {loop_current_temperature}°C\nHumidity: {loop_current_humidity}%"


print(Panel(f"{weather_panel_content}", title = "Weather Data", title_align = "center", border_style = "bold white", box = box.SQUARE))


def population_growth():

    # Define additional factors for market research
    additional_factors = {
        "Population Growth": {
            "API_URL": "https://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?format=json",
        },
    }

    # Population Growth Panel
    population_data = requests.get(additional_factors["Population Growth"]["API_URL"])
    population_json = population_data.json()
    population_indicator = population_json[1][0]["indicator"]["value"]
    population_value = population_json[1][0]["value"]
    population_growth_panel_content = f"Indicator: {population_indicator}\nValue: {population_value}"
    population_growth_panel = Panel(f"{population_growth_panel_content}", title="Population Growth")
    print(population_growth_panel)
    
    
population_growth()