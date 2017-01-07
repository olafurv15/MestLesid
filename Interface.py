import os
from bs4 import BeautifulSoup
import urllib.request
from flask import Flask, render_template, Markup


app = Flask(__name__)
app.secret_key = os.urandom(24)

def fotboltinet():
    with urllib.request.urlopen('http://www.fotbolti.net/') as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all(id="hot-news")

    for i in test:
        t = Markup(i)

    soup2 = BeautifulSoup(t, 'html.parser')

    for a in soup2.findAll('a'):
        link = a['href']
        a['href'] = 'http://www.fotbolti.net' + link

    return Markup(soup2)

def visir():
    with urllib.request.urlopen('http://www.visir.is/') as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('div', class_="top-most-wrapper")

    for i in test:
        t = Markup(i)

    soup2 = BeautifulSoup(t, 'html.parser')

    for a in soup2.findAll('a'):
        link = a['href']
        a['href'] = 'http://www.visir.is' + link

    return Markup(soup2)



# Front page.
@app.route("/")
def index():
    fotbolti = fotboltinet()
    v = visir()

    return render_template('index.html', fotboltinet = fotbolti, visir = v)

if __name__ == "__main__":
    app.run()