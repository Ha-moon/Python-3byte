import random
a=[]
for x in range(0,100):
    a.append(x)
random.shuffle(a)
for y in range(1,100):
    for i in y-1:
        if a[i]>a[i+1] :
            b=a[i]
            a[i+1]=a[i]
            a[i]=b
print(a)
