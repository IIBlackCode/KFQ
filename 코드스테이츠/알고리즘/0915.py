import sys

sys.stdin = open("test")

# n,m,v = map(int,input().split())
n,m = map(int,input().split())

l = list()

for i in range(m):
    l.append(input())
    
print(l)