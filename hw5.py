import pandas as pd
from pandas.plotting import autocorrelation_plot, lag_plot
import matplotlib.pylab as plt
from statsmodels.tsa.stattools import adfuller
#First, we've focused on the data for Brazil. While transferring "sudeste.csv" to pandas, we've used usecols to limit the data for the columns we need.
dfbrazil = pd.read_csv("sudeste.csv", delimiter=",", usecols= ['temp','date'])
#Then we've converted the objects into datetime format. This method helped us to sort the dates in order for them to match with the ones in the data for Madrid.
dfbrazil['date'] = pd.to_datetime(dfbrazil['date'])

#Examining the .csv files, we've found out that the dates between the year 2000 and 2016 are matching. ts is the limiter that we've used to slice the data from the point we needed.
#We've used groupby to reorder the data by 'date'. Then we've found the means of each group and rounded them into zero decimals.
ts= pd.to_datetime('2016-01-01')
g= (dfbrazil.loc[(dfbrazil['date']) < ts]).groupby(['date'])
mean= g.mean()
rounded= mean.round(0)


#Data for Madrid  was already in means form, containing data for the years between 1997 and 2015. To exclude the data between years 1997 and 2000, we've used skiprows.
#In this dataset, name of the date column was CET. We've changed it to date to be able to apply merge in the following step.
dfmadrid = pd.read_csv("weather_madrid_LEMD_1997_2015.csv", delimiter=",", skiprows=[i for i in range(1,1169)], usecols= ['Mean TemperatureC','CET'])
dfmadrid['CET'] = pd.to_datetime(dfmadrid['CET'])
dfmadrid.columns = ['date','Mean TemperatureC']

#As the previous dataframes were in datetime format, we've been able to use pd.merge to get them together in one last dataframe called dffinal. After adjusting the column names, the job was done. 
dffinal=pd.merge(rounded,dfmadrid,on="date")
dffinal.columns=['Date','Brazil Temperature','Madrid Temperature']


plt.plot(dffinal)
plt.show()

#We've managed to acquire a result with a ValueError. Unfortunately, could not solve the problem and continue the code.
