import urllib
import json
import pandas as pd


def read_data(selected_value):
    panaroma_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/panoramas")
    data = json.loads(panaroma_url.read())
    panaroma_data = pd.DataFrame.from_dict(data['results'])
    main_data = panaroma_data

    if selected_value == "Playgrounds":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/playground")
        data = json.loads(json_url.read())
        playground_data = pd.DataFrame.from_dict(data['results'])
        data = playground_data
    if selected_value == "advertising_column":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/advertising_column")
        data = json.loads(json_url.read())
        advert_data = pd.DataFrame.from_dict(data['results'])
        data = advert_data
    if selected_value == "Bridges":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/bridge")
        data = json.loads(json_url.read())
        bridge_data = pd.DataFrame.from_dict(data['results'])
        data = bridge_data
    if selected_value == "Buildings":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/building")
        data = json.loads(json_url.read())
        building_data = pd.DataFrame.from_dict(data['results'])
        data = building_data
    if selected_value == "Bus Stops":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/bus_stop")
        data = json.loads(json_url.read())
        bus_stop_data = pd.DataFrame.from_dict(data['results'])
        data = bus_stop_data
    if selected_value == "High Voltage pylons":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/high_voltage_pylon")
        data = json.loads(json_url.read())
        hv_data = pd.DataFrame.from_dict(data['results'])
        data = hv_data
    if selected_value == "Lamp Posts":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/lamppost")
        data = json.loads(json_url.read())
        lamp_data = pd.DataFrame.from_dict(data['results'])
        data = lamp_data
    if selected_value == "Metro Stops":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/metro_stop")
        data = json.loads(json_url.read())
        metro_data = pd.DataFrame.from_dict(data['results'])
        data = metro_data
    if selected_value == "Train Stations":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/train_line")
        data = json.loads(json_url.read())
        train_data = pd.DataFrame.from_dict(data['results'])
        data = train_data
    if selected_value == "Parks":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/park")
        data = json.loads(json_url.read())
        park_data = pd.DataFrame.from_dict(data['results'])
        data = park_data
    if selected_value == "Sports Field":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/sports_field")
        data = json.loads(json_url.read())
        sports_data = pd.DataFrame.from_dict(data['results'])
        data = sports_data
    if selected_value == "Toilets":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/toilet")
        data = json.loads(json_url.read())
        toilet_data = pd.DataFrame.from_dict(data['results'])
        data = toilet_data
    if selected_value == "Wind Turbines":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/wind_turbine")
        data = json.loads(json_url.read())
        wind_data = pd.DataFrame.from_dict(data['results'])
        data = wind_data
    if selected_value == "Trees":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/tree")
        data = json.loads(json_url.read())
        tree_data = pd.DataFrame.from_dict(data['results'])
        data = tree_data
    if selected_value == "Trash":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/trash")
        data = json.loads(json_url.read())
        trash_data = pd.DataFrame.from_dict(data['results'])
        data = trash_data
    if selected_value == "Tram Stops":
        json_url = urllib.request.urlopen("https://vps.inskegroenen.nl/api/tram_stop")
        data = json.loads(json_url.read())
        tram_data = pd.DataFrame.from_dict(data['results'])
        data = tram_data

    return data, main_data


def return_singles(df):
    # Create empty list to be returned
    singles = list()
    # Go through each column
    for column in df.columns:
        # If column has only 1 item
        if len(df[column].unique()) == 1:
            # Append that column name to the list
            singles.append(column)
    # Return singles
    return singles


def call_data(obj_list: list, objects: dict):
    for obj in obj_list:
        # Key control
        if obj not in objects:
            print(obj, 'is not located in the dict, please add later...')
            continue
        # Get data from the API
        data = urllib.request.urlopen(
            "https://vps.inskegroenen.nl/api/" + objects[obj]['url'])
        # Read as json
        data = json.loads(data.read())
        # If count info exist in data
        if 'count' in data:
            # Assign count of the object
            objects[obj]['count'] = data['count']
        # Create dataframe from the read json file
        df = pd.DataFrame.from_dict(data['results'])
        # Get the unnecessary column list
        singles = return_singles(df)
        # Drop those unnecessary columns
        df = df.drop(singles, axis=1)
        # Assign df, as converted to json format, into the dictionary
        objects[obj]['df'] = df.to_json()
    # Return updated dictionary
    return objects
