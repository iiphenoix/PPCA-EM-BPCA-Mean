import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error #均方误差
from sklearn.feature_selection import SelectKBest
import matplotlib
import hashlib
import pandas as pd

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]

#（完整数据集的地址，测试集取NaN和训练集的数据集地址）
def Csvopreation(name1,name2):
    trafficflowtwo = pd.read_csv(name1, encoding='gbk')
    trafficflowtwo1=trafficflowtwo[['经度','纬度','运行状态','速度','时间间隔']]   #完整的数据
    data_with_id = trafficflowtwo.reset_index()  # 加上行索引
    train_set, test_set = split_train_test_by_id(data_with_id, 0.2, "index")
    #此测试集无论如何运行每次都一样的测试集
    ind = test_set['速度'].index
    test_set['速度']=''
    test_set.to_csv(name2, sep=',', header=True,index = False,encoding='gbk',)
    #将测试集和训练集都写入表格，目的，''里的字符会自动转成NaN
    train_set.to_csv(name2, sep=',', header=False,index = False,encoding='gbk',mode='a')
    trafficflow21 = pd.read_csv(name2, encoding='gbk')
    #排序的目的是排除顺序的因素对实验的干扰
    trafficflow21 = trafficflow21.sort_values(by = 'index')
    trafficflow21 = trafficflow21.reset_index(drop = True)
    trafficflow21.to_csv(name2, sep=',', header=True,index = False,encoding='gbk',)
    trafficflow21 = trafficflow21[['经度', '纬度', '运行状态', '速度', '时间间隔']]
    #返回测试和训练的数据集，完整的数据集，测试集的索引
    return trafficflow21,trafficflowtwo1,ind

def Standardize(X,means,stds):

    #means = np.nanmean(X, axis=0)
    #stds = np.nanstd(X, axis=0)
    return (X - means) / stds

#训练好的数值
def Restandardize(X2 ,means,stds):
    #if(X == None and means == None and stds == None):
    #means = np.nanmean(X, axis=0)
    #stds = np.nanstd(X, axis=0)
    return X2 * stds + means

#x数据集，真实值数据集，ppca的模型值数据集，bpca的模型值数据集，
# EM的模型值数据集,是否标准化的，是否要画真实值的
def Plotfigure(x, real, model, model2, model3,t,t2):
    # 解决可视化不能显示中文和符号问题:
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure()
    plt.rcParams['figure.dpi'] = 180  # 分辨率

    if (t2==1):
        plt.plot(x,real,label='真实值', color='#4169E1')
    plt.plot(x,model,label='ppca模型值',color= '#FF1493')
    plt.plot(x,model2,label='bpca模型值',color= '#006400')
    plt.plot(x,model3,label='E M模型值', color='#00FFFF')
    if(t==1):
        name = '标准化后的'
    else:
        name = ''
    plt.xlabel(name+'时间间隔')
    plt.ylabel(name+'速度')
    plt.legend(loc='best')
    plt.show()


def RESE(real,mode1,model2,model3):
    rmse = []

    rmsevalue = np.sqrt(mean_squared_error(real,mode1))#RMSE
    print('ppca的RMSE：',rmsevalue)
    rmsevalue2 = np.sqrt(mean_squared_error(real,model2))#RMSE
    print('bpca的RMSE：',rmsevalue2)
    rmsevalue3 = np.sqrt(mean_squared_error(real,model3))#RMSE
    print('EM的RMSE：',rmsevalue3)
    rmse = [rmsevalue,rmsevalue2,rmsevalue3]
    return rmse

def autolabel(rects):
    for rect in rects:
        height = rect.get_width()
        plt.text(rect.get_x()+rect.get_height()/2.-0.2, 1.03*height, '%s' % float(height))

def draw_bar(num_list,start,end):
    # -*- coding: utf-8 -*-
    import numpy as np
    import matplotlib.pyplot as plt
    #fig, ax = plt.subplots()
    plt.xlim((start,end ))
    name_list = ['ppca','bpca','em']
    #plt.bar(name_list,num_list)
    b = plt.barh(range(len(num_list)), num_list,  tick_label=name_list)
    for rect in b:
        w = rect.get_width()
        plt.text(w, rect.get_y() + rect.get_height() / 2, '%.6f' %w, ha='left', va='center')

    plt.xlabel("RMSE值")
    plt.ylabel("算法类型")
    plt.show()




