import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose_time_series(data, date_column, value_column):
    data[date_column] = pd.to_datetime(data[date_column])
    data.set_index(date_column, inplace=True)
    
    decomposition = seasonal_decompose(data[value_column], model='additive')
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    
    return trend, seasonal, residual
