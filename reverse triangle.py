
n=int(input('number of rows:'))
x=[]
for i in range(2*n-1):
    x.append(' ')



for i in range(1,n+1):
    k=i-1
    while k<=(2*n-1)-i:
        x[k]='*'
        k=k+2
    print(*x,sep="")
    k=i-1
    while k<=(2*n-1)-i:
        x[k]=' '
        k=k+2
    
    
        

    
    
    
    
    
