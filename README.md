
# Weather Forecasting using Time Series Data

## Objectives
Visualize and predict temperature and humidity data collected from dht11 sensor, Raspberry pi using a InfluxDB database.

## Equipment 
- Raspberry Pi  
- DHT11 Sensor  
- HD Monitor, Keyboard, Mouse, Power Supply  
- HDMI & connection cables

## Software Requirements
1. **Raspberry Pi Setup**  
   - Update package list:  
     ```bash
     sudo apt update && sudo apt upgrade
     ```  
   - Install Python libraries:  
     ```bash
     sudo apt install python3-pip
     pip3 install Adafruit_DHT influxdb-client
     ```
2. **Install InfluxDB**  
   - [InfluxDB Install Guide](https://docs.influxdata.com/influxdb/v2/install/)  
   - Set up InfluxDB, InfluxDB CLI, and configure your token.

3. **Install Python Libraries**  
   - ```bash
     pip install pandas matplotlib statsmodels influxdb-client
     ```

## Project Flow
1. Set up the Raspberry Pi and connect the DHT11 sensor to it.
2. Download and run the script `send_data_to_influxdb.py` to collect temperature and humidity data.
3. Visualize the data in InfluxDB’s web UI by starting the InfluxDB server (`influxd`) and exploring the data at `http://localhost:8086`.
4. Run `load_data_into_csv_file.py` to extract the data from InfluxDB into a CSV file (`output.csv`).
5. Use `weather_forecasting.py` to predict future temperature and humidity using the ARIMA model, and visualize the results.

## Execution Steps
1. Power up the Raspberry Pi and connect dht-11 sensor.
2. Run the data collection script:  
   ```bash
   python send_data_to_influxdb.py
3. Visualize the collected data in the InfluxDB web UI:
   1. Start the InfluxDB server using:
       ```bash
       influx
   3. Open the InfluxDB web UI in your browser at:
      ```bash
      http://localhost:8086
      
4. Extract the data from InfluxDB into a CSV file by running the following script:
     ```bash
   python load_data_into_csv_file.py
5. Run the Weather_forecasting code to predict future temperature and humidity values:
     ```bash
   python weather_forecasting.py
