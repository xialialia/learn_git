# startswith() 方法用于检查字符串是否是以指定子字符串开头  filter函数会将返回 True 的元素放到新列表中
# movie_people=['alex_sb','wupeiqi_sb','linhaifeng','yuanhao_sb']
# print(list(filter(lambda n:not n.endswith('sb'),movie_people)))

# map函数
# msg='linhaifeng'
# print(''.join(list(map(lambda x:x.upper(),msg))))

# reduce函数
# from functools import reduce
# num_l=[1,2,3,100]
# print(reduce(lambda x,y:x+y,num_l,1))
# print(reduce(lambda x,y:x+y,num_l))
# print(reduce(lambda x,y:x+y, range(0,101)))
a=''
a=1
if a:
    a=2
print(a+1)