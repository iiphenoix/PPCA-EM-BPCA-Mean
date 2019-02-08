import time
import datetime
def getTimeDiff(timeStra,timeStrb):
    if timeStra<=timeStrb:
        return 0
    ta = time.strptime(timeStra, "%Y-%m-%d-%H.%M.%S")
    tb = time.strptime(timeStrb, '%Y-%m-%d-%H.%M.%S')
    y,m,d,H,M,S = ta[0:6]
    dataTimea=datetime.datetime(y,m,d,H,M,S)
    y,m,d,H,M,S = tb[0:6]
    dataTimeb=datetime.datetime(y,m,d,H,M,S)
    secondsDiff=(dataTimea-dataTimeb).seconds
    minutesDiff=round(secondsDiff/60,1)
    secondsDiff=(dataTimea-dataTimeb).total_seconds()
    return secondsDiff

import pandas as pd
trafficflow = pd.read_csv('D:\\trafficflow.csv', encoding='gbk')
a = trafficflow['时间']
diff=[]
for i in range(trafficflow.shape[0]):
    diff.append(getTimeDiff(a[i][:19],a[0][:19]))
trafficflow['时间间隔']=diff
trafficflow.to_csv('D:\\trafficflowtwo.csv', sep=',',
                    header=True,index = False,encoding='gbk')


