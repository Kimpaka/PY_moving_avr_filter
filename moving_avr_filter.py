import csv
# import chart_studio.plotly as py
import chart_studio
# from chart_studio.plotly import plot
import pandas as pd

from plotly.graph_objs import Scatter
from plotly.offline import plot

# Read CSV File
cvs_path = 'C:/Users/USER/Desktop/temp_data.csv'

with open(cvs_path, 'r') as f:
  reader = csv.reader(f, delimiter=',')
  ds = [ row for row in reader ]

# Write Graph
ds = ds[1:]

# front delta
ad_filter_time = []
ad_filter_data = []

filter_k: int = 95
filter_k_comp: int = 5

pre_data: int = int(ds[1][1])

idx = 1

for i in range(len(ds)):
    temp_data1 = pre_data * filter_k
    temp_data2 = int(ds[i][1]) * filter_k_comp
    temp_data = temp_data1 + temp_data2
    temp_data = temp_data / 100
    pre_data = temp_data
    filtered_data = pre_data
    ad_filter_time.append(idx)
    ad_filter_data.append(filtered_data)

    idx = idx + 1

plot(
    [Scatter(y=ad_filter_data, x=ad_filter_time, mode='lines', name='PCB NTC')]
)

df = pd.DataFrame(ad_filter_data, columns = ['ad_filter'])
df.to_csv("filter_data.csv", index = False)


