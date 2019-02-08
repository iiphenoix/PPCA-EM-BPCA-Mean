import pandas as pd
from sklearn.preprocessing import LabelEncoder
#表格的位置，缺失数据的列名，此列非空数据个数，缺失数据的列名2，
# 此列非空数据个数2,插入原数数据的编号
def Toencoding(name,colname,n1,colname2,n2,colname3):
    tonullpro = pd.read_csv(name, encoding='gbk')
    tonullpro2 = tonullpro.sort_values(by=colname)
    tonullpro2 = tonullpro2.reset_index(drop=True)
    encoder = LabelEncoder()
    addr_cat = tonullpro2[:n1][colname]
    addr_cat_encoded = encoder.fit_transform(addr_cat)
    ind = tonullpro2[colname3][:n1]

    tonullpro2[colname][:n1] = addr_cat_encoded
    tonullpro2 = tonullpro2.sort_values(by=colname2)
    tonullpro2 = tonullpro2.reset_index(drop=True)
    encoder2 = LabelEncoder()
    addr_cat2 = tonullpro2[:n2][colname]
    addr_cat_encoded2 = encoder2.fit_transform(addr_cat2)
    ind2 = tonullpro2[colname3][:n2]

    tonullpro2[colname2][:n2] = addr_cat_encoded2
    tonullpro = tonullpro2.sort_values(by=colname3)
    tonullpro = tonullpro.reset_index(drop=True)
    tonullpro.to_csv('E:\\feature.csv', sep=',', header=True, index=False, encoding='gbk')
    return ind,addr_cat_encoded ,ind2,addr_cat_encoded2




