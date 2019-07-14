import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
#matplotlib.rcParams['font.sans-serif'] = ['SimHei']
#matplotlib.rcParams['axes.unicode_minus'] = False
def draw_bar(month,ave_low,ave_high):
  label_list = ['2014', '2015', '2016', '2017']
  num_list1 = [20, 30, 15, 35]
  num_list2 = [15, 30, 40, 20]
  num_list1=ave_high
  num_list2=ave_low
  x = range(len(num_list1))
  plt.bar(left=x, height=num_list1, width=0.45, alpha=0.6, color='red', label="Maximum temperature")
  plt.bar(left=x, height=num_list2, width=0.45, alpha=1, color='#4169E1',label="Minimum temperature")

  plt.yticks(np.arange(-7.5, 40, 2.5))
  plt.ylabel("Temperature")
  plt.xticks(x, month)
  plt.xlabel("Month")
  plt.title("Temperature Bar")
  plt.legend()
  plt.show()
def ave(length,list):
    sum=0
    for i in range(length):
        t = list[i]
        list[i] = int(t[:-1])
        sum=sum+list[i]
    average=sum/length
    return average
def get_bar():
  month=[]
  ave_high=[]
  ave_low=[]
  dirpath = 'data/'
  files = os.listdir(dirpath)
  for j in files:
     data = pd.read_csv(dirpath + j , encoding='gbk')
     month.append(data['date'][2][:-3])
     #print(month)
     high=list(data['hTemp'])
     low=list(data['lTemp'])
     length=len(high)
     high=ave(length,high)
     low=ave(length,low)
     ave_high.append(high)
     ave_low.append(low)
  print(month)
  print(ave_low)
  print(ave_high)
  draw_bar(month,ave_low,ave_high)
get_bar()