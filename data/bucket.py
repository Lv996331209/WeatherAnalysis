class Bucket():#为桶定义一个集合类
    def __init__(self):#一个集合中有十个桶
        self.data =  [[] for row in range(10)]#初始十个桶定为空
    def capacity(self):#输出桶的容量
        print(len(self.data))
    def show(self):
        for i in range(len(self.data)):
            if len(self.data[i]):
              print(str(i)+'号桶内:'+str(self.data[i]))
            else:
              print(str(i)+'号桶内:[NULL]')

def sort_first(aim):
    a=Bucket
    a.num=0
    a.data= [[] for row in range(10)]
    for i in aim:
        x=i%10
        a.data[x].append(i)
    print("第一次桶排序后:",a.data)
    a.show(a)
    return a.data
def sort_second(b):
    a = Bucket
    a.data = [[] for row in range(10)]
    for i in b:
        for j in i:
            x = int(j / 10)
            a.data[x].append(j)
    print("第二次桶排序后:",a.data)
    a.show(a)
    return a.data
if __name__ == '__main__':
   f=open('num.txt','r',encoding='utf8')
   num=f.readlines()
   for i in range(len(num)):
       num[i]=int(num[i])
   print(num)
   b=sort_first(num)
   c=sort_second(b)

