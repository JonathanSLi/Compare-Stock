from typing import DefaultDict
from flask import Flask, request, redirect, render_template
import yfinance as yf
from collections import defaultdict

companiesInfo = defaultdict(list)

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        t = request.form.get('query')
        companies = t.split()
        # print(companies)
        companiesInfo.clear()
        options =  request.form.getlist('check')
        for comp in companies:
            c = yf.Ticker(comp.upper())
            # print('comp ', comp.lower())
            for o in options:
                companiesInfo[comp].append((o, c.info[o]))
        # print(companiesInfo)
        return redirect('/table')
    return render_template('index.html')

@app.route('/table')
def table():
    print('in table')
    cInfo = defaultdict(list)
    option = []
    i = 0
    for comp in companiesInfo:
        for x,y in companiesInfo[comp]:
            if i == 0:
                option.append(x)
            cInfo[comp].append(y)
        i+=1 
    companiesInfo.clear()
    return render_template('tables.html', options = option, companiesInfo = cInfo)
