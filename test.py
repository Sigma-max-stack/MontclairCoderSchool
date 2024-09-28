# # def add2(x, y):
# #     return x+y
    
# # print(add2(5, 6))

# # def subtract2(x, y):
# #     return x-y

# # print(subtract2(7 , 3))  

# # def multi4(x):
# #     return 7*x

# # print(multi4(7))   

# # def squared(x):
# #     return x*x

# # print(squared(9))

# # def rectangleP(l, w):
# #     return l*2 + w*2
# # print(rectangleP(7, 3))

# # def rectangleA(l, w):
# #     return l*w

# # print(rectangleA(7, 3))

# def square(l):
#     return l*4+l*l

# print(square(5))

# def three_add(x, y, z):
#     return(x+y+z)

# print(three_add(4,5,6))
'''
def op(x,y):
    a = x*y
    b = x+y
    return(a+b)

print(op(4, 5))    
'''
'''
def op2(x, y):
    a = x*y
    b = x+y
    if a>b:
        return(a-b)
    else:
        return(b-a)
print(op2(1, 1))
'''
'''
def c_circle(r):
    return(2*3.14*r)

print(c_circle(5))

def a_circle(r):
    return(3.14*r*r)
print(a_circle(5))    
'''

def op_circle(r):
    c = 2*3.14*r
    a = 3.14*r*r
    if a>c:
        return("area is bigger")
    else:
        return("circumfrence is bigger")
print(op_circle(5))