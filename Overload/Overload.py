class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,b):
        if(self.a<b.a):
            return "Object 1 is less than object 2"
        else:
            return "Object 1 is greater than object 2"
    def __equal__(self,b):
        if(self.a==b.a):
            return "Object 1 is equal to object 2"
        else:
            return "Both are not equal"

obj1=A(125)
obj2=A(13)

print(f"Values given are {obj1.a} and {obj2.a}")
print(obj1<obj2)

c=A(2)
d=A(1)
print(f"Values given are {c.a} and {d.a}")
print(c==d)