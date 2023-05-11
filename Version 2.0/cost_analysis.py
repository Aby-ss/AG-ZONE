import requests
from rich.console import Console
from rich.table import Table

# API endpoint for Trefle API
TREFLE_API_ENDPOINT = "https://trefle.io/api/v1/plants"

# API endpoint for World Bank API
WORLD_BANK_API_ENDPOINT = "https://api.worldbank.org/v2/country/all/indicator/AG.PRD.CROP.XD"

# Function to get crop information from Trefle API
def get_crop_info(crop_name):
    params = {"token": "<your_Trefle_API_token>", "q": crop_name}
    response = requests.get(TREFLE_API_ENDPOINT, params=params)
    if response.ok:
        data = response.json()["data"]
        if data:
            crop_data = data[0]
            return crop_data
    return None

# Function to get crop prices from World Bank API
def get_crop_prices(crop_name):
    params = {"format": "json", "MRV": "1", "per_page": "500", "source": "2",
              "date": "2019", "prefix": "PREFIX", "suffix": "SUFFIX"}
    response = requests.get(WORLD_BANK_API_ENDPOINT, params=params)
    if response.ok:
        data = response.json()[1]
        for item in data:
            if item["indicator"]["value"].lower() == crop_name:
                price = item["value"]
                return float(price)
    return None


# Function to calculate cost of production for a farmer
def calculate_cost_of_production(crop, area):
    # Assume the cost of production is 60% of the crop price
    crop_info = get_crop_info(crop)
    crop_price = get_crop_prices(crop)
    if crop_info and crop_price:
        cost_of_production = 0.6 * crop_price * area
        return cost_of_production
    return None

# Main function to display cost analysis for a farmer
def display_cost_analysis():
    console = Console()

    # Define a list of crops
    crops = ['wheat', 'corn', 'soybean', 'potato', 'tomato']

    # Define a fixed area of 500 hectares
    area = 500

    # Calculate cost of production for each crop
    costs_of_production = []
    for crop in crops:
        cost_of_production = calculate_cost_of_production(crop, area)
        costs_of_production.append(cost_of_production)

    # Display cost analysis in a table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Crop", style="dim", width=12)
    table.add_column("Area (ha)", style="dim", width=12)
    table.add_column("Crop Price", style="dim", width=12)
    table.add_column("Cost of Production", style="dim", width=18)

    for i, crop in enumerate(crops):
        crop_info = get_crop_info(crop)
        if crop_info:
            crop_name = crop_info["common_name"]
            crop_price = get_crop_prices(crop_name)
            if crop_price:
                table.add_row(crop_name, str(area), f"${crop_price:.2f}", f"${costs_of_production[i]:.2f}")
    
    console.print(table)

# Run the main function
if __name__ == "__main__":
    display_cost_analysis()