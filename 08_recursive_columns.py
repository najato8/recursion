def what(T ,i ,j):
    if (j >= 0):
        print(T[j][i])
        what(T,i,j-1)


T = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
what(T,0,len(T)-1)