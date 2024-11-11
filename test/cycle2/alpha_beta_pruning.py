Min,Max=-1000,1000


def min_max(tree,depth,maximizer,node,alpha,beta):
    if depth==3:
        return tree[node]
    
    if maximizer:
        best=Min
        for i in range(0,2):
            val=min_max(tree,depth+1,False,(node*2)+i,alpha,beta)
            best=max(best,val)
            alpha=max(best,alpha)

            if alpha>=beta:
                break
        return best

    else:
        best=Max
        for i in range(0,2):
            val=min_max(tree,depth+1,True,node*2+i,alpha,beta)
            best=min(val,best)
            beta=min(best,beta)

            if alpha>=beta:
                break
        return best
    
tree = [3, 5, 6, 9, 1, 2, 0, -1]
print(min_max(tree,0,True,0,Max,Min))