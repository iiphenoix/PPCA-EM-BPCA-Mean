from ycimpute.imputer import EM
from first import toencoding
import pandas as pd
import numpy as np
def Em(name1,feature,n1,n2):
    data = pd.read_csv('E:\\feature.csv', encoding='gbk')
    datafeature = data[feature]
    data2values = datafeature[feature].values
    emval = EM()
    datacompete = emval.solve(data2values)
    return datacompete

#地址为文字的dataframe，列名称，此列位于特征值的第n-1列，
# 索引（编号），映射值，所有完整的特征值
def NumbertoText(data,colname,n,ind,cat,datacompete):
    colvalue = np.rint(np.transpose(datacompete)[n])
    ind= list(ind)
    cat = list(cat)
    text = []
    for i in range(len(colvalue)):
        if(colvalue[i]>max(cat)):
            colvalue[i] = max(cat)
        if(colvalue[i]<min(cat)):
            colvalue[i] = min(cat)
        findid = cat.index(colvalue[i])
        text.append(data[colname][ind[findid]])
    return text

def StartNumToText(datacompete):
    ind, cat1, ind2, cat2 = toencoding.Toencoding\
        ('E:\\tonullpro2.csv', 'ADDRESS', 3108, 'TELEPHONE', 1720, 'index')
    data = pd.read_csv('E:\\tonullpro2.csv', encoding='gbk')
    addrtext = NumbertoText(data,'ADDRESS',3,ind,cat1,datacompete)
    teltext = NumbertoText(data,'TELEPHONE',4,ind2,cat2,datacompete)
    data['ADDRESS'] = addrtext
    data['TELEPHONE'] = teltext

    return data
datacompete = Em('E:\\tonullpro2.csv',['Longitude','Latitude','TYPEID','ADDRESS',
                                       'TELEPHONE','ChkNum','ChkUserNum'],3108,1720)
data = StartNumToText(datacompete)
data.to_csv('E:\\emfill.csv', sep=',', header=True,index = False,encoding='gbk')

