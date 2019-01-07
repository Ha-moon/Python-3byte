a=[3,9,6,7,4]
for i in range(0,5):
    for j in range (0,4) :
        if a[j]>a[j+1]:
            k=a[j]
            a[j]=a[j+1]
            a[j]=k
            i=i+1
print (a)