## session vs token
- token 令牌


- session 会话， 数据结构
{
    "user:1": yuz,
    "user:2"：xingye
}

- token 消耗的是计算资源，CPU;  session 消耗存储资源，IO 资源；
- session 机制，可以在客户端可以自动处理 session_id, 访问同域的地址时，
- 浏览器会自动把 session_id,
- token 是需要手工处理的。 Authorization: JWT kfowofwfwfwfowo, 跨域


## flask 项目当中使用 jwt
- pyjwt
- flask-jwt-extended

操作：
- 安装
- 注册插件
- SECRET_KEY (秘钥)
- 生成 token (注册，登录)
- 在访问的视图函数上加上校验的装饰器


## 序列化
- json 处理。 python 字典，   json字符串
-  python  --->  通用的数据格式。  序列化
