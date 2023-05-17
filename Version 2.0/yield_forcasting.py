import numpy as np
from sklearn.linear_model import LinearRegression
from rich import print

# Historical data (year, yield in tons)
years = np.array([2010, 2011, 2012, 2013, 2014, 2015])
yields = np.array([4.5, 5.1, 5.6, 5.9, 6.3, 6.8])

# Create a linear regression model
model = LinearRegression()

# Fit the model with the historical data
model.fit(years.reshape(-1, 1), yields)

# Get input from the user
new_year = int(input("Enter the year for yield prediction: "))

# Predict the yield for the new year
predicted_yield = model.predict([[new_year]])

# Print the predicted yield using rich module
print(f"The predicted yield for [bold]{new_year}[/bold] is [bold green]{predicted_yield[0]:.2f}[/] tons.")
