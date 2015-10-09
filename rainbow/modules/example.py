
class D(object):

    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1


class MyClass(object):

    def __init__(self):
        self.a = 1
        self.b = 2
        self._c = True
        self.d = D()

    def add(self):
        return self.a + self.b

    def log(self):
        return "log:", self.a, self.b
