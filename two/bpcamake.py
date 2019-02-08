import pandas as pd

def Bpcamake(name):
    data = pd.read_csv(name, encoding='gbk')
    model = data[['经度', '纬度', '运行状态', '速度', '时间间隔']].values
    return model

