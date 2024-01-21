from flask import Flask, render_template, redirect, url_for, request, jsonify
from dotenv import load_dotenv

load_dotenv()

DEFAULT_RADIO_VALUE = os.getenv('DEFAULT_RADIO_VALUE','2')
#'1' -> disabled; '2' -> turn off only; '3' -> enabled

class State:
    def __init__(self):
        self._radio_value = DEFAULT_RADIO_VALUE

    def get_radio_value(self):
        return self._radio_value

    def set_radio_value(self, value):
        self._radio_value = value
        return True

app = Flask(__name__)
state = State()

@app.route('/')
def index():
    return redirect(url_for('qbit_speed_toggle'))
    return render_template('index.html')

@app.route('/qbit', methods=('GET', 'POST'))
def qbit_speed():
    if request.method == 'POST':
        radio = request.form['radio']

        # change radio button value
        updated = state.set_radio_value(radio)
        if updated:
            return jsonify(type='success', message='Update successful')
        else:
            return jsonify(type='danger', message='Unable to change value')

    if request.method == 'GET':
        return jsonify(value=state.get_radio_value())

@app.route('/toggle-qbit')
def qbit_speed_toggle():
    # read radio button value
    radio = state.get_radio_value()
    return render_template('qbit_speed_toggle.html', radio=radio)

