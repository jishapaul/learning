import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib import dates as mdates

def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))
    #print (df.head())
    #Index(['ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'NAME', 'GSNFLAG',
      # 'HCNFLAG', 'WMOID', 'x', 'y', 'x_group', 'y_group', 'xy_group', 'hash'],
     # dtype='object')


    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df = df.sort('Date')

df_2015 = df[df.Date.str.contains('2015')==True]



df = df[df.Date.str.contains('2015')==False]



df['Date'] = df['Date'].str[5:]

df_max_2015 = df_2015.groupby(['Date'], sort=True)['Data_Value'].max()
df_min_2015 = df_2015.groupby(['Date'], sort=True)['Data_Value'].min()


df_max_2015 = df_max_2015.reset_index()
df_min_2015 = df_min_2015.reset_index()
#print (df_max_2015)

df = df[df.Date.str.contains('02-29')==False]
df_max_2015 = df_max_2015[df_max_2015.Date.str.contains('02-29')==False]
df_min_2015 = df_min_2015[df_min_2015.Date.str.contains('02-29')==False]

df_max = df.groupby(['Date'], sort=True)['Data_Value'].max()
df_min = df.groupby(['Date'], sort=True)['Data_Value'].min()

df_max = df_max.reset_index()
df_min = df_min.reset_index()
 


max_data = np.array(df_max['Data_Value'])
min_data = np.array(df_min['Data_Value'])

print (len(max_data))


#plt.figure()
plt.title('Temperature  Plot')

a = pd.DatetimeIndex(start='2010-01-01',end='2014-01-01' , freq='D')
b = pd.Series(np.random.randn(len(a)), index=a)

#plt.gca().axis([0,366,-400,400])
plt.plot(max_data, '-',label='High', color='orange')
plt.plot(min_data, '-',label='Low',color='lightblue')
plt.gca().fill_between(range(len(max_data)), max_data, min_data, facecolor = 'lightgreen', alpha = 0.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#months = ['Jan','Feb','Mar','Apr']
months = [1,2,3,4,5,6,7,8,9,10]
plt.xticks(months, rotation='vertical')
plt.gca().set(xticks=[15, 45, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349],
              xticklabels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                           'November', 'December'])

df_max_2015 = df_max_2015[df_max_2015['Data_Value'] > df_max['Data_Value']]
df_min_2015 = df_min_2015[df_min_2015['Data_Value'] < df_min['Data_Value']]




plt.scatter(x=list(df_max_2015.index),y=list(df_max_2015['Data_Value']),color='red')
plt.scatter(y=list(df_min_2015['Data_Value']),x=list(df_min_2015.index),color= 'green')

plt.xlabel('Days of the Year (Starting from Jan1)')
plt.ylabel('Temperature in Tenth of Degree Celcius')

plt.legend(['High', 'Low', 'Temperature within record ranges', '2015 record breakers-High','2015 record breakers-Low'],loc='center left', bbox_to_anchor=(1.0, 0.5))
fig = plt.gcf()
fig.savefig('graph.png',dpi=100,bbox_inches='tight')
plt.show()


