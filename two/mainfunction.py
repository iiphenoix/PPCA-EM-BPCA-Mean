from two import ppcamake, emmake, bpcamake, share
import numpy as np
import pandas as pd
if(__name__ == '__main__'):
    realReStd, modelppca, ind ,means ,stds = ppcamake.Ppcamake('D:\\trafficflowtwo.csv', 'D:\\trafficflow21.csv')
    modelem = emmake.EMmake('D:\\trafficflowtwo.csv', 'D:\\trafficflow21.csv')
    modelbpca = bpcamake.Bpcamake('D:\\trafficflow232.csv')
    realStd = share.Standardize(realReStd, means, stds)

    modelppcaReStd = share.Restandardize(modelppca, means, stds)
    modelemReStd = share.Restandardize(modelem, means, stds)
    modelbpcaReStd = share.Restandardize(modelbpca, means, stds)
    modelppcaReStddataframe = pd.DataFrame(modelppcaReStd)
    modelppcaReStddataframe.to_csv('D:\\ppcafill.csv', sep=',', header=True, index=False, encoding='gbk', )
    modelemReStddataframe = pd.DataFrame(modelemReStd)
    modelemReStddataframe.to_csv('D:\\emfill.csv', sep=',', header=True, index=False, encoding='gbk', )
    modelbpcaReStddataframe = pd.DataFrame(modelbpcaReStd)
    modelbpcaReStddataframe.to_csv('D:\\bpcafill.csv', sep=',', header=True, index=False, encoding='gbk', )

    realReStdT = np.transpose(realReStd)
    realStdT = np.transpose(realStd)
    modelppcaT = np.transpose(modelppca)
    modelppcaReStdT = np.transpose(modelppcaReStd)
    modelemT = np.transpose(modelem)
    modelemReStdT = np.transpose(modelemReStd)
    modelbpcaT = np.transpose(modelbpca)
    modelbpcaReStdT = np.transpose(modelbpcaReStd)

    share.Plotfigure(realReStdT[4][ind], realReStdT[3][ind],
                     modelppcaReStdT[3][ind], modelbpcaReStdT[3][ind], modelemReStdT[3][ind], 0,1)
    share.Plotfigure(realReStdT[4][ind], realReStdT[3][ind],
                     modelppcaReStdT[3][ind], modelbpcaReStdT[3][ind], modelemReStdT[3][ind], 0,0)
    print('未标准化数据的RMSE大小如下')
    rmse = share.RESE(realReStdT[3][ind], modelppcaReStdT[3][ind], modelbpcaReStdT[3][ind], modelemReStdT[3][ind])

    share.draw_bar(rmse,21.5,22.1)

    share.Plotfigure(realStdT[4][ind], realStdT[3][ind],
                     modelppcaT[3][ind], modelbpcaT[3][ind], modelemT[3][ind], 1,1)
    share.Plotfigure(realStdT[4][ind], realStdT[3][ind],
                     modelppcaT[3][ind], modelbpcaT[3][ind], modelemT[3][ind], 1,0)
    print('标准化数据的RMSE大小如下')
    rmse2 = share.RESE(realStdT[3][ind],
                       modelppcaT[3][ind], modelbpcaT[3][ind], modelemT[3][ind])

    share.draw_bar(rmse2, 0.9, 1.0)





