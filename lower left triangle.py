n=int(input('number of rows:'))
x=[]

p=0
while p<n:
    x.append('*')
    print(*x,sep=" ")
    p=p+1
