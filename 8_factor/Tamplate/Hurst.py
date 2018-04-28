#type3  -  the intermediate variable of the factor is also a factor
import numpy as np
import pandas as pd

def hurst(ts,N):
    lags =range(2, N)
    tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0]*2.0

def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param
        
    t = param['t']
    
    close = dv.get_ts("close_adj").dropna(how='all', axis=1)
    Hurst = pd.DataFrame({sec_symbol: hurst(value.values, t) for sec_symbol, value in close.iteritems()}, index=close.index)
    dv.append_df(Hurst,'Hurst_J')
    
    return Hurst  