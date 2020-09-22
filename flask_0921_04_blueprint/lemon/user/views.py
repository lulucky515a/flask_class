from lemon.user.blueprint import user_bp


@user_bp.route('/login')
def login():
    return "login"