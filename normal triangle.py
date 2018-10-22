
n=int(input('enter side:'))
x=[]
for i in range(2*n-1):
    x.append(' ')

p=[]
for i in range(0,n):
    k=i
    while k<=(2*n-1)-i:
        x[k]='*'
        k=k+2
    j=''.join(x)
    p.append(j)
    k=i
    while k<=(2*n-1)-i:
        x[k]=' '
        k=k+2

p.sort()

for j in p:
    print(j)
