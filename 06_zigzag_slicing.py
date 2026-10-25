def zigzag(T):

    for i , ligne in enumerate(T):
        if i % 2 == 0:
            print(ligne)
        else:
            print(ligne[::-1])

T = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
zigzag(T)