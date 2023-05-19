from rich.console import Console
from rich.table import Table
from datetime import datetime, timedelta

# Create a console object
console = Console()

# Create a table for displaying pest and disease information
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Pest/Disease", style="dim")
table.add_column("Description")
table.add_column("Treatment")

# Add data to the table with shorter descriptions
table.add_row("Aphids", "Small sap-feeding insects", "Use insecticidal soap or neem oil")
table.add_row("Powdery Mildew", "Fungal disease with white powdery coating", "Apply fungicide")
table.add_row("Leafhoppers", "Insects causing leaf yellowing", "Use insecticidal spray")
table.add_row("Black Spot", "Fungal disease causing black spots on leaves", "Remove infected leaves and apply fungicide")
table.add_row("Caterpillars", "Larvae of butterflies and moths eating leaves", "Handpick or use organic insecticide")

# Print the whole table
console.print(table)

# Pest scheduler
console.print("\n[bold cyan]Pest Scheduler:[/bold cyan]\n")

current_date = datetime.now()
end_date = current_date + timedelta(days=30)

while current_date <= end_date:
    console.print(f"\n[bold yellow]{current_date.strftime('%Y-%m-%d')}:[/bold yellow]\n")
    console.print(table)
    current_date += timedelta(days=7)