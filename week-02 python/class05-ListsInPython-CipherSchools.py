a=[1,2,3,4,5,6]
print(a)
print(len(a))

for i in a:
    print(i)

a.insert(1,100)
a.append(5)
print(a)

a.sort()
sorted(a)
print(a)

a.reverse()
list(reversed(a))
print(a)

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

",".join(["Jatin","Ram","Tinku"])
