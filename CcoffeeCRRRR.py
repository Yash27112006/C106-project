import csv
import plotly.express as px
import numpy as np

with open('coffee_sleep.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Coffee", y="sleep")
    fig.show()

def getDataSource(data_path):
    sleep = []
    coffee = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            sleep.append(float(row["sleep"]))
            coffee.append(float(row["Coffee"]))
    
    return {"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(" ")
    print("Correlation between coffee and sleep time: ", correlation[0,1])
    print(" ")

def setup():
    data_path = "coffee_sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()