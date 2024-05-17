from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for the dropdowns
countries = {
    "usa": ["California", "Florida", "New York"],
    "canada": ["Alberta", "Ontario", "Quebec"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/states/<country>')
def states(country):
    state_list = countries.get(country.lower(), [])
    return jsonify(state_list)

if __name__ == "__main__":
    app.run(debug=True)
