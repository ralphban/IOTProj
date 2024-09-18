from flask import Flask, render_template, request, jsonify
# import RPi.GPIO as GPIO

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('index.html')

## TODO: implement the logic for the led turning on
@app.route('/toggle-led', methods=['POST'])
def toggle_led():
    ## write logic here
    return jsonify({'success': True}) # keep this line to indicate that the script passed and the led is turned on or off successfully, otherwise return False

if __name__ == "__main__":
    app.run()