from influxdb_client import InfluxDBClient
import pandas as pd

url = "http://192.168.116.2:8086" # Enter your influxDB server URL
token = "sWrMXywylSLRJOgB7Y187AVcd_Gc-FTuX80hHAsLVoO-ajHrSqSRRVKXJMDSmTL2x2EkOysDpvRWNWLqaI6Fvw==" # Enter your authentication token used to connect to InfluxDB        
org = "Org1"  # Enter the name of your organization in InfluxDB                     
bucket = "bucket1" # Enter the name of your bucket where data is stored in InfluxDB


client = InfluxDBClient(url=url, token=token, org=org) # Initialize the InfluxDB client with the server URL, authentication token, and organization
query_api = client.query_api() # Create an instance of the query API to execute queries

# Write query to extract the data from influxdb database
query = f'from(bucket: "{bucket}") |> range(start: -30d) |> filter(fn: (r) => r._measurement == "dht11_sensor") |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")'


data_frame = query_api.query_data_frame(query) # Execute the query and store the result in a DataFrame

print("Queried Data:")
print(data_frame.head()) # Display the first few rows of the DataFrame

data_frame.to_csv('output.csv', index=False) # Save the DataFrame to a CSV file named 'output.csv' without including the index

print("Data successfully saved to output.csv")
