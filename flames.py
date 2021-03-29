a,b=input("Enter name :"),input("Enter name :")
a,b=a.lower(),b.lower()
a,b=a.replace(' ',''),b.replace(' ','')
v={1:"friends",2:"lovers",3:"attraction",4:"marriage",5:"enemies"}
l=[1,2,3,4,5,6]
k,h=[],[]
c=c1=0
for i in range(len(a)):
    if a[i] not in k:
        m,g=a.count(a[i]),b.count(a[i])
        if m>g:
            c=c+g
            k.append(a[i])
        elif m<g:
            c=c+m
            k.append(a[i])
        else:
            c=c+m
            k.append(a[i])
z=(len(a)+len(b))-c*2
while(True):
    for j in range(1,7):
        if j not in h:
            c1+=1
            if c1==z:
                l.remove(j)
                h.append(j)
                c1=0
    if len(l)==1:
        k=l[0]
        print(z,v[k])
        break

        
