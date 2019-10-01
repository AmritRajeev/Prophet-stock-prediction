import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import prophet


df = pd.read_csv('dataset.csv')
df =df[['Date','High']].dropna()
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
week_df = df.resample('W').mean()
w_df = week_df.reset_index().dropna()
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
week_df = df.resample('W').mean()
d_df = daily_df.reset_index().dropna()
d_df.columns = ['date', 'High']
m = Prophet()
m.fit(d_df)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
forecast[['date', 'Open', 'High', 'Low','Close']].tail()
fig1 = m.plot(forecast)
