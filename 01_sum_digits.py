def rec_sum(n):
    if n < 10:
        return n

    return (n % 10) + rec_sum(n // 10)

print(rec_sum(99))