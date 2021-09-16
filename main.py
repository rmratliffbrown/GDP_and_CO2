import pandas as pd

GDP = pd.read_csv(“https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv”)

new_GDP=GDP[[“GDP per capita (constant 2010 US$)“, “Mortality rate, infant (per 1,000 live births)“, “Country Name”]]

new_GDP.plot(x=“Mortality rate, infant (per 1,000 live births)“,y=“GDP per capita (constant 2010 US$)“)

