import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("data1.csv")

data = df["temp"].tolist()

# 
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("population mean: ", population_mean)
print("std deviation:  ", std_deviation)

# function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = "MEAN"))
    fig.show()

# code to find mean and standard of hundred data points
# dataset = []
# for i in range(0,100):
#     random_index = random.randint(0,len(data))
#     value = data[random_index]
#     dataset.append(value)
#  mean = statistics.mean(dataset)
# std_deviation = statistics.stdev(dataset)    

#  print("mean of sample: ",mean)
# print("std deviation of sample: ",std_deviation)

# function to get the mean of the given data samples
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
mean = statistics.mean(dataset)
return mean

# function to get mean of 100 data p[oints 1000 times and plot the graph
def setup():
    mean_list = []
    for i in range (0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)   

setup()     

# function to get std_deviation of 100 data p[oints 1000 times and plot the graph
def standard_deviation():
    mean_list = []
    for i in range (0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("std_deviation of sampling distribution: ", std_deviation)

std_deviation()