from flask import Flask, render_template, request, jsonify
import yagmail
import RPi.GPIO as GPIO


app = Flask(__name__)


#GPIO setup
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


#Initial LED state
led_state = False
GPIO.output(LED_PIN, GPIO.LOW)



@app.route('/')
def dashboard():
    GPIO.output(LED_PIN, GPIO.LOW)
    return render_template('index.html')


## TODO: implement the logic for the led turning on
@app.route('/toggle-led', methods=['POST'])
def toggle_led():
    #get current LED status
    global led_state
    
    data = request.get_json()
    #parse json data
    switch_state = data['state'] #Get the state value
    
    if switch_state:
        GPIO.output(LED_PIN, GPIO.HIGH) #Turn on LED if switch state is true
        led_state = True #Update led_state to follow that LED is now on
    else:
        GPIO.output(LED_PIN, GPIO.LOW) #Turn off LED if switch state is false
        led_state = False #Update led_state to follow that LED is now off
        
    return jsonify({'success': True, 'led_state': led_state}) # keep this line to indicate that the script passed and the led is turned on or off successfully, otherwise return False and include the current LED state in the response

def send_email(current_temp):
    sender_email = "iotdashboard2024@gmail.com"
    receiver_email = "iotdashboard2024@gmail.com"
    password = "dyqv qvrd yjzt eusa"
    yag = yagmail.SMTP(user=sender_email, password=password)

    subject = "Temperature Alert"
    body = f"The current temperature is {current_temp}. Would you like to turn on the fan?"
    yag.send(to=receiver_email, subject=subject, contents=body)
    print("Sent!")
        
if __name__ == "__main__":
    app.run()

