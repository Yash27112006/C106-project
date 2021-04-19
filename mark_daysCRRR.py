import csv
import plotly.express as px
import numpy as np

with open('marks_daysPresent.csv') as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Days Present", y="Marks")
    fig.show() 

def getDataSource(data_path):
    marks = []
    daysPresent = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks"]))
            daysPresent.append(float(row["Days Present"]))
    
    return {"x":daysPresent,"y":marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(" ")
    print("Correlation between marks and days present: ", correlation[0,1])
    print(" ")

def setup():
    data_path = "marks_daysPresent.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)


setup()