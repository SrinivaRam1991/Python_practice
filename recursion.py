def count_down(n):
    if n == 0:
        return n
    else:
        print(n)
    result = n + count_down(n-1)

    print(result)
    count_down(4)

