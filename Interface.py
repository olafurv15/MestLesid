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
    with urllib.request.urlopen('http://www.visir.is/section/FRETTIR') as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('div', class_="tabContent most fmob")

    for i in test:
        t = Markup(i)

    soup2 = BeautifulSoup(t, 'html.parser')

    for a in soup2.findAll('a'):
        link = a['href']
        a['href'] = 'http://www.visir.is' + link

    return Markup(soup2)

def mbl():
    with urllib.request.urlopen('http://www.mbl.is/frettir/') as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('div', id="popularity-tab-12hours-allt")

    for i in test:
        t = Markup(i)

    soup2 = BeautifulSoup(t, 'html.parser')

    for a in soup2.findAll('a'):
        link = a['href']
        a['href'] = 'http://www.mbl.is' + link

    return Markup(soup2)



# Front page.
@app.route("/")
def index():
    f = fotboltinet()
    v = visir()
    m = mbl()

    return render_template('index.html', fotboltinet = f, visir = v, mbl = m)

if __name__ == "__main__":
    app.run()