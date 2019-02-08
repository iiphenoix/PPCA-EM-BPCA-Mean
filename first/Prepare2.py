import pandas as pd
def Tonull(name1,name2,n):
    project = pd.read_csv(name1,encoding = 'gbk')
    pro = project.values
    for i in range(pro.shape[0]):
        col = list(pro[i])
        for j in range(0,pro.shape[1]):
            if(('None' == col[j]) or ('#NULL!' == col[j])):
                project.iloc[i,j]=''
    ind = []
    for i in range(n):
        ind.append(i)

    project['index'] = ind
    project.to_csv(name2, sep=',', header=True,index = False,encoding='gbk',)
Tonull('E:\\kunmingdata2.csv','E:\\tonullpro2.csv',4845)

