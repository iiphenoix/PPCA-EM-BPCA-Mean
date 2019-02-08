from two import share
from two import ppca

def Ppcamake(name1,name2):
    trafficflow21,trafficflowtwo1,ind = share.Csvopreation(name1, name2)
    data = trafficflow21.values  #测试集和训练集
    ppc = ppca.PPCA()
    ppc.fit(data ,3)

    return trafficflowtwo1.values,ppc.data,ind,ppc.means,ppc.stds

