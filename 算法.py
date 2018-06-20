# 题目要求：
#
# 你得到一个可能混合大小写字母的字符串，你的任务是把该字符串转为仅使用小写字母或者大写字母，为了尽可能少的改变：
#
# 如果字符串包含的大字母数小于等于小写字母数，则把字符串转为小写。
#
# 如果大写的数目大于小写字母数，则把字符串转为全大写。
# 用到的知识点map函数
def check_character(c):
    return -1 if c.islower() else 1

def solve(s):
    nums = list(map(check_character, s))
    print(nums)
    return s.upper() if sum(nums)>0 else s.lower()

s='alsjdhaaJJJJJJ'
# print(solve(s))

m={'tom':1, 'height':190}


def foo(m):
    for a, b in enumerate(m):
        print(a, b)


a = list(map(foo, m))

# print(a)