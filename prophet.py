import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fbprophet import prophet


df = pd.read_csv('dataset.csv')
df =df[['date','High']].dropna()
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
week_df = df.resample('W').mean()
w_df = week_df.reset_index().dropna()
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
week_df = df.open.resample('W').mean()
d_df = daily_df.reset_index().dropna()
d_df.columns = ['date', 'High']
m = Prophet()
m.fit(d_df)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
forecast[['date', 'Open', 'High', 'Low','Close']].tail()
fig1 = m.plot(forecast)
