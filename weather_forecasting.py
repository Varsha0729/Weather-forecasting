import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the data
data = pd.read_csv('C:/Users/sajja/OneDrive/Desktop/influxDB/influxdb2-2.7.6-windows/output.csv')

# Convert the '_time' column to datetime and set it as the index
data['_time'] = pd.to_datetime(data['_time'], format='%Y-%m-%d %H:%M:%S.%f%z')
data.set_index('_time', inplace=True)

# Sort the data by time if necessary
data = data.sort_index()

# Extract the target series (_value column) for humidity and temperature
humidity_series = data['humidity']
temperature_series = data['temperature']

# Plot the data for humidity and temperature
plt.figure(figsize=(12, 6))


# Plot the humidity time series
plt.subplot(2, 1, 1)
plt.plot(humidity_series, label='Actual Humidity')
plt.title('Humidity Time Series Data')
plt.xlabel('Time')
plt.ylabel('Humidity')


# Plot the temperature time series
plt.subplot(2, 1, 2)
plt.plot(temperature_series, label='Actual Temperature', color='orange')
plt.title('Temperature Time Series Data')
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.tight_layout()
plt.show()

# Define and fit ARIMA models for both humidity and temperature
humidity_model = ARIMA(humidity_series, order=(2, 0, 1))
humidity_model_fit = humidity_model.fit() # Fit the ARIMA model for humidity

temperature_model = ARIMA(temperature_series, order=(2, 0, 1))
temperature_model_fit = temperature_model.fit() # Fit the ARIMA model for temperature

# Print model summaries
print("Humidity Model Summary:")
print(humidity_model_fit.summary())

print("\nTemperature Model Summary:")
print(temperature_model_fit.summary())

forecast_steps = 20  # Enter the number of steps ahead for forecasting

# Forecast for humidity
humidity_forecast = humidity_model_fit.get_forecast(steps=forecast_steps)
humidity_forecast_index = pd.date_range(start=humidity_series.index[-1], periods=forecast_steps + 1, freq='D')[1:]
humidity_forecast_df = humidity_forecast.predicted_mean.to_frame(name='Forecast')
humidity_forecast_df.index = humidity_forecast_index

# Forecast for temperature
temperature_forecast = temperature_model_fit.get_forecast(steps=forecast_steps)
temperature_forecast_index = pd.date_range(start=temperature_series.index[-1], periods=forecast_steps + 1, freq='D')[1:]
temperature_forecast_df = temperature_forecast.predicted_mean.to_frame(name='Forecast')
temperature_forecast_df.index = temperature_forecast_index

# Plot the actual vs predicted values for both humidity and temperature
plt.figure(figsize=(14, 12))

# Plot actual vs predicted humidity
plt.subplot(2, 1, 1)
plt.plot(humidity_series, label='Actual Humidity')
plt.plot(humidity_forecast_df, label='Predicted Humidity', linestyle='--')
plt.legend()
plt.title('Actual vs Predicted Humidity')
plt.xlabel('Time')
plt.ylabel('Humidity')

# Plot actual vs predicted temperature
plt.subplot(2, 1, 2)
plt.plot(temperature_series, label='Actual Temperature', color='orange')
plt.plot(temperature_forecast_df, label='Predicted Temperature', linestyle='--', color='red')
plt.legend()
plt.title('Actual vs Predicted Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.tight_layout() # Adjust the layout to prevent overlapping
plt.show() # Display the plots

