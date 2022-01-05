from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/')
def index():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city='Gwalior'

    weather_json=requests.get(url.format(city)).json()

    weather_data=[]

    temp_c=5/9*(weather_json['main']['temp']-32)
    temp_c=int(temp_c)

    weather={
        'city':city,
        'temperature':temp_c,
        'description':weather_json['weather'][0]['description'],
        'icon':weather_json['weather'][0]['icon']
    }
    weather_data.append(weather)
    print(weather_json)
    return render_template("index.html",weather_data=weather_data)

@app.route('/temp',methods=['POST'])
def temp():
    t1=request.form['city_name']
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city=t1

    weather_json=requests.get(url.format(city)).json()

    weather_data=[]

    temp_c=5/9*(weather_json['main']['temp']-32)
    temp_c=int(temp_c)

    weather={
        'city':city,
        'temperature':temp_c,
        'description':weather_json['weather'][0]['description'],
        'icon':weather_json['weather'][0]['icon']
    }
    weather_data.append(weather)
    print(weather_json)
    return render_template("index.html",weather_data=weather_data)


if __name__=="__main__":
    app.run(debug=True)