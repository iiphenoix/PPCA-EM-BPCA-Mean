from scipy import stats

def AccordingMeanInsert(tonullpro2,add,nonullcount):
    tonullpro2 = tonullpro2.sort_values(by=add) #目的：将Adress缺值的沉入底部
    la = stats.mode(tonullpro2[add][:nonullcount]) #adress属性3108个值非空
    fill = tonullpro2[add].fillna(value=list(la.mode)[0])
    tonullpro2[add]=fill
    return tonullpro2

import pandas as pd
tonullpro2 = pd.read_csv('E:tonullpro2.csv', encoding='gbk')
tonullpro2 = AccordingMeanInsert(tonullpro2,'ADDRESS',3108)  #从表格中读出的数据，列的属性，非空的个数
tonullpro2 = AccordingMeanInsert(tonullpro2,'TELEPHONE',1720)  #从表格中读出的数据，列的属性，非空的个数
tonullpro2.to_csv('D:\\finalone.csv', sep=',', header=True,index = False,encoding='gbk')