n=int(input('number of rows:'))
x=[]
for i in range(2*n-1):
    x.append(' ')
p=[]
k=0
while k<2*n-1:
    x[k]='*'
    j=''.join(x)
    p.append(j)
    k=k+2

p.sort(reverse=True)
for i in p:
    print(i)
    
