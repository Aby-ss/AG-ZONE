from rich.console import Console
from rich.table import Table
from datetime import datetime, timedelta

# Create a console object
console = Console()

# Create a table for displaying pest and disease information
pest_table = Table(show_header=True, header_style="bold blue")
pest_table.add_column("Pest/Disease", style="dim")
pest_table.add_column("Description")
pest_table.add_column("Treatment")

# Add data to the table with shorter descriptions
pest_table.add_row("Aphids", "Small sap-feeding insects", "Use insecticidal soap or neem oil")
pest_table.add_row("Powdery Mildew", "Fungal disease with white powdery coating", "Apply fungicide")
pest_table.add_row("Leafhoppers", "Insects causing leaf yellowing", "Use insecticidal spray")
pest_table.add_row("Black Spot", "Fungal disease causing black spots on leaves", "Remove infected leaves and apply fungicide")
pest_table.add_row("Caterpillars", "Larvae of butterflies and moths eating leaves", "Handpick or use organic insecticide")

# Print the whole table
console.print(pest_table)

