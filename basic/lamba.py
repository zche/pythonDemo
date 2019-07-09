
f = lambda x,y,z : x+y+z  
print(f(1,2,3))
  
g = lambda x,y=2,z=3 : x+y+z  
print(g(1,z=4,y=5))


L = [(lambda x: x**2),  
    (lambda x: x**3),  
    (lambda x: x**4)]  
print (L[0](2),L[1](2),L[2](2))
  
D = {'f1':(lambda: 2+3),  
    'f2':(lambda: 2*3),  
    'f3':(lambda: 2**3)}  
print (D['f1'](),D['f2'](),D['f3']())


from functools import reduce 
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
 
print (list(filter(lambda x: x % 3 == 0, foo)))
#[18, 9, 24, 12, 27]
 
print (list(map(lambda x: x * 2 + 10, foo)))
#[14, 46, 28, 54, 44, 58, 26, 34, 64]
 
print (reduce(lambda x, y: x + y, foo))
# 139