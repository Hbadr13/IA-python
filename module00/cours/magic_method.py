class Example:
    nakename = 'example'
    def __init__(self):
        self.name = 3
        self.name = "s"
        print("Starting")
    @classmethod
    def clsmethod(cls):
        print("I am a clsmethod")
    @staticmethod
    def stcmehod():
        return ("I am a static method")
    def __str__(self):
        return f"handler of seporter for myself{self.nakename}"
    def __len__(self):
        return 3
obj = Example()

print(len(obj)) # => print(obj.__str__)
