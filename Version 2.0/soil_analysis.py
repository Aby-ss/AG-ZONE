from rich import box
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.progress import Progress

from rich.traceback import install
install(show_locals=True)

import time
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Define the input data
# The input data includes soil properties like pH, organic matter content, nitrogen levels, etc.
X = np.array([[6.5, 2.3, 1.2, 0.3],
              [7.2, 1.8, 1.0, 0.2],
              [6.8, 2.0, 1.1, 0.4],
              [6.3, 2.5, 1.4, 0.5],
              [7.0, 1.5, 0.9, 0.1]])

# Define the output data
# The output data includes the soil's health rating, which is a number from 0 to 10.
y = np.array([8, 7, 8, 6, 9])

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Define a function to predict the soil's health rating based on input data
def predict_soil_health(pH, om, nitrogen, phosphorus):
    input_data = np.array([[pH, om, nitrogen, phosphorus]])
    soil_health = model.predict(input_data)
    
    with Progress() as progress:

        task1 = progress.add_task("[red]Downloading...", total=1000)
        task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[blue]Uploading...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=6)
            progress.update(task2, advance=4)
            progress.update(task3, advance=5)
            time.sleep(0.02)
            
            
    return Panel.fit(f"{soil_health[0]}", title = "Soil Heath Data", title_align = "left", border_style = "bold green", box = box.SQUARE)

# Test the function with some input values
pH = Prompt.ask("Enter your soil's detected pH level")
om = Prompt.ask("Enter your soil's detected om levels")
nitrogen = Prompt.ask("Enter your soil's detected nitrogen level")
phosphorus = Prompt.ask("Enter your soil's detected phosphorus level")
predicted_soil_health = predict_soil_health(pH, om, nitrogen, phosphorus)

# Print the predicted soil health rating
print(predicted_soil_health)