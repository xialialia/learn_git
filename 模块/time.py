import datetime
# --------------------------我们先以当前时间为准,让大家快速认识三种形式的时间
# print(time.time()) # 时间戳:1487130156.419527
# print(time.strftime("%Y-%m-%d %X")) #格式化的时间字符串:'2017-02-15 11:40:53'
#
# print(time.localtime()) #本地时区的struct_time
# print(time.gmtime())    #UTC时区的struct_time
# print(time.strftime("%Y-%m-%d %X", time.localtime()))
# print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))

# -------datetime-----
# 1.datetime.date：表示日期的类
# today=datetime.date.today()
# print(today)
# t = datetime.date(2014,8,15)
# print(t)
# m = t.strftime('%Y-%m-%d %X')  # 字符串
# print(m)
# print(today.timetuple())  # 结构化时间
# a = time.mktime(today.timetuple())  # 时间戳
# print(datetime.date.fromtimestamp(a))  # 时间戳转化为date
# print(today.replace(month=3))

# -------2、datetime.datetime 类----
# d1 = datetime.datetime.today()
# print(d1)
# d2 = datetime.datetime(2014, 8, 15, 8, 12, 34,)
# print(d2)
# d3 = datetime.datetime.now()  # 和.today()一样
# print(d3)
# d4 = d3.strftime('%Y-%m-%d %H:%M:%S')  # 转成str
# print(d4)
# print(d1.replace(year=2000))
# print(datetime.datetime.fromtimestamp(time.time()))
# print(time.mktime(d1.timetuple()))  # 结构化时间转为时间戳

# -------3,timedelta------
d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')  # str转为datetime
d2 = datetime.datetime.strptime('2012-03-02 15:40:08', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
print(d1, d2, type(delta), delta.days,)
# delta = datetime.timedelta(days=3)
print(d1+datetime.timedelta(days=delta.days), )