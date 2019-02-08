from ycimpute.imputer.mice import MICE
import pandas as pd
from first import em
def Mice(name,feature):
    data = pd.read_csv(name, encoding='gbk')
    datafeature = data[feature].values
    mice = MICE()
    competefeature =  mice.complete(datafeature)
    return competefeature

competefeature = Mice('E:\\feature.csv',['Longitude','Latitude','TYPEID',
                                         'ADDRESS','TELEPHONE','ChkNum','ChkUserNum'])
data = em.StartNumToText(competefeature)
data.to_csv('E:\\micefill.csv', sep=',', header=True,index = False,encoding='gbk')

