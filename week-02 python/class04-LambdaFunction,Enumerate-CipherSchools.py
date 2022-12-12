x=lambda a,b : a + b
print(x(5,2))

y=lambda a,b : a*b
print(y(5,6))

names=["a","b","c","d"]
scores=[20,30,40,50]
for name,score in zip(names,scores):
    print(name,"-",score)

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)