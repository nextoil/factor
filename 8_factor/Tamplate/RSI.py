#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':12}
    if not param:
        param = defult_param
        
    t = param['t']
    
    RSI = dv.add_formula("RSI_J","Ta('RSI',0,close,close,close,close,close,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return RSI  
