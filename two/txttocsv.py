def filetocsv(name1,name2,x1,x2,x3,x4,x5,x6,x7):
    import re
    a = []
    f=open(name1,"r",encoding='utf-8')
    f.readline()
    for line in f:
        l = re.split('[^云^A-Z^0-9.-]+',line.strip())
        a.append(l)
    data = list(map(list,zip(*a)))
    from pandas import Series,DataFrame
    import pandas as pd
    datt={
        x1:data[1],
        x2:data[2],
        x3:data[3],
        x4:data[4],
        x5:data[5],
        x6:data[6],
        x7:data[7]
    }
    df = DataFrame(datt)
    df.to_csv(name2, sep=',', header=True,index = False,encoding='gbk')

filetocsv('E:AT0027.txt','D:trafficflow.csv','车牌号','时间','经度','维度','运行状态','速度','方向')