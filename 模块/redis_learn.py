# import redis
# r = redis.Redis(host='127.0.0.1', port=6379)
# r.set('foo', 'Bag')
# r.is_internal = True
#
# print(r.is_internal)

# import redis, time
#
# pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
#
# r = redis.Redis(connection_pool=pool)
# r.set('foo', 'car', nx=True)
# # time.sleep(2)
# print(r.get('foo'))

# r.mset(k1='v1', k2='v2')
# print(r.mget('k1', 'k2'))

# print(r.getset('k1', 'v445'))
# print(r.getrange("k1", 1, 2)) # range就涉及到索引的赋值和取值
# r.setrange("k1", 1, 77)
# print(r.get('k1'))
# r.append('k1','ert')
# print(r.get('k1'))

# hash
# r.hset('name', "xia", "liang")
# print(r.hget('name', "xia"))
# r.hmset('xx', {'k1':'v1', 'k2': 'v2'})
# print(r.hmget('xx', "k1", "k2"))
# print(r.hgetall("xx"))

# r.rpush('bb',  66,11,22,33,55)
# print(r.lindex('bb', 0))
# print(r.lpop('bb'))

# r.sadd('nam',{1,2,3},{3242,1})
# print(r.scard("nam"))

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):  # 发布
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()   # 监听
        return pub




