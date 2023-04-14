import redis

# 创建对象
r = redis.StrictRedis(host="127.0.0.1", port=6379, db=0)


def set_code(key, value, t):
    """ key：设置一个key
        value: 设置一个值
        t：设置一个有效期
    """
    r.set(name=key, value=value, ex=t)
    return 'ok'


def get_code(key):
    """ 获取验证码 """
    s = r.get(key)
    if s:
        s = s.decode()
    return s


def dal_code(key):
    """ 删除验证码 """
    return r.delete(key)


if __name__ == '__main__':
    t = get_code('test')
    print(t)
