l=int(input('enter no of asterisks from left to right:'))
b=int(input('enter no of asterisks from top to bottom:'))
x=[]
for i in range(2*l-1):
    x.append(' ')

p=0
while p<2*l-1:
    x[p]='*'
    p=p+2
print(*x,sep="")
for i in range(1,2*l-2):
    x[i]=' '
k=0
while k<b-2:
    print(*x,sep="")
    k=k+1
m=0
while m<2*l-1:
    x[m]='*'
    m=m+2
print(*x,sep="")
