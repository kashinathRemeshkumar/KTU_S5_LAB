class Node:
    def __init__(self,name,heuristics):
        self.name=name
        self.heuristics=heuristics
        self.neighbors={}
    
    def add_neighbour(self,neighbor,cost):
        self.neighbors[neighbor]=cost

    
def best_first_search(start,goal):
    open_list=[start]
    closed_list=[]

    while open_list:
        current_node=min(open_list,key=lambda node:node.heuristics)
        open_list.remove(current_node)
        print(f"expanding node {current_node.name}")

        if current_node==goal:
            print("goal reached ")
            return
        if current_node not in closed_list:
            closed_list.append(current_node)

            for neighbour in current_node.neighbors:
                if neighbour in closed_list or open_list:
                    continue
            open_list.append(neighbour)
                
    print("goal not found")

a=Node('A',5)
b=Node('B',3)
c=Node('C',2)
d=Node('D',1)
e=Node('E',0)

a.add_neighbour(b,1)
a.add_neighbour(c,1)
b.add_neighbour(d,3)
c.add_neighbour(e,2)

best_first_search(a,e)
            

