# Water Jug using dfs 

class Node:
    def __init__(self,state,parent):
        self.state=state
        self.parent=parent
    
    def child_nodes(self,capacity):
        a,b=self.state
        max_a,max_b=capacity
        children=[]
        children.append(Node((max_a,b),self))
        children.append(Node((a,max_b),self))
        children.append(Node((0,b),self))
        children.append(Node((a,0),self))
        if a+b >= max_b:
            children.append(Node((a+b-max_b,max_b),self))
        else:
            children.append(Node((0,a+b),self))
        if a+b>=max_a:
            children.append(Node((max_a,a+b-max_a),self))
        else:
            children.append(Node(((a+b),0),self))
        return children
    
def dfs(start_state,goal_state,capacity):
    start_node=Node((start_state),None)
    visited=set()
    stack=[start_node]
    while stack:
        node=stack.pop()
        if node.state==goal_state:
            path=[]
            while node.parent:
                path.append(node.state)
                node=node.parent
            path.append(start_state)
            path.reverse()
            return path
        if node.state not in visited:
            visited.add(node.state)
            for child in node.child_nodes(capacity):
                stack.append(child)

    

if __name__=="__main__":
    start_state=(0,0)
    a,b=map(int,input("Enter the Capacities of the Jugs : ").split())
    c,d=map(int,input("Enter the Final Goal State : ").split())
    goal_state=(c,d)
    capacity=(a,b)
    path=dfs(start_state,goal_state,capacity)
    print(path)
