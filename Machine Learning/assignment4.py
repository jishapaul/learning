import pandas as pd
import matplotlib.pyplot as plt
import mplleaflet
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib import dates as mdates

# Data from https://data.worldbank.org/country/india?view=chart 

df_india = pd.read_csv('india.csv',skiprows=4)
df_china = pd.read_csv('China.csv',skiprows=4)
df_south_africa = pd.read_csv('SouthAfrica.csv',skiprows=4)
df_usa = pd.read_csv('USA.csv',skiprows=4)

df = df_india[df_india['Indicator Name']=='Population density (people per sq. km of land area)']
df_temp = df_china[df_china['Indicator Name']=='Population density (people per sq. km of land area)']
df = df.append(df_temp)
df_temp = df_south_africa[df_south_africa['Indicator Name']=='Population density (people per sq. km of land area)']
df = df.append(df_temp)
df_temp = df_usa[df_usa['Indicator Name']=='Population density (people per sq. km of land area)']
df = df.append(df_temp)
df = df.reset_index()
df

#print (df)
data1 = (list(df.loc[0])[5:])
data2 = (list(df.loc[1])[5:])
data3 = (list(df.loc[2])[5:])
data4 = (list(df.loc[3])[5:])

plt.title("Population density", fontsize=20)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


x_now = list(range(0,62))
years = list(range(1961,2017))
years_str =  ["%.4i" % number for number in years]

plt.plot(data1, '-',label='India', color='orange')
plt.plot(data2, '-',label='China', color='red')
plt.plot(data3, '-',label='South Africa', color='green')
plt.plot(data4, '-',label='USA', color='blue')
plt.legend(['India', 'China','South Africa', 'USA'],loc='upper left')


plt.gca().set(xticks=x_now, xticklabels=years_str)
plt.xticks(rotation='vertical', fontsize=18)

fig_size = plt.rcParams["figure.figsize"]
print (fig_size)
fig_size[0] = 45
fig_size[1] = 30
plt.rcParams["figure.figsize"] = fig_size
plt.xlabel('Year',fontsize=30)
plt.ylabel('Density per sqkm',fontsize=30)
fig = plt.gcf()

params = {'axes.labelsize': 12,'axes.titlesize':20, 'text.fontsize': 20, 'legend.fontsize': 20, 'xtick.labelsize': 28, 'ytick.labelsize': 20}
plt.rcParams.update(params)

fig = plt.gcf()
fig.savefig('asignment4.png',dpi=100,bbox_inches='tight')
plt.show()