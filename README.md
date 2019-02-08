1.实验（first模块）

①删除特殊字符：代码在first包里的Prepare.py。

②EM算法插值：代码操作如first包里的em.py所示，并且调用了toencoding.py代码

③多重插值：代码操作如first包里mice.py所示，直接调用ycimpute库里的MICE函数，代码操作思路与EM算法操作相似，只需将from ycimpute.imputer import EM 改  from ycimpute.imputer.mice import MICE，调用MICE函数里的插补函数即可。



2.比较EM算法、PPCA算法、BPCA算法的插值误差（two模块）

①bpca插补算法：直接使用Shigeyuki Oba所编写的jar包

②.ppca插补算法：python2可直接导入下载的PPCA插值的代码库，python3导入出错，于是将将ppca包里的函数复制粘贴至two包的ppca.py里，ppcamake.py是调用ppca插值算法里的函数。

③调用ycimpute里的EM模块即可。将测试集的特征值带进EM里的插值函数。返回插值处理后的特征值数据集


具体的过程请访问博客https://blog.csdn.net/qq_31089125/article/details/86776974
