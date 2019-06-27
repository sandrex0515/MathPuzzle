import random

x = ["Saab", "Volvo", "BMW"]
y,z = 2,4
xx = 'sandrex, cabrales {}'
print(x[1] + " " + x[0])
# []
print(type(z))
print(random.randrange(1,100))
print(y)

print(xx[0:10].strip())
print(len(x))
print(xx.upper())
print(xx.replace("a", "S"))
print(xx.split(","))
print(xx.format(y))
print(y ** z)
print(y is not z)
for zz in x:
    print(zz)
    if 'BMWs' in x:
        print('YES!')
else:
    print('NO!')
    i = 0
    while i < len(x):
        print(i)


        i += 1

for z2 in x:
    print(z2)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + "And I am " + self.age)

p1 = Person("Sandrex", "23")
p1.myfunc()


exit() #exit