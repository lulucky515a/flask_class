# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：demo_schema_test 
# 当前登录名：LuckyLu
# 创建日期：2020/9/29 16:24
# 文件IDE名称：PyCharm


from marshmallow import schema, fields, post_load, post_dump, validate


class User:
    def __init__(self, name, password="hello"):
        self.name = name
        self.password = password


class UserSchema(schema.Schema):
    name = fields.Str(required=True, validate=[validate.Length(max=6)])
    password = fields.Str(required=True)

    # # TODO: 小 BUG, 一定要加上 **kw
    @post_load
    def to_orm(self, data, **kwargs):
        return User(**data)


schema = UserSchema()
# 反序列化 load
# request.json
user_data = {"name": "yuz234", "password": "123456"}

data = schema.load(user_data)
# 得到的还是一个字典。， 而不是通常意义上的 python 对象 User
# 数据校验
print(data)
print(data.name)
print(data.password)