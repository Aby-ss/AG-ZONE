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
    Equipment_DB = Table.grid(expand = True)
    Equipment_DB.add_column("Order No.", justify = "center", ratio = 1)
    Equipment_DB.add_column("Location", justify = "center")
    Equipment_DB.add_column("Status", justify = "right")
    Equipment_DB.add_column("Customer Name", justify = "right")
    Equipment_DB.add_row("[b]Order No.", "[b]Location", "[b]Status", "[b]Customer Name")
    Equipment_DB.add_row("456754678", "12th street, avenue", "[b green]In process", "Allen")
    Equipment_DB.add_row("546769867", "Main street, City block 12", "[b red]Late", "Chris")
    Equipment_DB.add_row("465787655", "City Centre, 22nd House", "[b yellow]Pending", "Cristiano")
    Equipment_DB.add_row("564467658", "24th House, Birmingham", "[b yellow]Pending", "Adam")
    Equipment_DB.add_row("687786578", "City Centre", "[b green]Done", "Leonel")

equip_management()