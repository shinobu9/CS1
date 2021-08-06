def prefixfunc(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i-1]
        while k > 0 and s[i] != s[k]:
            k = p[k-1]
        if s[i] == s[k]:
            k+=1
        p[i] = k
    return p

def zfunc(s):
    zf = [0] * len(s)
    left = 0
    right = 0
    for i in range(1, len(s)):
        zf[i] = max(0, min(right - i, zf[i - left]))
        while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf
            
def findstr(s, x):
    p = zfunc(x + s)
    #print(p)
    ans = []
    for i in range(len(x), len(p)):
        if p[i] >= len(x):
            ans.append(i - len(x))
    if ans == []:
        ans.append(-1)
    return ans
        

x = input()
s = input()
#p = prefixfunc(s)
#p = zfunc(s)
ans = findstr(s, x)
print(' '.join([str(i) for i in ans]))