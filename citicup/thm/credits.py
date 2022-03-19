import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler

#import numpy.random.rand as rand
# np.transpose(A)

## 1 数据初始化(这部分是函数除了样本数据以外要传进来的参数)
n=4;    # 指标个数
m=6;  # 样本个数

# 随机建立样本,每一列分别是光盘次数, 公交次数, 家庭用电, 步数
# 直接把用户数据里面的评价指标项传进来就行
#X=np.array([60*np.random.rand(m,1), 80*np.random.rand(m,1), 1000*np.random.rand(m,1),10000*np.random.rand(m,1)])
X = np.array([48,22,957,7922,54,43,485,9594,7,76,800,6557,54,77,141,357,37,12,421,8491,5,77,915,9339])
X = X.reshape(m,n)
k1=-1;    # 需要正向化的列号
k2=[0,1];   # 需要进行模糊处理的列号

# 下面两个是隶属函数的参数, 测试阶段懒得调的话, 就直接固定0和0.3
alpha=0;    # α,后期可以人为调整
sigma=0.3;  # σ,后期可以人为调整

## 2 数据预处理n
# 2.1 构造指标矩阵
# 传进来的矩阵X就是

# 2.2 数据正向化
if k1 != -1:   # -1表明这个指标不需要这么操作
   X[:,k1]=max(X[:,k1])-X[:,k1]+min(X[:,k1]);

# 2.3 数据标准化
#XX = StandardScaler().fit_transform(X)
XX = X / np.sqrt(sum(np.power(X,2)))

## 3 模糊集合处理
if k2 != -1:   # -1表明这个指标不需要这么操作
    temp=XX[:,k2];
    temp=temp*(temp>=alpha);   # 把小于alpha的部分清零
    f=1-np.exp(-np.power(temp-alpha,2)/(2*sigma**2));   # 把需要处理的列代入隶属度函数
    XX[:,k2]=f; # 修改后更新XX数组

## 4 逆熵权法赋权值
# 4.1 计算概率矩阵C
C=XX/sum(XX);

# 4.2 计算熵H
H=-( sum( (C*np.log(C+0.0000001)) ) )/np.log(m);

# 4.3 计算逆熵权W
W=H/sum(H);

## 5 优劣解距离法计算综合评分
# 5.1 计算加权规范化决策矩阵R
R=XX*W;
# 5.2 计算各个样本到正负理想解的距离D+,D-
Rp=np.max(R,axis=0);  #r+
Rn=np.min(R,axis=0);  #r-
Dp=np.transpose( np.sqrt( sum ( np.transpose(np.power(Rp-R,2) ) ) ) ); # d+, 这里sum里面要转置一下
Dn=np.transpose( np.sqrt( sum ( np.transpose(np.power(Rn-R,2) ) ) ) ); # d-, 这里sum里面要转置一下
# 5.3 计算初步得分E'
EE=Dn/(Dp+Dn);
# 5.4 归一化
# 这为了直观直接放到0~100
E = ((EE - np.mean(EE)) / (np.max(EE)-np.min(EE))+1)*50
print(E)