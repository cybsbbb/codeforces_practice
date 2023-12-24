from sys import stdin
# from sortedcontainers import SortedList
import functools
input=lambda:stdin.readline().strip()
n,m,q=map(int,input().split())
s=[0]+list(map(int,list(input())))
node=[i for i in range(n+2)]
priority=[-1]*(n+1)
pri=1
# S=SortedList([i for i in range(n+2)])
for i in range(m):
    l,r=map(int,input().split())
    while l<=r:
        while l!=node[l]:
            l=node[l]
        if l<=r:
            priority[l]=pri
            pri+=1
            node[l]=r+1
            l+=1
    # temp=S[S.bisect_left(l)]
    # while temp<=r:
    #     priority[temp]=pri
    #     S.remove(temp)
    #     pri+=1
    #     temp=S[S.bisect_left(temp+1)]
print(priority)
length=pri-1
for i in range(1,n+1):
    if priority[i]==-1:
        priority[i]=pri
        pri+=1
priority[0]=0
print(priority)
SUM=[0]*(n+1)
def lowbit(x):
    return x&(-x)
def update(index,d):
    while index<=n:
        SUM[index]+=d
        index+=lowbit(index)
def find(index):
    ret=0
    while index>0:
        ret+=SUM[index]
        index-=lowbit(index)
    return ret
# print(priority)
for i in range(1,n+1):
    if s[i]:
        update(priority[i],1)
# print(SUM)
for i in range(q):
    x=int(input())
    if s[x]==0:
        update(priority[x],1)
    else:
        update(priority[x],-1)
    s[x]^=1
    count=find(n)
    if count<=length:
        print(min(count,length)-find(count))
    else:
        print(length-find(length))

