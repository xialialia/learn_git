# from datatimes import User
import datetime


from tweet import *
# xia = User.create(username='xialiang', password=123, email='123@123xia.com',)
# liang = User.create(username='liang', password=123, email='123@123xia.com', join_date='2016-06-30 16:00:00')
# tweet = Message.create(user=2, content='hello',pub_date='2016-06-30 16:00:00')
# li = User()
# li.username = 'lifann'
# li.password = 12314
# li.email = 'hdfbd@123.com'
# li.save()
# print(li.id)
# User.insert(username='xiayu',password= 13213,email='ahhf@qwu.com').execute()

# User.update({User.password:int(User.password)+int(1)}).execute()
# User.replace(id=1,username='aiud',email='jadfbh@jke.com',password=1213).execute()
# User.delete().where(User.id>4).execute()
# User.update(password=123485).where(User.id>3).execute()
# a = User.select(User.username).where(User.id>2)
# b = a.where(User.username=='xiayu')
# # print([m.username for m in b])
# print(b[0].username)
# print(a[2].username)
# a = Message.select().where(Message.id==2).get()
# print(a.content)
# a= User.select(User,fn.LENGTH(User.username)).order_by(fn.LENGTH(User.username), User.id.desc())
# # print([a])
# for m in a:
#     print(m.username)


# a= User.select().group_by(User.id).having(User.password == 123)
# b= User.select().group_by(User.id).having(User.password != 123)
c= []
a = User.select().where(User.password==123)
b = User.select().where(User.password!=123).order_by(User.id.desc())


# for m in a:
#     c.append(m)
#
# for n in b:
#     c.append(n)
#
# print(c)

a=2








