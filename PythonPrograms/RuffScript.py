class test:
    def __init__(self):
        print("Hello I'm in constructor")

    @staticmethod
    def hellostatic():
        print("Hey this is static method, No need of Instance creation")

    @classmethod
    def greet(cls):
        print("Hey this is class method")


test.hellostatic()

l=list(range(100))
print([x for x in l if x%2==0])










