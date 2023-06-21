
import csv
import math

with open("weather_data.csv") as data:
    #data_list = data.readlines()
    #print(data_list)
    data_list = csv.reader(data)
    print(data_list)
    temperatures = []
    for row in data_list:
        print(row)
        if row[1] !="temp":
            tem = int(row[1])
            temperatures.append(tem)
    print(temperatures)

    import pandas
    print(pandas.read_csv("weather_data.csv"))
    datapand = pandas.read_csv("weather_data.csv")
    datadict = datapand.to_dict()
    temps_list = datapand["temp"].to_list()

    avg = len(temps_list)
    addtemps = 0
    for number in temps_list: #sum(list)
        addtemps +=number
    average = math.floor(addtemps/avg)
    print(average)
    highest = datapand["temp"].max()
    print(highest)