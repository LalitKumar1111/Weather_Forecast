from flask import Flask, render_template, request
import requests
import time
import pyttsx3

app = Flask(__name__)

engine = pyttsx3.init()
text = "I am \nAlex,\n Welcome to \n Weather forecast \n enter your city \nand get\n weather of your city\n Thank you"
engine.say(text)
# play the speech
engine.runAndWait()


@app.route('/temperature', methods=['POST'])
def temperature():
    city = request.form['city']

    # city=input("Enter city to know weather")

    r = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_object =requests.get(r).json()
    h = int(json_object["main"]["temp"])
    i=int(json_object["main"]["feels_like"])
    # return h
    cty=city.upper()
    condition = json_object['weather'][0]['main']
    temp_f =int (h - 273.15)
    f_like=int(i - 273.15)
    min_temp = int(json_object['main']['temp_min'] - 273.15)
    max_temp = int(json_object['main']['temp_max'] - 273.15)
    pressure = json_object['main']['pressure']
    humidity = json_object['main']['humidity']
    wind = json_object['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_object['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_object['sys']['sunset'] - 21600))

    # engine.say(["main"])
    # play the speech
    # l=engine.runAndWait()

    return render_template('temprtr.html',c=cty,condi=condition,temp=temp_f,like=f_like,mint=min_temp,maxt=max_temp,pres=pressure,hum=humidity,wnd=wind,snrs=sunrise,snst=sunset)

@app.route('/')
def index():
	return render_template('weathe.html')

if __name__ == '__main__':
    app.run(debug=True)














