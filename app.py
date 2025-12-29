from weather import get_weather
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name required"})
    
    result = get_weather(city)
    
    # Handle error case (when result is a string)
    if isinstance(result, str):
        return jsonify({"error": result})
    
    # Transform the weather data to match frontend expectations
    return jsonify({
        "city": result.get("City", ""),
        "temp": result.get("Temperature", "").replace(" °C", ""),
        "feels": result.get("Feels Like", "").replace(" °C", ""),
        "humidity": result.get("Humidity", "").replace(" %", ""),
        "condition": result.get("Weather", ""),
        "wind": result.get("Wind Speed", "").replace(" kph", "")
    })

if __name__ == '__main__':
    app.run(debug=True)