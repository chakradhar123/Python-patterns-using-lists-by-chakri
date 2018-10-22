
n=int(input('number of rows:'))
x=[]
for i in range(2*n-1):
    x.append(' ')

p=0
while p<2*n-1:
    x[p]='*'
    p=p+2
print(*x,sep="")
for i in range(1,2*n-2):
    x[i]=' '
k=0
while k<n-2:
    print(*x,sep="")
    k=k+1
m=0
while m<2*n-1:
    x[m]='*'
    m=m+2
print(*x,sep="")
    
