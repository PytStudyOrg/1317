A = [5,9,2,3,8]
N=len(A)
M = A[0]
for i in range(1,N):
     if A[i] > M:
         M = A[i]
 print(M)

 for x in A:
     if x > M:
         M=x
 print(M)

M=max(A)
nMax=A.index(M)
print("A[",nMax,"]=",M,sep="")