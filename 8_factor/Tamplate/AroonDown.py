#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    AroonDown= dv.add_formula("AroonDown_j","(%s-Ts_Argmin(low,%s))/%s*100"%(t,t,t),
           is_quarterly=False,
           add_data=False)
    return AroonDown       
