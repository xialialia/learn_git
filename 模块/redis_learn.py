# import redis
# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('foo', 'Bag')
# r.is_internal = True
# print(r.get("foo"))
# print(r.is_internal)

import redis, time

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

r = redis.Redis(connection_pool=pool)
# r.set('foo', 'car', nx=True)  # nx，如果设置为True，则只有name不存在时，当前set操作才执行
# time.sleep(2)
# print(r.get('foo'))

# r.mset(k1='v1', k2='v2')  # 批量设置值
# print(r.mget('k1', 'k2'))

# print(r.getset('k1', 'v445')) # 设置新值并获取原来的值
# print(r.getrange("k1", 1, 2)) # range就涉及到索引的赋值和取值
# r.setrange("k1", 1, 77)  #  修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# print(r.get('k1'))
# r.append('k1','ert')
# print(r.get('k1'))

# hash
# r.hset('name', "xia", "liang")
# print(r.hget('name', "xia"))
r.hmset('xx', {'k1':'v1', 'k2': 'v2'})  # 在name对应的hash中批量设置键值对
print(r.hmget('xx', "k1", "k2"))
print(r.hgetall("xx"))

# r.rpush('bb',  66,11,22,33,55)
# print(r.lindex('bb', 0))
# print(r.lpop('bb'))

# r.sadd('nam',{1,2,3},{3242,1})
# print(r.scard("nam"))

# import redis
#
#
# class RedisHelper:
#
#     def __init__(self):
#         self.__conn = redis.Redis(host='127.0.0.1')
#         self.chan_sub = 'fm104.5'  # 订阅频道
#         self.chan_pub = 'fm104.5'  # 发布频道
#
#     def public(self, msg):  # 发布
#         self.__conn.publish(self.chan_pub, msg)
#         return True
#
#     def subscribe(self):
#         pub = self.__conn.pubsub()  # 打开收音机
#         pub.subscribe(self.chan_sub) # 调整频道
#         pub.parse_response()   # 准备监听
#         return pub




