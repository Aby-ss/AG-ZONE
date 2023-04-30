from rich import text
from rich import box
from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

from rich.live import Live
from rich.traceback import install
install(show_locals=True)
from rich.console import Console

from datetime import datetime
import numpy as np
import asciichartpy
import csv
import keyboard
from time import sleep
import psutil
import platform

layout = Layout()
layout.split_column(
        Layout(name = "Header"),
        Layout(name = "Body"),
        Layout(name = "Footer")
        )

layout["Body"].split_row(
        Layout(name = "Right"),
        Layout(name = "Left", size = 77)
        )
layout["Right"].split_column(
    Layout(name = "Right_upper"),
    Layout(name = "Right_lower")

)

layout["Header"].size = 3
layout["Footer"].size = 3

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand = True)
        grid.add_column(justify="left")
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")

        grid.add_row("🌿", "[b]AG ZONE[/]", datetime.now().ctime().replace(":", "[blink]:[/]"))

        return Panel(grid, style = "Bold white on Black")

class Footer:
    def __rich__(self) -> Panel:
        f_grid = Table.grid(expand=True)
        f_grid.add_column(justify="left")
        f_grid.add_column(justify="center")
        f_grid.add_column(justify="right")

        f_grid.add_row("🧠", "[b]Good Day Sir, All Systems Online", "📑")

        return Panel(f_grid, style = "Bold white on black")


layout["Header"].update(Header())
layout["Footer"].update(Footer())

print(layout)