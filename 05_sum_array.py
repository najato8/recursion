def sum_table(T):
    if len(T) == 0:
        return 0
    
    return T[0] + sum_table(T[1:])

T = [1,2,3,4]
print(sum_table(T))
D = []
print(sum_table(D))