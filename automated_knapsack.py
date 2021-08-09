import itertools

def inp(n,weight,value,max):

    print("Enter the values for the weight:")
    for i in range(n):
        el = input()
        weight.append(el)

    print("Enter the values for the value:")
    for i in range(n):
        el = input()
        value.append(el)
    return  (n,weight,value,max)

def combinations(n, b):
    a = list(range(1,n+1))
    for i in range(1, n+1):
        for subset in itertools.combinations(a,i):
            b.append(subset)
    print(b)

def map(i,weight,w,tw,tv,v):
    for j in i:
        w = int(w) + int(weight[j-1])
        v = int(v) + int(value[j-1])
    tw.append(w)
    tv.append(v)

def logic(weight,w,tw,v,tv,b):
    for i in b:
        map(i,weight,w,tw,tv,v)

def ans(tw,tv,max,Ans):
    temp = 0

    for i in range(len(tw)):
        if temp == tw[i]:
            Ans.append(i)
            print(f'The max possible weight is: {tw[i]}, and the value is {tv[i]}')
        else:
            for i in tw:
                if i >= temp and i <= max:
                    temp = i


'''def logic(n, b, weight, value):
    tw = []
    tv = []
    z = len(b)
    for x in b:
        for z in range(0, n):
            for i in range(0, n):
                tw.append(weight[(x[len(b)[i]]) - 1])
                tv.append(value[(x[len(b)[i]]) - 1])
    print(tw)
    print(tv)'''


'''weight = [6, 4, 10, 6]
value = [16, 30, 20, 10]
max = 16

n = len(value)
Arr = []
tw = []
tv = []

s = list(combinations([1, 2, 3, 4], 1))
t = list(combinations([1, 2, 3, 4], 2))
u = list(combinations([1, 2, 3, 4], 3))
v = list(combinations([1, 2, 3, 4], 4))
Arr = s + t + u + v

for i in Arr:
    if len(i) == 1:
        tv.append(value[(i[0]) - 1])
        tw.append(weight[(i[0]) - 1])

    elif len(i) == 2:
        tv.append(value[(i[0]) - 1] + value[(i[1] - 1)])
        tw.append(weight[(i[0]) - 1] + weight[(i[1] - 1)])

    elif len(i) == 3:
        tv.append(value[(i[0] - 1)] + value[(i[1] - 1)] + value[(i[2] - 1)])
        tw.append(weight[(i[0] - 1)] + weight[(i[1] - 1)] + weight[(i[2] - 1)])

    elif len(i) == 4:
        tv.append(value[(i[0] - 1)] + value[(i[1] - 1)] + value[(i[2] - 1)] + value[(i[3] - 1)])
        tw.append(weight[(i[0] - 1)] + weight[(i[1] - 1)] + weight[(i[2] - 1)] + weight[(i[3] - 1)])

temp = 0
Ans = []

for i in range(len(tw)):
    if temp == tw[i]:
        Ans.append(i)
        print(f'The max possible weight is: {tw[i]}, and the value is {tv[i]}')
    else:
        for i in tw:
            if i >= temp and i <= max:
                temp = i'''


if __name__ == "__main__":
    weight = []
    value = []
    b = []
    max = 0
    Ans = []

    tw=[]
    tv=[]
    w=0
    v=0

    print("Enter the no. of elements:")
    n=int(input())

    print("Enter the max weight")
    max = int(input())

    inp(n, weight, value, max)
    combinations(n, b)
    logic(weight,w,tw,v,tv,b)
    ans(tw,tv,max,Ans)
    print(tw)
    print(tv)

'''

import itertools
w=[4,5,2,9,6,7]
v=[5,6,7,2,1]

c=0
s=0
a = list(range(1,5))
for i in range(1, 5):
    for subset in itertools.combinations(a,i):
        b.append(subset)
#print(b)

s=0
tw=0
b=[]
w=[4,5,2,9,6,7]
def map(i,w,s,tw):
    for j in i:
        s = s + w[j-1]
    tw.append(s)

for i in b:
    map(i,w,s,tw)
'''
