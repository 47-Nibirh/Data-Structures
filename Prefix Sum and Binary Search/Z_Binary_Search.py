N, Q = map(int, input().split())

A = list(map(int, input().split()))

A.sort()

while Q:
    Q -= 1

    x = int(input())
    l = 0
    r = N - 1
    flag = False

    while l <= r:
        mid = (l + r) // 2

        if A[mid] == x:
            flag = True
            break

        if x > A[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if flag:
        print("found")
    else:
        print("not found")