#!/usr/bin/python
def convert_to_base(n, b):
    base = []
    while n:
        n, r = divmod(n, b)
        base.append(r)
    return base

def answer(n):
    limit = round((n + 2) if (n <= 6) else (n / 2))
    for b in range(2, limit, 1):
        base = convert_to_base(n,b)
        if (n % b) and (base == base[::-1]):
            return b
    
    return 2 if (n == 0) else (n - 1)

print(answer(42))
