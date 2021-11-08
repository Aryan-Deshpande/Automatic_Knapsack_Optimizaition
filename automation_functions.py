import itertools

#varibale initialisation
weight = []
value = []
b = []
max = 0
Ans = []
tw=[]
tv=[]
w=0
v=0

#data proccessing functions
def inp(n,weight,value,max):

    print("Enter the weight for each of the elements:")
    for i in range(n):
        el = input()
        weight.append(el)

    print("Enter the values for each of the elements")
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