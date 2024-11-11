def is_safe(i,j):
    for k in range(n):
        if bord[i][k]==1 or bord[k][j]==1:
            return False
        
    for k in range(n):
        for l in range(n):
            if (k+l==i+j)or(k-l==i-j):
                if bord[k][l]==1:
                    return False
            
    return True

def n_queen(n):
    if n==0:
        return True
    else:
        for i in range(len(bord)):
            for j in range(len(bord)):
                if ((is_safe(i,j)) and (bord[i][j]!=1)):
                    bord[i][j]=1
                    if n_queen(n-1):
                        return True
                    bord[i][j]=0
        return False        


n=int(input("enter the number of queens"))

bord=[[0]*n for _ in range(n)]
n_queen(n)
for i in range(n):
    for j in range(n):
        print(bord[i][j],end="  ")
    print(end="\n")