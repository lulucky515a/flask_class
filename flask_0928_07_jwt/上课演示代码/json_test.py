# -*- coding: UTF-8 -*-
# 当前项目的名称: flask_class 
# 新文件名称：json_test 
# 当前登录名：LuckyLu
# 创建日期：2020/9/30 10:55
# 文件IDE名称：PyCharm 

# https://www.jianshu.com/p/c460c4c97acb Flask 序列化对象封装及自定义json返回类型
class Solution(object):
    name = 'wyq'
    age = 89

    def __init__(self):
        self.gender = '女'


o = Solution()
print(o.__dict__)
# python中类变量是不会存放到__dict__,只有实例变量才会存入
# {'gender': '女'}


# ------ 如果获取到__dict__下的所有实例变量和类变量，我们就可以用jsonify序列化对象 ------
# 定义keys和__getitem__方法,key方法个性化可以放到对象中，getitem固定不变建议放入Base基类中
class Solution2(object):
    name = 'wyq'
    age = 89

    def __init__(self):
        self.gender = '女'

    def keys(self):
        return ['name', 'age', 'gender']

    def __getitem__(self, item):
        return getattr(self, item)


o2 = Solution2()
print(dict(o2))
