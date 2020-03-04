from flask import Flask, render_template, url_for, request
# from app import app
import data

app = Flask(__name__)
# Objects info dictionary
app.objects = {
    'Advertising Columns': {
        'count': None,
        'df': None,
        'url': 'advertising_column'
    },
    'Bridges': {
        'count': None,
        'df': None,
        'url': 'bridge'
    },
    'Toilets': {
        'count': None,
        'df': None,
        'url': 'toilet'
    }
}

# @app.route('/')
@app.route("/asd", methods=["GET", "POST"])
def index():
    objects = ['Bridges', 'Buildings', 'Bus Stops', 'High Voltage Pylons',
               'Lamp Posts', 'Metro Stops', 'Parks', 'Playgrounds',
               'Sports Field', 'Toilets', 'Traffic Lights', 'Train Stations',
               'Tram Stops', 'Trash', 'Trees', 'Wind Turbines']
    # Load only Bridges data in the beginning
    # This can be changed to couple more later ...
    objects_data = data.call_data(['Toilets'], app.objects)
    print(objects_data)
    if request.method == "POST":
        # Receive multiple objects by getlist method
        selected_objects = request.form.getlist('obj_list')
        print("connection succesfull")
        print(selected_objects)
        # Kailai way of importing data [COMMENTED OUT]
        # data.read_data(selected_object)
        # Read & Process the data and receive objects dictionary
        objects_data = data.call_data(selected_objects, app.objects)
        return render_template('index.html', objects=objects, objects_data=objects_data)
    return render_template('index.html', objects=objects, objects_data=objects_data)


if __name__ == "__main__":
    app.run(debug=True)
