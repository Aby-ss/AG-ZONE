from rich import print
from rich import text
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

from rich.traceback import install
install(show_locals=True)

from datetime import datetime
import numpy as np
import pandas as pd
import asciichartpy
import math

def equip_management():
    csv_path = 'EquipmentDB.csv'
    # Read the CSV file into a Pandas DataFrame
    data = pd.read_csv(csv_path)
    
    # Initialize the table
    EDB_table = Table(show_header=True, header_style="bold magenta")
    
    # Add columns to the table
    for column in data.columns:
        EDB_table.add_column(column)
    
    # Add rows to the table
    for row in data.values.tolist():
        EDB_table.add_row(*row)
    return Panel(EDB_table, title = "Equipment Database", title_align = "left", style = "Bold White")

equip_management()