# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = "黄斐" # 这里填下你的名字
default_params = {"t1":6}# 这里填写因子参数默认值，比如: {"t1": 10}
params_description = {} # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    alpha21=REGBETA(MEAN(CLOSE,6),SEQUENCE(6))alpha21=REGBETA(MEAN(CLOSE,6),SEQUENCE(6)) 
    """
    dv.add_formula('Mean','Ts_Mean(close_adj,%s)'%(t1),is_quarterly = False, add_data = True)
    value = dv.add_formula('alpha21',
            "Ta('LINEARREG_SLOPE',0,Mean,Mean,Mean,Mean,Mean,%s)"(t1),
        is_quarterly=False, add_data=True)
    return value
