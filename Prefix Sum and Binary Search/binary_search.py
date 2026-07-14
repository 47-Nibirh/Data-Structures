n = int(input())
arr = list(map(int,input().split()))
x = int(input())

l= 0
r = n-1

flag = False

while l<=r:
    mid_index = (l+r)//2

    if arr[mid_index] == x:
        flag = True
        break

    if x>arr[mid_index]:
        l = mid_index +1
    else:
        r = mid_index - 1

print(l, r)

if flag:
    print("YES")
else:
    print("NO")