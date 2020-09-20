import time


def log_time(f):
    def decorator():
        print(time.time())
        return f()
    return decorator

@log_time
def project():
    return "project"


project()