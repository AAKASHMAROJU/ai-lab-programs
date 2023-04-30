# Mini Max Algorithm 
import math

def minimax(currDepth,currIdx,maxTurn,scores,targetDepth):
    if currDepth == targetDepth:
        return scores[currIdx]
    if maxTurn:
        return max(minimax(currDepth+1,2*currIdx,False,scores,targetDepth),minimax(currDepth+1,2*currIdx+1,False,scores,targetDepth))
    else:
        return min((minimax(currDepth+1,2*currIdx,True,scores,targetDepth),minimax(currDepth+1,2*currIdx+1,True,scores,targetDepth)))

print("Enter the Elements : ")
scores = list(map(int,input().split()))
targetDepth=math.log(len(scores),2)
print(minimax(0,0,True,scores,targetDepth))