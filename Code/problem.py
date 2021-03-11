A=[]
n=int(input("ENTER THE FINAL ODD NUMBER YOU WISH"))
for i in range(0,n):
    if (i%2!=0):
        A.append(i)
print(A)
B=[]
c=[1,2]
D=[]
for i in A:
    fn=((3**i)/2**(i-1))*((i+1)-2)
    B.append(fn)
    if fn in c:
        D.append(fn)
print(B)
print(D)