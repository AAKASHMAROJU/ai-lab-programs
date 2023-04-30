import math
MAX=1000
MIN=-1000

def minimaxab(depth,idx,maxTurn,scores,alpha,beta,targetDepth):
    if depth==targetDepth:
        return scores[idx]
    if maxTurn:
        best=MIN
        for i in range(2):
            val=minimaxab(depth+1,2*idx+i,False,scores,alpha,beta,targetDepth)
            best=max(best,val)
            alpha=max(alpha,best)
            if alpha >= beta : 
                # print("Pruned it is ")
                break
        return best
    else:
        best=MAX
        for i in range(2):
            val=minimaxab(depth+1,2*idx+i,True,scores,alpha,beta,targetDepth)
            best=min(best,val)
            beta=min(beta,best)
            if alpha >= beta:
                # print("Pruned at min turn")
                break
        return best


scores=list(map(int,input().split()))
targetDepth = math.log(len(scores),2)
print(minimaxab(0,0,True,scores,MIN,MAX,targetDepth))