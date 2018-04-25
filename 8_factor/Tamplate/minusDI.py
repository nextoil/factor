#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':14}
    if not param:
        param = defult_param
        
    t = param['t']
    
    minusDI= dv.add_formula("minusDI_J","Ta('MINUS_DI',0,high,low,close,volume,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return minusDI       
