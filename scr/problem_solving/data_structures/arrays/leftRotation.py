n, d = map(int, input().split())
A = list(map(int, input().split()))
print(*(A[d:] + A[:d])) 

