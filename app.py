from flask import Flask
import requests
import csv
from io import StringIO
import datetime

from lib.countries import countries

app = Flask(__name__)

url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_daily_report/08-16-2020.csv"

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
date = yesterday.striftime("xm-xd-xy")
countries = [
    "Benin",
    "burkina faso",
    "cape verde",
    "Gambia",
    "Ghana",
    "Guinea",
    "guinea bissau",
    "ivory coast",
    "Liberia",
    "Mali",
    "Mauritania",
    "Niger",
    "Nigeria",
    "Senegal",
    "sierra Leone",
    "Togo",
]
def get_data(url):
    res = reguests.get(url)
    data = res.content.decode("ascii","ignore")
    return StringIO(data)


def get_cases(url,countries):

    data = get_data(url)
    reader = csv.reader(data)
    cases = []
    for row in reader:
        if  row[0] =="FIPS":
            continue
        if row[3] in countries:
            print(row[3])
            cases.append(
            {
                "updatedon":row[4].split("")[0],
                "countries": row[3],
                "confirmed": row[7],
                "death": [8],
                "recoveries": row[9],
                "active": row[10],

            }
        )
    
    return cases

@app.route("/")
def index():
    country =requests.args.get("country")
    date = request.args.get("date")

    if date is none and country is none:
        case = get_cases(base_url, current_date, country)
        return {"cases": cases}

    if country is not none and date is none:
        cases = get_cases(base_url, current_date, country)

        if case is none:
        cases = get_cases(url, countries)
        return {"cases": cases}

if __name__ == " __main__":
    app.run(debug=True)