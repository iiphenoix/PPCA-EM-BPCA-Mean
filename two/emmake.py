from two import share
import numpy as np
from ycimpute.imputer import EM

def EMmake(name1,name2):
    trafficflow, b, ind = share.Csvopreation(name1, name2)
    datavalue = trafficflow.values
    datavalue = share.Standardize(datavalue, np.nanmean(datavalue, axis=0),
                                  np.nanstd(datavalue, axis=0))
    #print(trafficflow.values.dtype)
    em = EM()  # EM算法
    model = em.solve(datavalue)
    return model

