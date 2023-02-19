A=[i for i in range(-10,10)]
def egor(x):
    return x*x-3*x+1
B=[]
for f in range(len(A)):
    B.append(egor(A[f]))
print(A)
print(B)
maxB=max(B)
minB=min(B)
for i in range(len(B)):
    if B[i]==maxB or B[i]==minB:
        print(B[i])
