# def foo():
#
#     return 1 if 1>0
# def get_user_id():
#     if  True:
#         return None
#     return 1
#
# print(get_user_id())
# def foo():
#   if not False:
#      return 1
#   print(2)
#   if not False:
#     print(3)
#
# print(foo())
# if True:
#   try:
#      raise Exception('错误了。。。')
#   except Exception as e:
#      pass


class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


# try:
#     raise WupeiqiException('我的异常')
# except WupeiqiException as e:
#     a=e
# print(a)

# class Foo(object):
#     pass
#
#
# obj = Foo()
#
# print(isinstance(obj, Foo))

# class Foo(object):
#     pass
#
#
# class Bar(Foo):
#     pass
#
#
# print(issubclass(Bar, Foo))

# class Foo(object):
#     def __init__(self):
#         self.name = 'xialiang'
#     def func(self):
#         return 'func'
#
# obj = Foo()
# print(hasattr(obj, 'name'))
# print(getattr(obj, "func"))
# setattr(obj, "age", 18)
# print(getattr(obj, 'age'))
# setattr(obj, 'show', lambda num: num + 1)
#
# print(obj.show(1))

# import sys
#
#
# def s1():
#     print ('s1')
#
#
# def s2():
#     print ('s2')
#
# print(__name__)
#
# this_module = sys.modules[__name__]
#
# hasattr(this_module, 's1')
# getattr(this_module, 's2')
# import sys
#
# def fn():
#     print('hello world')
#
# func_name = fn.__name__
# print(func_name)
# fn_obj = getattr(sys.modules[__name__], func_name)
#             # 便是找到当前文件下名称为func_name的对象（类对象或者函数对象）。
#             # 根据函数名（func_name），获得函数对象
# print(sys.modules[__name__])
# fn_obj()
# to_users = [2,1]
# to_user=[1,2,4,3]
# to_user.extend(to_users)
# print(to_user)
# to_user = list(set(to_user))
#
#
# if to_user:
#     print(to_user)
# def get_project_info(project, project_index = 0):
#     if project_index:
#         print(1)
#
# get_project_info("project")
# props_total = []
# pagenum = 1
# pagesize = 3
# props = props_total[(pagenum-1):pagesize]
# print(props)
# L=[{'status':1,'com':'a'},{'status':2 ,'com':'c' },{'status':3 ,'com':'b' },{'status':4 ,'com':'a' }]
# L.sort(key=lambda x:(-x['status'])) #
# print(L)
# a= [1,2,3,4]
# n= [2,1,7]
# a.append(n)
# print(a)
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# site.pop('name')
# print(site)
# class MilestoneSearch():
#     def __init__(self,name):
#         MilestoneSearch.nam
#     def get(cls):
#         cls.foo()
#
#     def foo(self):
#         print(1)
#
# MilestoneSearch.foo()

a=[{"a":1,"x":2}]
# a[-1]["a"] = 3
print(a[-1])