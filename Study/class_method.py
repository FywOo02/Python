class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @staticmethod
    def static_test_method():
        print("This is a static method")


# 创建该工具对象
tool1 = Tool("Axe")
tool2 = Tool("Hammer")

# 调用类方法
Tool.show_tool_count()
