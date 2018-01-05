def SumOf(n):
    if n == 0:
        return None
    elif n == 1:
        return 1
    else:
        return n + SumOf(n-1)

print(SumOf(0))
print(SumOf(3))
print(SumOf(10))

def RemoveDup(st):
    st = ''.join(sorted(st))
    if len(st) == 1:
        return st
    elif st[0] == st[1]:
        return RemoveDup(st[1:])
    else:
        return st[0] + RemoveDup(st[1:])

print(RemoveDup('aaaabbbbccccccdddddddd'))
print(RemoveDup('aabbaddabccbcddccddcdd'))

