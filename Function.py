A=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def egor(x):
    return x*x-3*x+1
B=[]
for f in range(len(A)):
    B.append(egor(A[f]))
print(A)
print(B)
maxB=max(B)
minB=min(B)
print(maxB)
print(minB)
