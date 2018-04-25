#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    dv.add_field('turnover', dv)
    
    TVMA20= dv.add_formula("TVMA20_j","Ts_Mean(turnover,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return TVMA20