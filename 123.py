# from mysql import Person
# from tweet import *
# from category import *
from datatimes import *

import datetime

now = datetime.datetime.now()
print(now)
#你拿到的数据是一条数据还是多条数据，如果是多条数据就要循环，首先拿到一条数据（实例对象），然后再用.获得属性
# a = Message.select().where(Message.id==1).get()
# a = Message.select()
# b= Message.select().where(Message.id == 9)
# print(a.user.username)
# print([m.user.username for m in a])
# print(b)
# print(a[1].id)
#反向查找
# a = User.select().where(User.username == 'andy')
# print([m.message for m in a.messages])

# a= User.select()
# for m in a:
#     for n in m.messages:
#         print(n.content)
#
# a= Message.select(Message.id).where(Message.id <= 3).limit(1).first()
# print(a.id)
# a = Message.select().join(User).where(User.id == 1)
# print([m.content for m in a])
#每个用户发的message数
# messages=Message.select(Message,fn.count(Message.id).alias('num_messages'),User.id)\
#     .join(User).group_by(Message.user)
#下面m.user.id的user必须是小写
# print([(m.num_messages,m.user.id) for m in messages])
# users = (User
#          .select(User, fn.Count(Message.id).alias('num_tweets'))
#          .join(Message, JOIN.LEFT_OUTER)
#          .group_by(User.id)
#          .order_by(fn.Count(Message.id).desc()))
#
# print([(m.username,m.num_tweets) for m in users])
#我会关注那些用户
# a = (User
#  .select()
#  .join(Relationship, on=Relationship.to_user)
#  .where(Relationship.from_user == 2))
#
# for m in a:
#     print(m.username)
#自关联
# Parent = Category.alias()
# a= Category.select().join(Parent, on=(Category.parent == Parent.id))\
#     .where(Parent.name == '家电')
# # print(a)
# print([m.id for m in a])
#比较时间大小的筛选
a=User.select().where(User.id == 2).get()
print(1111111)
a_time = a.join_date
print(a_time)
# m=(now-a_time).days
b = User.select().where(User.join_date > a_time)
for m in b:
    m.join_date = datetime.timedelta((now - a_time).days) + m.join_date
    m.save()
    print(m.join_date)



