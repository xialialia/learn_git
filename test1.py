
# sya.argv的用法
# import sys
# a = sys.argv[1:]
# print(a)

# a = 's.b,2b'
# print(a.split('.'))
# print(a.__contains__('s.'))
# print(a.__eq__('s.b,2b'))


# a='211113111'
# print(a.center(9,"*"))
# print(a.count('1',1,3))
# print(a.endswith('1'))
# print(a.find('3',0,6))
# print(a.index('3',0,6))  # 找不到会直接报错

# a = 'a\tlex'
# print(a, a.expandtabs() )
# a = "alex {0} as {1}"
# c = a.format('sb','eric')
# print(c)
# a ="alex {name} as {id}"
# print(a.format(name='sb',id = 'eric'))
# print("alex {0} as {1}".format('ad','akj'))
# import os
# a = os.system('w')
# print(a)
# a={1:2,3:4}
# print(type(a))

# a.pop(1)
# print(a)

# b=[1,2,3,4]
# b.pop(0)
# print(b)
# pids = [1,2,3]
# pms = [4,5,6]
# for x in pms:
#     if x == 5:
#         continue
#     pids.append(x)
#
# print(pids)
# class WithdrawOrder(object):
#     def __init__(self, order):
#         self.order = order
#
#     @classmethod
#     def get(cls):
#         order = True
#         return None if not order else cls(order)
#
#     def audit(self, user):
#         print(user)
#
# withdraw_order = WithdrawOrder.get()
# order_audit_pay = withdraw_order.audit('user')
# a={'q':1,"b":2}
# a['q']=2
# a['q']=3
#
# print(a)

# data=['mac',10000,[2016,10,12]]
# name,price,date=data
# print(name,type(price),date)

# sales_record=[11,12,3,7,9,6,3,5]
# *_,tail=sales_record
# print(_,tail)
# print(sum(head)/len(head))

# records=[
#     ('say_hi','hello'),
#     ('calculate',10,20,30,40),
#     ('dic_handle','name','lhf')
# ]
#
# def say_hi(msg):
#     print(msg)
#
# def calculate(l):
#     res=0
#     for i in l:
#         res+=i
#     print(res)
#
# def dic_handle(l):
#     key,val=l
#     dic={key:val}
#     print(dic)
#
# for func,*args in records:
#     print(type(func), args)
#     if func == 'say_hi':
#         say_hi(args)
#     elif func == 'calculate':
#         calculate(args)
#     elif func == 'dic_handle':
#         dic_handle(args)

# record = 'root:x:0:0:super user:/root:/bin/bash'
# *head, home_dir, _ = record.split(':')
# print(record.split(":"))
# print(head, home_dir, _)
# print('家目录', home_dir)

from collections import deque

# 实现队列,不指定大小则无限添加
# d=deque(maxlen=3)
# d.append(1)
# d.append(2)
# d.append(3)
# print(d)
# d.append(4)
# print(d)
# d.appendleft(5)
# print(d)
# print(d.pop())  # 返回最右边的数
# print(d.popleft())  # 返回最左边的数

# a=[1,2,3,4,5]
# a.pop(0)
# print(a)

# def search(file,pattern,max_len=5):
#     pre_lines=deque(maxlen=max_len)
#     for line in file:
#         if pattern in line:
#             yield pre_lines,line
#         pre_lines.append(line)
# import sys
# sys.path.append('/Users/xialiang/PycharmProjects/py_codetraining/模块/all2.log')
# if __name__ == '__main__':
#     with open('/Users/xialiang/PycharmProjects/py_codetraining/模块/all2.log') as file:
#         for pre_l,line in search(file,'Exchange'):
#             print('-'*60)
#             for i in pre_l:
#                 print(i)
#             print('匹配行----->',line)
import heapq

nums=[1,2,3,-10,100,30,200,21,9,-7]
# print(heapq.nlargest(3,nums))
# print(heapq.nsmallest(3,nums))

# portfolio=[
#     {'name':'IBM','shares':100,'price':91.1},
#     {'name':'AAPL','shares':50,'price':532.1},
#     {'name':'FB','shares':200,'price':21.01},
#     {'name':'HPQ','shares':35,'price':32.75},
#     {'name':'YHOO','shares':45,'price':16.35},
#     {'name':'ACME','shares':75,'price':115.65}
# ]
#
# cheap=heapq.nsmallest(3,portfolio,key=lambda x:x['price'])
# print(cheap)

# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# import re
# rr = re.compile(r"&lt;@([a-zA-Z0-9]{16}|0)\|.+?&gt;")
# ids = rr.findall('&lt;@e808728aa38f53e4|13500001111&gt;&lt;@5cf9b9d04d28ee36|xialiang&gt;&lt;@9d73f3fea6305b1f|13400001111咕咕&gt;')
# print(set(ids))
# if 'e808728aa38f53e4' in set(ids):
#     print(1)
# a={"1":2,"s":3}
# print(list(a))
# task_id = False
# task_id = 1
# if task_id:
#     print(1)

# def foo(m=1):
#     print(m)
#
# foo(m=2)

# import requests,time
#
# r = requests.get('http://task.yunwoke.com/api/projects/task/search?ts=1531729777907&slug=tuan-dui-si-you-xiang-mu-ce-shi-cheng-yuan-shi-shi-xian-shi&ftype=&subject=&status=normal&executor_id=&creator_id=&tag_id='）
# print(r.content)
# to_users=[1,3,4]   # 所有的排序
# to_user=[3]      # 筛选后的
#
# for m in to_users:
#    if not m in to_user:
#       to_users.remove(m)
# print(to_users)
# teams=[1,2,3]
# teams.insert(0, 4)
# print(teams)
# m=[1,2,3]
# for n in m:
#     print(n)
#     if n == 1:
#        print('a')
# a='{:.0%}'.format(42/50)
# print(a)
# no_meaning = False
# def foo(x):
#     if x=="kanban":
#         no_meaning = True
#         print(no_meaning)
# foo("kanban")
# x=''
# y=''
# def foo(x,y):
#     return x,y
#
# if True:
#    foo(1,2)
#    return x, y
# a="abc"
# len(a)=3
import test2

print(1)