class A(object):
    def bark():
        print "ohai"

class B(A):
    def blub(self):
        self.bark()

class C(B):
    pass
