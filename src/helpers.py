import time
import functools


def add_delay(pre, post):
    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            time.sleep(pre)
            res = f(*args, **kwargs)
            time.sleep(post)
            return res
        return inner
    return wrapper
