from peewee模型.Tweet_model import Tweet, User
import peewee
# 获取一条数据使用get()
# a=Tweet.select().join(User).where(User.username == 'xiatian').order_by(Tweet.created_date.desc()).get()
# print(a.id)

# 创建并且得到这条数据user
# user, created = User.get_or_create(username='liyuanyuan')
# print(user.id, created)



# 反向查找，user.tweets就跳转到Tweet表中了
# user = User.get()   # 获取第一条数据
# for m in user.tweets:
#            print(m.id)

# 运算符.注意查询条件
# tweet = Tweet.select().join(User).where((User.username == 'xialiang') | (User.username == 'xiatian') )
# if tweet.id == 4:
#     print(1)
# user = User.select().where((User.username == 'xialiang') | (User.username == 'liyuanyuan'))
# for m in user:
#     print(m.id)
# # tweet = Tweet.select(Tweet.id).where(Tweet.id > 1)
# for m in tweet:
#     print(m.id)
# tweet1 = tweet.where(Tweet.id > 2)
# for m in tweet1:
#     print(m.id)
# tweet = Tweet.select().where(((Tweet.id << [1, 2]) & (Tweet.user_id == 1)) | ((Tweet.id << [1, 2]) & (Tweet.user_id == 2)))
#
# for m in tweet:
#     print(m.id)
# pm_default = Tweet.select().where(Tweet.id != 1).order_by(Tweet.id.desc())
# pm_archive = Tweet.select().where(Tweet.id == 1).order_by(Tweet.id.desc())
# pm_default = list(pm_default)
# pm_archive = list(pm_archive)
project = User()
project.username = 'xiameng'
project.save()
id = project.id
print(id)
# pm_default.extend(pm_archive)
# a=pm_default[:2]
# print(a)
# pm_default = peewee.ModelSelect( pm_default,Tweet)
# pms = pm_default.extend(pm_archive)
# all_count = pms.count()
# print(all_count)
# for m in pm_default:
#     print(m.id)
# pms = pms.paginate(pagenum, pagesize)
# if tweet :
#     print(1)


# for m in tweet:print(m.message)

# get users whose username starts with "x"
# SUBSTR(str,pos,len):这种表示的意思是，就是从pos开始的位置，截取len个字符(空白也算字符)。
# a_users = User.select().where(fn.Lower(fn.Substr(User.username, 1, 1)) == 'x')
# for m in a_users: print(m.username)

# Get tweets by id=1 or 2 using a subquery:
staff_super = User.select(User.id).where((User.id == 1) | (User.id == 2))
# for m in staff_super: print(m.id)
user_st=Tweet.select().where(Tweet.user << staff_super)
# for m in user_st: print(m.message)

# order tweets by the username of the author, then by created_date:
qry = Tweet.select().join(User).order_by(User.username, Tweet.created_date.desc())

# get all usernames and the number of tweets they've made,sort this list from users with most tweets to users with fewest tweets.
# query = (User
#          .select(User.username, fn.COUNT(Tweet.id).alias('num_tweets'))
#          .join(Tweet, JOIN.LEFT_OUTER)
#          .group_by(User.username).order_by(fn.COUNT(Tweet.id).desc()))
# for m in query: print(m.username, m.num_tweets)

# Getting random records
# qur = User.select().order_by(fn.Random())
# for m in qur:print(m.username)

# paginate() 分页
# for tweet in Tweet.select().order_by(Tweet.id).paginate(1, 3):
    # print (tweet.message)

# 使用原生sql
# for name in ('linux', 'tuple', 'list'):
#     db.execute_sql('REPLACE INTO user (username) VALUES (?)', (name,))

# .contains 包含某写字符串
# query = Tweet.select(Tweet.message).where(Tweet.message.contains('ic')).scalar()
# print(query)

# ～表示否定
# strangers = User.select().where(~(User.username << ['xialiang', 'lifangyuan'])).scalar()
# print(strangers)

# null为空 not_in
# User.select().where(User.last_login.is_null(True))
# usernames = []
# a=User.select().where(User.username.not_in(usernames))
# for m in a:print(m.id)

# join
# peewee will use the last joined table as the source table
# User.select().join(Tweet).join(Comment)

# If you would like to join the same table twice, use the switch() method
# Join the Artist table on both `Ablum` and `Genre`.
# Artist.select().join(Album).switch(Artist).join(Genre)

# a = Tweet.get(Tweet.id == 1)
# User.update(username = 'xia').where(User.id == a.user).execute()
# a.user.username = 'xial'
# a.user.save()
# print(a.user.username)