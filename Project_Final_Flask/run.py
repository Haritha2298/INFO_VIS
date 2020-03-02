from flask import Flask, render_template, url_for, request
# from app import app
import data

app = Flask(__name__)

# @app.route('/')
@app.route("/index", methods=["GET", "POST"])
def index():
    objects = ['Bridges', 'Buildings', 'Bus Stops', 'High Voltage Pylons',
               'Lamp Posts', 'Metro Stops', 'Parks', 'Playgrounds',
               'Sports Field', 'Toilets', 'Traffic Lights', 'Train Stations',
               'Tram Stops', 'Trash', 'Trees', 'Wind Turbines']
    if request.method == "POST":
        # Receive multiple objects by getlist method
        selected_object = request.form.getlist('kailai')
        print("connection succesfull")
        print(selected_object)
        data.read_data(selected_object)
    return render_template('index.html', objects=objects)


if __name__ == "__main__":
    app.run(debug=True)
