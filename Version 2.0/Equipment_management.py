from rich.console import Console
from rich.table import Table
import pandas as pd

def Equip_man():
    # Read CSV file into a pandas DataFrame
    data = pd.read_csv("C:\\Users\\hadir\\Documents\\VSC - Projects\\Python\\AG-ZONE\\Version 2.0\\EquipmentDB.csv")

    # Create a Rich table object
    table = Table(title="My CSV Data")

    # Add header to the table
    for col in data.columns:
        table.add_column(col)

    # Add data to the table
    for row in data.values:
        table.add_row(*row)

    # Create a Rich console object
    console = Console()

    # Print the table to the console
    return table