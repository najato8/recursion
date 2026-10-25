def zigzag(T):

    i =0
    while (i < len(T)):
        if i % 2 == 0:
            j=0
            while (j < len(T[i])):
                print(T[i][j], end=" , ")
                j+=1
                
        else:
            j = len(T[i]) - 1
            while (j >= 0):
                print(T[i][j],end=" , ")
                j -=1
            
        print()
        i+=1
        

T = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
zigzag(T)