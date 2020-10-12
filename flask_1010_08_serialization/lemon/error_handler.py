
def not_found(err):
    return {"result": "failed", "msg": "no this page"}, 404


def server_error(err):
    return {"result": "failed", "msg": "server error"}, 500


def zero_error_handler(err):
    return {"result": "failed", "msg": "can divide 0"}, 500
    # return Api


def validation_handler(err):
    return {"result": "failed", "msg": err.messages}, 401