while True:
    a=int(input("a="))
    b=a*2
    c=""
    for i in range(b):
        if i==1:
            c+=str(i)
            if (i+1)!=b:
                c+=","
        elif i%2!=0:
            c+=str(i)
            if (i+1)!=b:
                c+=","
        else:
            pass
    print(c)
