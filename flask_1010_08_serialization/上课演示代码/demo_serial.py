from marshmallow import schema, fields


class User:
    """ORM 对象"""
    name = "yuz"
    password = "123456"
    age = "helloo"


class UserSchema(schema.Schema):
    name = fields.Str()
    password = fields.Str()
    # age = fields.Integer()


# 序列化操作
# ------ 最基本的序列化 过滤age ------
# schema = UserSchema()
# data = schema.dump(User)
# print(data, type(data))

# ------ only 包含的数据字段 ------
# schema = UserSchema(only=['name', 'password'])
# data = schema.dump(User)
# print(data)

# ------ exclude 包含的数据字段 ------
# schema = UserSchema(exclude=['age'])
# data = schema.dump(User)
# print(data)

# ------ 多值序列化 ------
schema = UserSchema(exclude=['password'], many=True)
data = schema.dump([User, User, User])
print(data)