import json
import pandas as pd


def read_json(file):
    # Open the file
    with open(file, 'r') as f:
        # Load file
        data = json.load(f)
    # Return file
    return data


# Read Advertising Column
adv_column = read_json('../data/advertising_column.json')
# Create Advertising Column Dataframe
adv_column = pd.DataFrame.from_dict(adv_column['results'])

# Read Bicycle Route
bicycle_route = read_json('../data/bicycle_route.json')
# Create Bicycle Route Dataframe
bicycle_route = pd.DataFrame.from_dict(bicycle_route['results'])

# Read Bridge
bridge = read_json('../data/bridge.json')
# Create Bridge Dataframe
bridge = pd.DataFrame.from_dict(bridge['results'])

# Read Building
building = read_json('../data/building.json')
# Create Building Dataframe
building = pd.DataFrame.from_dict(building['results'])

# Read Bus Line
bus_line = read_json('../data/bus_line.json')
# Create Bus Line Dataframe
bus_line = pd.DataFrame.from_dict(bus_line['results'])

# Read Bus Stop
bus_stop = read_json('../data/bus_stop.json')
# Create Bus Stop Dataframe
bus_stop = pd.DataFrame.from_dict(bus_stop['results'])

# Read Ferry
ferry = read_json('../data/ferry.json')
# Create Ferry Dataframe
ferry = pd.DataFrame.from_dict(ferry['results'])

# Read High Voltage Pylon
high_voltage_pylon = read_json('../data/high_voltage_pylon.json')
# Create High Voltage Pylon Dataframe
high_voltage_pylon = pd.DataFrame.from_dict(high_voltage_pylon['results'])

# Read Lamp Post
lamp_post = read_json('../data/lamp_post.json')
# Create Lamp Post Dataframe
lamp_post = pd.DataFrame.from_dict(lamp_post['results'])

# Read Metro Line
metro_line = read_json('../data/metro_line.json')
# Create Metro Line Dataframe
metro_line = pd.DataFrame.from_dict(metro_line['results'])

# Read Metro Stop
metro_stop = read_json('../data/metro_stop.json')
# Create Metro Stop Dataframe
metro_stop = pd.DataFrame.from_dict(metro_stop['results'])

# Read Park
park = read_json('../data/park.json')
# Create Park Dataframe
park = pd.DataFrame.from_dict(park['results'])
