for i in range(2,30):
    j=2
    flag=0
    while j<i:
        if i%j==0:
            flag=1
            j+=1
        else:
            j+=1
    if flag==0:
        print(i,"is a prime no.")
    else:
        flag=0
