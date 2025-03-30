import json
from datetime import datetime

# ✅ Function to convert ISO timestamp to milliseconds
def iso_to_millis(iso_timestamp):
    dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)

# ✅ Convert data-1.json to target format
def convert_data_1(data):
    return {
        "deviceID": data["deviceID"],
        "deviceType": data["deviceType"],
        "timestamp": data["timestamp"],  # Already in milliseconds
        "location": data["location"],
        "operationStatus": data["operationStatus"],
        "temp": data["temp"]
    }

# ✅ Convert data-2.json to target format
def convert_data_2(data):
    return {
        "deviceID": data["device"]["id"],
        "deviceType": data["device"]["type"],
        "timestamp": iso_to_millis(data["timestamp"]),  # Convert ISO to milliseconds
        "location": f"{data['country']}/{data['city']}/{data['area']}/{data['factory']}/{data['section']}",  # Merge location fields
        "operationStatus": data["data"]["status"],
        "temp": data["data"]["temperature"]
    }

# ✅ Test code
if __name__ == "__main__":
    # Load JSON files
    with open("data-1.json", "r") as f1, open("data-2.json", "r") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    # Convert and print results
    result1 = convert_data_1(data1)
    result2 = convert_data_2(data2)

    print("Converted Data-1:", json.dumps(result1, indent=4))
    print("Converted Data-2:", json.dumps(result2, indent=4))
