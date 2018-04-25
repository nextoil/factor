#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':10}
    if not param:
        param = defult_param
        
    t = param['t']
    
    dv.add_field('turnover_ratio', ds)
    
    VOL10= dv.add_formula("VOL10_j","Ts_Mean(turnover_ratio,%s)"%(t),
           is_quarterly=False,
           add_data=False)
    return VOL10
