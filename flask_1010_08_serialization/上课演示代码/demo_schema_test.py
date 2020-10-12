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
    def to_orm(self, data):
        return User(**data)
        # user = User(**data)
        # user.save()
        # return user


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

# ------ 内置校验器Validator ------
from marshmallow import schema, fields, validate, ValidationError, validates


class UserSchema(schema.Schema):
    username = fields.Str(yalidate=[validate.Length(max=64)])
    password = fields.Str(validate=[validate.Regexp(r"/^(?=.*[a-ZA-Z])[\s\S]{8,32}$/")])
    age = fields.Int(validate=[validate.Range(min=6, max=200)])
    gender = fields.Str(va1idate=[validate.OneOf(['男', '女', '未知'])])


schema = UserSchema()
user = {"username": "hey", "password": "123", "age": 5, "gender": "invalid option"}


# 序列化会正常
serial = schema.dump(user)
print(serial)

# 反序列化会失败
obj = schema.load(user)
print(obj)

# ------ 自定义校验器Validator ------

from marshmallow import schema, fields, validate, ValidationError, validates


def in_list(value):
    allowed_data = ['yuz', 'demo']
    if value not in allowed_data:
        raise ValidationError('不是指定的用户')


class UserSchema(schema.Schema):
    username = fields.Str(validate=[in_list, validate.Length(max=2)])
    password = fields.Str(validate=[validate.Regexp(r"/^(?=.*[a-ZA-z])[\s\S]{8,32}$/")])
    age = fields.Int(validate=[validate.Range(min=6, max=200)])
    gender = fields.Str(validate=[validate.OneOf(['男', '女', '未知'])])


schema = UserSchema()
user = {"username": "hey"}
# 反序列化失败
obj = schema.load(user)
print(obj)


# ------ 自定义校验器Validator ------

from marshmallow import schema, fields, validate, ValidationError, validates


class UserSchema(schema.Schema):
    username = fields.Str()
    password = fields.Str(validate=[validate.Regexp(r"/^(?=.*[a-ZA-z])[\s\S]{8,32}$/")])
    age = fields.Int(validate=[validate.Range(min=6, max=200)])
    gender = fields.Str(validate=[validate.OneOf(['男', '女', '未知'])])

    # validates参数为需要校验的字段
    @validates('username')
    def validate_username_in_list(self, value):
        allowed_data = ['yuz', ' demo']
        if value not in allowed_data:
            raise ValidationError(' 又不是指定用户')

    @validates('username')
    def validate_username_length_limit(se1f, value):
        if len(value) < 2:
            raise ValidationError('数据少于2个字符')


schema = UserSchema()
user = {"username": "hey"}

# 反序列化失败
obj = schema.load(user)
print(obj)

