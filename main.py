from flask import Flask, render_template, url_for, request, redirect, session
import requests
import json

app = Flask(__name__)
app.secret_key = "OSU"


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        city = request.form["location"]
        month = request.form["month"]
        if len(city) == 0 or len(month) == 0:
            return render_template("home.html")
        month.title()
        session["city"] = city
        session["month"] = month
        return redirect(url_for("location"))
    return render_template("home.html")


@app.route("/location")
def location():
    # where micro service will be implemented
    if "city" in session:
        city = session["city"]
        city_split = city.rsplit(", ")
        sending = {"city": city_split[0], "state": city_split[1]}
        req = requests.post("http://fsar.pythonanywhere.com/weather", json=sending)
        data = req.json()
        print(data)
        month = session["month"]
        temp = data[month]['Ave. high (F)']
        response = requests.get("http://jaaguil2.pythonanywhere.com/" + temp)
        return render_template("location.html", location=city, month=month, temp_act=temp, temp=response.json())
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
