
class D(object):

    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1


class MyClass(object):

    def __init__(self):
        self.a = 0
        self._b = True
        self.c = D()

    def log(self):
        return "log:", self.a

    def add(self, p=1, q=2, r=3):
        return p + q + r
