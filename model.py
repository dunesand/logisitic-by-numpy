Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #加载数据
def loadDataSet():
    dataMat=[];labelMat=[]  #特征数据和类别标签
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

>>> def sigmoid(inX):  #sigmoid函数
    return 1.0/(1+exp(-inX))

>>> def gradAscent(dataMatIn,classLabels):  #梯度上升法
    dataMatrix=mat(dataMatIn)
    labelMat=mat(classLabels).transpose()
    m,n=shape(dataMatrix)
    alpha=0.001    #步长
    maxCycles=500  #迭代次数
    weights=ones((n,1))  #初始回归系数
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=(labelMat-h)
        weights=weights+alpha*dataMatrix.transpose()*error
    return weights  #返回回归系数
