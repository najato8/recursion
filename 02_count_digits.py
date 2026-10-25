def count_number(n):
    if n < 10:
        return 1

    return 1 + count_number(n // 10)

#print(count_number(1234)) #4
#print(count_number(5))
print(count_number(0))