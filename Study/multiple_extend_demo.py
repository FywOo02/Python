class A:
    def test(self):
        print("test")


class B:
    def demo(self):
        print("demo")


class C(A, B):
    pass


c = C()
c.test()
c.demo()