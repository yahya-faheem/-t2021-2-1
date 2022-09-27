c=str(input("Enter list of number\n"))
d=c.strip("][").split(",")
b={}
for i in range(1,10):
    a=0
    for j in d:
        if (int(j))%i==0:
            a+=1
        else:
            pass
    b[i]=a
print(b)
