import Adafruit_DHT
from influxdb_client import InfluxDBClient, Point, WriteOptions
import time

# Set the DHT11 sensor type and the GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# InfluxDB connection settings
influxdb_url = "http://192.168.1.4:8086" # Enter your influxDB server URL
influxdb_token = "sWrMXywylSLRJOgB7Y187AVcd_Gc-FTuX80hHAsLVoO-ajHrSqSRRVKXJMDSmTL2x2EkOysDpvRWNWLqaI6Fvw==" # Enter your authentication token used to connect to InfluxDB
influxdb_org = "Org1" # Enter the name of your organization in InfluxDB
influxdb_bucket = "bucket1" # Enter the name of your bucket where data is stored in InfluxDB

# Initialize InfluxDB client
client = InfluxDBClient(url=influxdb_url, token=influxdb_token)
write_api = client.write_api(write_options=WriteOptions(batch_size=1))

while True:
   
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)  # Read data from DHT11 sensor
    
    if humidity is not None and temperature is not None:
        # Create a point for InfluxDB
        point = Point("dht11_sensor") \
            .tag("location", "bangalore") \
            .field("temperature", temperature) \
            .field("humidity", humidity)
        
        write_api.write(bucket=influxdb_bucket, org=influxdb_org, record=point)  # Write the point to InfluxDB

        print(f"Temperature: {temperature:.1f}C Humidity: {humidity:.1f}%")
    else:
        print("Failed to retrieve data from dht11 sensor")

    time.sleep(10) # Wait before taking the next reading
