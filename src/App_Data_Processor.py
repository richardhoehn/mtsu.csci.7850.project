import numpy as np
import pandas as pd


class Data_Processor():
    def __init__(self, seq_length=90):
        self.seq_length = seq_length
        self.df_raw = pd.DataFrame()
        self.df_sales = pd.DataFrame()
        self.df_sales_raw = pd.DataFrame()
        self.df_sales_avg = pd.DataFrame()
        return

    def load_data(self, url, date_fmt):
        self.df_raw = pd.read_csv(url, parse_dates=["date"])
        
        # Format Date Column to DateTime
        self.df_raw['date'] = pd.to_datetime(self.df_raw['date'], format=date_fmt)

        # Process Data
        self.df_sales = self.df_raw.groupby(['date'])['sales'].sum().reset_index()
        self.df_sales_raw = self.df_sales.copy()
        self.df_sales_avg = self.df_sales.copy()
        self.df_sales_avg['sales'] = self.df_sales_avg['sales'].rolling(window=7, min_periods=1).mean()

    @property
    def sales_raw(self): 
         return self.df_sales_raw['sales'].values.reshape(-1, 1)
    
    @property
    def sales_avg(self): 
         return self.df_sales_avg['sales'].values.reshape(-1, 1)

    def create_sequences(self, data):
        xs, ys = [], []
        for i in range(len(data) - self.seq_length- 1):
            x = data[i:(i + self.seq_length)]
            y = data[i + self.seq_length]
            xs.append(x)
            ys.append(y)
        return np.array(xs), np.array(ys)