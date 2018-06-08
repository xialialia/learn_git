import json
# f = open('text1','w')
# dic={'name':'xialiang','age':'24'}
# data = json.dumps(dic)
# f.write(dic)

f = open('text1','w')
dic={'name':'xialiang','age':'24'}
json.dump(dic,f)
f.close()
