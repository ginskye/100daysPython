import numpy
import pandas
#output csv with furcolor, count
data = pandas.read_csv("SquirrelData.csv")
furs = (data["Primary Fur Color"]).unique() # this includes nan, so we need to remove
a = numpy.delete(furs, 0) #numpy array is immutable, so create copy without first element
gray_nums = len(data[data["Primary Fur Color"]=="Gray"])#pulls full rows into a list, can call len
red_nums = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_nums = len(data[data["Primary Fur Color"]=="Black"])
dict = {
    "Fur Color": a,
    "Count": [gray_nums, red_nums, black_nums]
}
frame = pandas.DataFrame(dict)
print(frame)
frame.to_csv("squirrel_count.csv")
