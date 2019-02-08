from two import share
import numpy as np
import pandas as pd
def Bpcapre(name1,name2,name3):
    trafficflow, a,ind = share.Csvopreation(name1, name2)
    data = trafficflow.values  # 排除ppca训练对data的干扰
    data = share.Standardize(data)
    #bpca算法的jar运行包要求将空值转成999
    np.transpose(data)[3][ind] =999.0
    rea = pd.DataFrame(data)
    rea.to_csv(name3, sep=',', header=False, index = False, encoding='gbk', )
    #print(np.nanmean( rea1,axis=0))

#完整的数据集，测试集和训练集，空值转成999形成的表格
Bpcapre('D:\\trafficflowtwo.csv','D:\\trafficflow21.csv','D:\\trafficflow23.csv')

