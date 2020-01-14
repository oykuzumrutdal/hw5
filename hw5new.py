import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.api import Holt 
from statsmodels.tsa.stattools import adfuller
import pymannkendall as mk
import os
#We imported the required libraries
filenamemadrid = os.getcwd() + "\\weather_madrid_LEMD_1997_2015.csv"
df_madrid = pd.read_csv(filenamemadrid, usecols = ["CET","Mean TemperatureC"], sep="," ) 
#We make python read the csv files
df_madrid = df_madrid.dropna()
df_madrid = df_madrid.rename(columns={"CET": "date"})

filenamebrazil = os.getcwd() + "\\sudeste.csv"
df_brazil = pd.read_csv(filenamebrazil, usecols = ["date","temp"], sep=",") 
df_brazil = df_brazil.dropna()

df_brazil = df_brazil.groupby(["date"])["temp"].mean()
df_brazil = df_brazil.to_frame()
df_brazil = df_brazil.reset_index(drop=False)
df_brazil = df_brazil.set_index('date')
df_madrid = df_madrid.set_index('date')

plt.show()
trend_brazil = mk.original_test(df_brazil)
print(trend_brazil)
trend_madrid = mk.original_test(df_madrid)
print(trend_madrid)