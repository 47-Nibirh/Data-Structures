n,q = map(int,input().split())

a = list(map(int,input().split()))

pre = [0]*n

pre[0] = a[0]

for i in range(1,n):
    pre[i] = pre[i-1]+a[i]



while q>0:
    l,r = map(int,input().split())

    l-=1
    r-=1

    if l==0:
        ans = pre[r]
    else:
        ans = pre[r]-pre[l-1]

    print(ans)

    q-=1