people=[
    {'name':'alex','age':1000},
    {'name':'wupei','age':10000},
    {'name':'yuanhao','age':9000},
    {'name':'linhaifeng','age':18},
]
max(people,key=lambda dic:dic['age'])
print(max(people,key=lambda x:x['age']))