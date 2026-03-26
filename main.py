from flask import Flask, render_template

# Skapa en Flask-app
app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)

# Ange vad som händer när man går in på startsidan '/'
@app.route('/')
def home():
    return 'Hello world'

# På adressen /hello/ kan man ange sitt namn som parameter
@app.route("/<namn>")
def hello(namn):
    return "Hej " + namn

# Starta webbappen när man kör python-filen
if __name__ == "__main__":
    app.run(debug=True)