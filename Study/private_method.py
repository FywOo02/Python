class Man:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def secrete(self):
        print("%s的年龄是%d" % (self.name, self.__age))


cho = Man("Cho", 18)
cho.secrete()
