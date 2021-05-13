from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)
app.secret_key = "OSU"

# Converts temp to string
def get_temp(crnt_temp):
    if crnt_temp >= 95:
        temp_text = "Stay inside or use A/C!!!"
    elif 80 <= crnt_temp < 95:
        temp_text = "It's hot outside!"
    elif 70 <= crnt_temp < 80:
        temp_text = "It's a nice warm day."
    elif 60 <= crnt_temp < 70:
        temp_text = "It's a nice cool day."
    elif 57 <= crnt_temp < 60:
        temp_text = "It's mildly cold outside, get a jacket."
    elif 40 <= crnt_temp < 57:
        temp_text = "It's cold outside, bundle up!"
    else:
        temp_text = "It's extremely cold outside, stay inside!"
    return temp_text

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        city = request.form["location"]
        session["city"] = city
        return redirect(url_for("location"))
    return render_template("home.html")

@app.route("/location")
def location():
    # where micro service will be implemented
    if "city" in session:
        city = session["city"]
        # example data
        crnt_temp = 86
        # Converter
        temp_text = get_temp(crnt_temp)
        return render_template("location.html", location=city,temp=temp_text)
    else:
        return render_template("home.html")

@app.route("/future")
def future():
    # where micro service will be implemented
    if "city" in session:
        city = session["city"]
        # example data
        crnt_temp = 76
        # Converter
        temp_text = get_temp(crnt_temp)
        return render_template("future.html", location=city, temp=temp_text)
    else:
        return render_template("home.html")

@app.route("/tomorrow")
def tomorrow():
    # where micro service will be implemented
    if "city" in session:
        city = session["city"]
        # example data
        crnt_temp = 101
        # Converter
        temp_text = get_temp(crnt_temp)
        return render_template("tomorrow.html", location=city, temp=temp_text)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

