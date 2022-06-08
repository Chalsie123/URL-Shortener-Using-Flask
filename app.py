from flask import *
import pyshorteners

app = Flask(__name__)
api_key = "f82efcc559a1b6e4f0d3c82842903f451aec8bde"
og_url = ""

def checkurl():
    if len(og_url)>32:
        return og_url[:32]

def shorturl():
    inpu_api = pyshorteners.Shortener(api_key=api_key)
    urlshort = inpu_api.bitly.short(og_url)
    return urlshort, inpu_api

def clicks():
    urlshort, inpu_api = shorturl()
    no_of_clicks = inpu_api.bitly.total_clicks(urlshort)
    return no_of_clicks

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route("/result", methods=['GET', 'POST'])
def result():
    global og_url
    # if request.method=="POST":
    #     urlshort = request.form['urlshort']
    #     print(urlshort)
    #     return render_template('click.html', urlshort=urlshort)
    og_url = request.form['original_url']
    urlshort, inpu_api = shorturl()
    og_url=checkurl()
    return render_template('result.html', urlshort=urlshort, og_url=og_url)

@app.route('/click', methods=['GET', 'POST'])
def click():
    no_of_clicks = clicks()
    return render_template('click.html', no_of_clicks=no_of_clicks, og_url=og_url)

# print(urlshort)

if __name__=="__main__":
    app.run(debug=True)