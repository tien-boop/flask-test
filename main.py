from flask import Flask, render_template, request
import datetime
#GÖR DATETIME FÖDELSEDAG

# Skapa en Flask-app
app = Flask(__name__)

# Ange vad som händer när man går in på startsidan '/'
@app.route('/')
def home():
    return 'Hello world'

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)

@app.route("/show", methods=["POST"])
def show():
    b_day = request.form["b_day"].split("-")
    this_year = datetime.date.today().year
    today = datetime.date.today()
    this_b_day = datetime.date(this_year, int(b_day[1]), int(b_day[2]))
    if (this_b_day - today).days > 0:
        time_to_birthday = (this_b_day - today).days
    else:
        time_to_birthday = (this_b_day - today).days + 365

    #time_to_birthday = datetime.date.fromisoformat(b_day) - today
    return "Du fyller om " + str(time_to_birthday) + " dagar!"

# På adressen /hello/ kan man ange sitt namn som parameter
@app.route("/<namn>")
def hello(namn):
    return "Hej " + namn

# Starta webbappen när man kör python-filen
if __name__ == "__main__":
    app.run(debug=True)