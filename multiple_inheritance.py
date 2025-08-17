'''Multiple inheritance'''

class A:
    varA = 'Welcome to class A'

class B:
    varB = 'Welcome to class B'

class C(A,B):
    varC = 'Welcome to class C'


c = C()
print(c.varC)
print(C.varA)
print(C.varB)

