a=(7,2,3,4,8,9,10)
i=input("enter a value")
for i in range(0,len(a)-1):
 if i>a:
    a+=1
    print(a.count(a[0]+i))
 else:
    print("lll")
