def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)

def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))
    print(separator.join(args))

def concat(*args,sep="/"):
    return sep.join(args)

concat("earth","mars","venus")
concat("earth","mars","venus",sep=".")

standard_arg("standard_arg(arg)")   
standard_arg(arg = "standard_arg(arg)")  

pos_only_arg("pos_only_arg(arg)")   
# pos_only_arg(arg = "pos_only_arg(arg)")  

# kwd_only_arg("kwd_only_arg(arg)")   
kwd_only_arg(arg = "kwd_only_arg(arg)")   

def foo(name,**kwds):
    return 'name'in kwds

# foo(1,**{'name':2})

l = [1,4,3,2]
l.sort();
print(l)

pairs =[(1,'1'),(2,'12'),(3,'3'),(4,'21')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)

# squares =[]
# for x in range(10):
#     squares.append(x**2)
# print(squares)


# squares = lambda x:x**2,range(10)
# -> 변환하기 >>> 과제!!!
# squares = []
# def f(x):
#     return x**2
# for x in range(10):
#     squares.append(f(x))

# squares = list(map(lambda x:x**2,range(10)))
# print(squares)
squares = [x**2 for x in range(10)]
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

print([(x,y) for x in [1,2,3]for y in [3,1,4]if x !=y])

a = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x !=y:
            a.append((x,y))
print(a)

vec =[[1,2,3],[4,5,6],[7,8,9]]

# [
# 0: [1,2,3],
# 1: [4,5,6],
# 2: [7,8,9]
# ]
print(vec[1][2])
print(vec)
vec2 = [num for elem in vec for num in elem]
print(vec2)
print(vec2[5])

from math import pi
print([str(round(pi,i)) for i in range(1,6)])

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print([[row[i]for row in matrix]for i in range(4)])
temp = []
for i in range(4):
    itemTemp = []
    for row in matrix:
        itemTemp.append(row[i])
    temp.append(itemTemp)
print(temp)        