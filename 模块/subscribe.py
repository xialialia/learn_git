from 模块.redis_learn import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()  # 阻塞的，没有消息就卡住
    print(msg)
