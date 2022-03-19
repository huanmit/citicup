import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from django.db import connection
import datetime

def evaluate():
    ##1.数据初始化，确定一些参数
    n=4
    print('\n\n\n\n\n\n\n',"开始评估")
    cursor = connection.cursor()
    cursor.execute("select count(*) from user")
    m = cursor.fetchone()[0]
    k1=-1;    # 需要正向化的列号
    k2=[0,1];   # 需要进行模糊处理的列号
    # 下面两个是隶属函数的参数, 测试阶段懒得调的话, 就直接固定0和0.3
    alpha=0;    # α,后期可以人为调整
    sigma=0.3;  # σ,后期可以人为调整

    today = str(datetime.date.today())

    cursor.execute("select id from user")
    res = cursor.fetchall()
    users = []
    for user in res:
        users.append(user[0])

    ## 2 数据预处理n
    # 2.1 构造指标矩阵
    X = np.array([])
    for user in users:
        cursor.execute("select plogtypeid,carboncurrency from footprint where userid=%s and DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= %s",[user,today])
        res = cursor.fetchall()
        l1 = 0
        l2 = 0
        l3 = 0
        l4 = 0
        for each in res:
            if each[0] == 3:
                l1 += each[1]
            elif each[0] == 4:
                l2 += each[1]
            elif each[0] == 2:
                l3 += each[1]
            elif each[0] == 1:
                l4 += each[1]
        X = np.concatenate((X, [l1,l2,l3,l4]))
    # 建立样本,每一列分别是不用一次性餐具, 公交次数, 骑行, 步数
    X = X.reshape(m,n)

    # 2.2 数据正向化
    if k1 != -1:   # -1表明这个指标不需要这么操作
        X[:,k1]=max(X[:,k1])-X[:,k1]+min(X[:,k1]);
    # 2.3 数据标准化
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

    ### ranking
    step = list(np.argsort(X[:,3]))
    ride = list(np.argsort(X[:,2]))
    chop = list(np.argsort(X[:,0]))
    bus = list(np.argsort(X[:,1]))
    rank = list(np.argsort(E))
    print(rank)

    ### insert into the table
    for i in range(m):
        print("mmm ",i)
        c = round((chop.index(i)+1) / m,4)
        b = round((bus.index(i)+1) / m,4)
        r = round((ride.index(i)+1) / m,4)
        s = round((step.index(i)+1) / m,4)
        rk = round((rank.index(i)+1) / m,4)
        #print(users[i])
        cursor.execute("insert into carboncredits values(%s,%s,%s,%s,%s,%s,%s,%s)",[users[i],today,round(E[i]),s,r,c,b,rk])
        cursor.execute("update user set carboncredit=%s where id=%s",[round(E[i]),users[i]])
        print([users[i],today,E[i],s,r,c,b,0])



'''
#import numpy.random.rand as rand
# np.transpose(A)

## 1 数据初始化(这部分是函数除了样本数据以外要传进来的参数)
n=4;    # 指标个数
m=6;  # 样本个数

# 随机建立样本,每一列分别是不用一次性餐具, 公交次数, 骑行, 步数
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
'''
