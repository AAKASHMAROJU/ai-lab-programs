def isPlace(i,j):
    for l in range(i):
        if x[l]==j or abs(l-i)==abs(x[l]-j):
            return False
    return True

def nQueens(curr_q,n):
    for col in range(n):
        if isPlace(curr_q,col):
            x[curr_q]=col
            if curr_q==n-1:
                print(*x)
            else:
                nQueens(curr_q+1,n)

n=int(input("Enter the Number of Queens : "))
x=[0 for i in range(n)]
nQueens(0,n)