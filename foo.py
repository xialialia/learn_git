# def hello():
#     print('hello')
#
# hello()
# a= [{'name':'xia','time':'123'},{'name':'liang','time':'321'}]
# b=[]
# for m in a:
#         b.append(m['time'])
#
# print(b)
L= [1,2,3,0]
def is_increasing_normal(lst):
    for i in range(0, len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

print(is_increasing_normal(L))


