import random
import requests
from rich.console import Console
from rich.panel import Panel

# Function to calculate potential yield based on field and weather factors
def calculate_yield(field_size, rainfall, temperature):
    base_yield = field_size * 50  # Base yield assumption: 50 tons per acre

    # Randomly adjust yield based on weather factors
    yield_adjustment = random.uniform(0.8, 1.2)  # Random adjustment between 0.8 and 1.2
    weather_yield = base_yield * yield_adjustment

    # Adjust yield based on rainfall
    if rainfall < 500:
        rainfall_yield = weather_yield * 0.8  # Reduce yield by 20% if rainfall is less than 500 mm
    elif rainfall > 1000:
        rainfall_yield = weather_yield * 1.2  # Increase yield by 20% if rainfall is greater than 1000 mm
    else:
        rainfall_yield = weather_yield

    # Adjust yield based on temperature
    if temperature < 20:
        temperature_yield = rainfall_yield * 0.9  # Reduce yield by 10% if temperature is less than 20°C
    elif temperature > 30:
        temperature_yield = rainfall_yield * 1.1  # Increase yield by 10% if temperature is greater than 30°C
    else:
        temperature_yield = rainfall_yield

    return temperature_yield


# Get input from the user
field_size = float(input("Enter the size of the field (in acres): "))
rainfall = float(input("Enter the average annual rainfall (in mm): "))

# Fetch temperature data from an API
response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London,uk")
weather_data = response.json()
temperature = weather_data.get("main", {}).get("temp", 0) - 273.15  # Convert temperature from Kelvin to Celsius

# Calculate the potential yield
potential_yield = calculate_yield(field_size, rainfall, temperature)

# Create a console object
console = Console()

# Display the potential yield in a panel
yield_panel = Panel.fit(
    f"The potential yield for a field of [bold]{field_size:.2f}[/bold] acres is [bold]{potential_yield:.2f}[/bold] tons.",
    title="Yield Forecast",
    border_style="green",
    padding=(1, 2),
)
console.print(yield_panel)
