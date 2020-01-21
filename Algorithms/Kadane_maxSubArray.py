a = list(map(int,input().split()))
kde(a)

def kde(a):
    max_current = a[0]
    max_global = a[0]
    for i in range(1,len(a)):
        max_current = max(a[i],(max_current+a[i]))
        if(max_current > max_global):
            max_global = max_current
    return max_global
