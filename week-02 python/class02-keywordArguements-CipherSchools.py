def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)
func(c=8,a=6,b=2)

def hello():
    print("Hello World")
a=hello
a()

def func(a=1,b=2):
    print(a,b)
func()

def func(a,b,*c):
    print(a)
    print(b)
    print(c)
func(1,2,3,6,54,8)

def func(a,b=1,*c,d,e="",**k):
    print(k)
func(name="Jatin")

