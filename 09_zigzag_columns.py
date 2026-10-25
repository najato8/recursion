def what_bas_haut(T ,i ,j):
    if (j >= 0):
        print(T[j][i], end=" ")
        what_bas_haut(T,i,j-1)

def what_haut_bas(T ,i ,j=0):
    if (j < len(T)):
        print(T[j][i], end=" ")
        what_haut_bas(T,i,j+1)


def haut_bas(T,i ):
    while(i<len(T)):

        if i % 2 == 0:
            what_haut_bas(T,i,0)
            
        else:
            what_bas_haut(T,i,len(T)-1)
            

        i +=1
        print()

T = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
haut_bas(T,0)
