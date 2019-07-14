import matplotlib.pyplot as plt
import pandas as pd
import os
def draw_pie(month,list):
    labels = ['优','良','轻度污染','中度污染','重度污染','严重污染']
    X = list
    plt.axis('equal')
    plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.legend()
    plt.show()
def get_pie():
  month='2018-01'
  term=['优','良','轻度污染','中度污染','重度污染','严重污染']
  dirpath = 'data/'
  degree=[]
  degree_count=[]
  files = os.listdir(dirpath)
  for j in files:
     data = pd.read_csv(dirpath + j , encoding='gbk')
     if data['date'][2][:-3]==month:
      #print(month,data['date'][2][:-3])
      degree=list(data['pDegree'])
      break

  for i in term:
     degree_count.append(degree.count(i))
  print(degree_count)
  draw_pie(month,degree_count)
get_pie()

