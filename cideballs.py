import time

def elder_age(m,n,l,t):
    total = 0
    for r in range(n):
        for c in range(m):
            xor = (c ^ r) - l
            if xor > 0: total += xor
    total %= t
    return total

def runtest(m,n,l,t):
    starttime = time.time()
    elder_age(m,n,l,t)
    endtime = time.time()
    return endtime-starttime

testn = 3
at = []

for i in range(testn):
    at.append(runtest(216, 216, 1, 100))

print(f"Max: {max(at)}")
print(f"Min: {min(at)}")
print(f"Avg: {sum(at)/len(at)}")

