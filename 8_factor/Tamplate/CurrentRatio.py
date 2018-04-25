#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    CurrentRatio = dv.add_formula("CurrentRatio_J","tot_cur_assets/tot_cur_liab",
           is_quarterly=False,
           add_data=False)
    return CurrentRatio       

