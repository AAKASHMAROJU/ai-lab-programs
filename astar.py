def aStarAlgo(start,stop):
    openset=set(start)
    closeset=set() 
    g={} # dist from start
    parent={}
    parent[start]=start
    g[start]=0
    while len(openset) > 0:
        n=None
        for v in openset:
            if n==None or g[v]+Heuristic(v)<g[n]+Heuristic(n):
                n=v
        if n==stop or Graph_nodes[n]==None:
            pass
        else:
            for (m,wt) in get_neighbors(n):
                if m not in openset and m not in closeset:
                    openset.add(m)
                    parent[m]=n
                    g[m]=g[n]+wt
                else:
                    if g[m] > g[n]+wt:
                        g[m]=g[n]+wt
                        parent[m]=n
                        if m in closeset:
                            closeset.remove(m)
                            openset.add(m)


        if n==None:
            print("Path Does not Exist")
            return None
        if n==stop:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print(path)
            return path
        openset.remove(n)
        closeset.add(n)

    print("Path Doesn't Exist ")
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
    

def Heuristic(n):
    H={
        'A':11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0
    }
    return H[n]

Graph_nodes={
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    'C':None,
    'D':[('G',1)],
    'E':[('D',6)]
}

aStarAlgo('A','G')