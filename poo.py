def triangle(n):
    m = 0
    r = 1
    while m <= n:
        print(m)
        m += r
        r += 1
limit = int(input("Limit: "))

triangle(limit)