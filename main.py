from flask import Flask

# Skapa en Flask-app
app = Flask(__name__)

# Ange vad som händer när man går in på startsidan '/'
@app.route('/')
def home():
    return 'Hello world'

# Starta webbappen när man kör python-filen
if __name__ == "__main__":
    app.run(debug=True)