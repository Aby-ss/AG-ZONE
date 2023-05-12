from rich.console import Console
from rich.table import Table

# Create a console object to output the results
console = Console()

# Define a table to display the irrigation schedule
schedule_table = Table(title="Irrigation Schedule")
schedule_table.add_column("Day")
schedule_table.add_column("Zone 1")
schedule_table.add_column("Zone 2")
schedule_table.add_column("Zone 3")

# Define the irrigation zones and their watering requirements (in minutes)
zones = {"Zone 1": 20, "Zone 2": 30, "Zone 3": 40}

# Define the available watering times (in minutes)
watering_times = [15, 30, 45, 60]

# Get the user's input for the lawn area and the desired watering frequency
lawn_area = float(input("Enter the lawn area (in square meters): "))
watering_frequency = int(input("Enter the desired watering frequency (in days): "))

# Calculate the daily water requirement (in liters) based on the lawn area
water_requirement = lawn_area * 4

# Calculate the watering time (in minutes) for each zone based on the water requirement and the zone's watering requirement
zone_watering_times = {}
for zone in zones:
    zone_watering_times[zone] = int((zones[zone] / 60) * water_requirement)

# Generate the irrigation schedule for the next 7 days
for day in range(1, 8):
    schedule_row = [f"Day {day}"]
    for zone in zones:
        schedule_row.append(f"{zone_watering_times[zone]} min")
    schedule_table.add_row(*schedule_row)

# Print the irrigation schedule
console.print(schedule_table)