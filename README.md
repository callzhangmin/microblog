# microblog
##学习flask的记录，通过学习flask巩固python

1、Flask提供了一个名为url_for()的函数，它使用URL到视图函数的内部映射关系来生成URL。 例如，url_for('login')返回/login，url_for('index')返回/index。url_for()的参数是endpoint名称，也就是视图函数的名字。
2、 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
    class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__