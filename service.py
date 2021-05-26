from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return "Enter an integer"

class Weather(Resource):
    def get(self, crnt_temp):
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


api.add_resource(Weather, "/<int:crnt_temp>")
api.add_resource(Home, "/")

if __name__ == "__main__":
    app.run()
