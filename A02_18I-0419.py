
import sys
import queue


array = [[False for i in range(20)] for j in range(20)] #array to maintain visited points


def move_left(state):
    #print("Moving from ", state)
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexj not in [0] and new_state[indexi][indexj-1]==1:
        new_state[indexi][indexj]=1
        new_state[indexi][indexj-1]=2        
        return new_state
    else:
        return None
    
    


def move_right(state):
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexj not in [19] and new_state[indexi][indexj+1]==1:
        new_state[indexi][indexj]=1
        new_state[indexi][indexj+1]=2        
        return new_state
    else:
        return None


def move_up(state):
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexi not in [0] and new_state[indexi-1][indexj]==1:
        new_state[indexi][indexj]=1
        new_state[indexi-1][indexj]=2        
        return new_state
    else:
        return None


def move_down(state):
    
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexi not in [19] and new_state[indexi+1][indexj]==1:
        new_state[indexi][indexj]=1
        new_state[indexi+1][indexj]=2        
        return new_state
    else:
        return None


def create_node(state, parent, operator, depth):
    return Node(state, parent, operator, depth)


def expand_node(node,nodes,goal):
  expanded_nodes = []  
  global direct
 
  
  left = move_left(node.state)
  if left != None: #moving left is allowed from state
 
      x=create_node(left, node.state, "left", node.depth+1)
      for i, e in enumerate(left):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:          
        expanded_nodes.append(x) 

  right = move_right(node.state) 
  if right != None: #moving right is allowed from state
     
      x=create_node(right, node.state, "right", node.depth+1)
      #x.print()
      for i, e in enumerate(right):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:       
        expanded_nodes.append(x) 
  up = move_up(node.state)
  if up != None: #moving up is allowed from state

      x=create_node(up, node.state, "up", node.depth+1)
    
      for i, e in enumerate(up):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

      if array[indexi][indexj] != True: #if hasnt been visited before                    
        expanded_nodes.append(x) 

  down = move_down(node.state)
  if down != None: #moving down is allowed from state
    
      x=create_node(down, node.state, "down", node.depth+1)
      #x.print()
      for i, e in enumerate(down):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:
        expanded_nodes.append(x)   
      
  return expanded_nodes

def equals(a, b):
  isEqual=True
  for i in range (0,20):
    for j in range (0,20):
      if a[i][j]!=b[i][j]:
        isEqual=False
        return isEqual
  return isEqual


def gbfs(start, goal):

    nodes_expanded = 0
    global array
    array = [[False for i in range(20)] for j in range(20)]
    steps=0
    result=[None]
    matches=True
    closed=[]
    path=[]
    count=0
    open=queue.PriorityQueue(0)
      

    for i, e in enumerate(start):
          try:
              sy=e.index(2)
              sx=i               
          except ValueError:
              pass
    for i, e in enumerate(goal):
          try:
              gy=e.index(2)
              gx=i               
          except ValueError:
              pass

    h= manhattanDistance(sx, sy, gx, gy)

    open.put((h,count, create_node(start, None, None, 0)))

    while (open.empty()== False):
       
        
        currenth,tie, current_node=open.get()

        closed.append(current_node)

        for i, e in enumerate(current_node.state):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

        

        array[indexi][indexj] = True

        h=manhattanDistance(indexi, indexj, gx, gy)        


        if current_node.state == goal:
          #print("Result complete")
          print("***************************************")
          print("Direct Path Cost: ", current_node.depth)          
          return steps

        
        exp_ans = expand_node(current_node, list(open.queue),goal)
        steps+=1 
        if exp_ans == 0:
          return steps
        else:
          for node in exp_ans:
            if node.state==goal:
              print("***************************************")
              print("Direct Path Cost: ", node.depth)          
              return steps
            elif node not in closed:
              opens=list(open.queue)
              present=False
              for c,lol, n in opens:
                if node==n:
                  present=True
              if present==False:
                for i, e in enumerate(node.state):
                  try:
                      indexj=e.index(2)
                      indexi=i               
                  except ValueError:
                      pass
                man=manhattanDistance(indexi, indexj, gx, gy) 
                
                open.put((man, count, node))
                count+=1
        
               

def astar(start, goal):

    nodes_expanded = 0
    global array
    array = [[False for i in range(20)] for j in range(20)]
    steps=0
    result=[None]
    matches=True
    closed=[]
    path=[]
    count=0
    open=queue.PriorityQueue(0)
      

    for i, e in enumerate(start):
          try:
              sy=e.index(2)
              sx=i               
          except ValueError:
              pass
    for i, e in enumerate(goal):
          try:
              gy=e.index(2)
              gx=i               
          except ValueError:
              pass

    h= manhattanDistance(sx, sy, gx, gy)
    startnode=create_node(start, None, None, 0)
    startnode.h=h
    startnode.f=startnode.h+0
    goalnode=create_node(goal, None, None, 0)
    open.put((startnode.f,count, startnode))

    while open.empty()==False:

        currentf,tie, current_node=open.get()

        closed.append(current_node)

        for i, e in enumerate(current_node.state):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

        

        array[indexi][indexj] = True

        h=manhattanDistance(indexi, indexj, gx, gy)   


        if current_node.state == goal:
          #print("Result complete")
          print("***************************************")
          print("Direct Path Cost: ", current_node.depth)          
          return steps

        
        exp_ans = expand_node(current_node, list(open.queue),goal)

        if exp_ans == 0:
          return steps
        else:
          for node in exp_ans:
           if node not in closed:
             for i, e in enumerate(node.state):
                  try:
                      indexj=e.index(2)
                      indexi=i               
                  except ValueError:
                      pass
             man=manhattanDistance(indexi, indexj, gx, gy) 
             node.h=man
             node.g=1+current_node.g
             node.f=node.g+node.h

             opens=list(open.queue)
             present=False
             for c,lol, n in opens:
               if node.state==n.state:
                 present=True             
             if present==False:
                #print("Adding to open ", indexi, indexj)
                open.put((node.f, count, node))
                count+=1
           else:
             opens=list(open.queue)
             present=False
             for c,lol, n in opens:
              if node.state==n.state:
                present=True             
                new=1+current_node.g
                if (n.g > new):
                  n.g=new 

        
        steps+=1        

def In_Open(open, neighbor):
        
        for cost, tie, node in list(open.queue):
            if (neighbor.state == node.state and neighbor.f >= node.f):
                return False
        return True
class Node:
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth=depth
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    def __eq__(self, other):
            return self.state == other.state
    # Sort nodes
    def __lt__(self, other):
          return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.g))

    def print(self):
      print("State: ", self.state, "Parent: ", self.parent, "Operator: ", self.operator)
        
def print_array(a):
  for i in range (0,20):
        for j in range (0,20):
            print(a[i][j]," ", end = '')
        print("\n")

def manhattanDistance(cx, cy, gx, gy):
    h = abs (cx-gx) + abs (cy-gy)

    return h

def main():

    maze=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
          [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0],
          [0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1],
          [0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1],
          [0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,0,1],
          [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1],
          [0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1],
          [0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1],
          [0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,0],
          [0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,1],
          [0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0],
          [1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1],
          [0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0],
          [0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    startpoint="14,0"
    endpoint="12,19"
 
    starting_state= [row[:] for row in maze]
    indices=startpoint.split(",")
    starting_state[int(indices[0])][int(indices[1])]=2

    sx=int(indices[0])
    sy=int(indices[1])
   
    
   
    goal_state = [row[:] for row in maze]
    indices=endpoint.split(",")
    goal_state[int(indices[0])][int(indices[1])]=2

    gx=int(indices[0])
    gy=int(indices[1])    

    h = abs (sx-gx) + abs (sy-gy)
    
    
    print("_________    Printing start state _________")
    
    print_array(starting_state)

    print("_________    Printing goal state _________")

    print_array(goal_state)
    

    result = gbfs(starting_state, goal_state)
    print("ALgorithm Used= GBFS")
    print("No of Moves Utilized: ",result)

    print("***************************************")
    result = astar(starting_state, goal_state)
    print("ALgorithm Used=A*")
    print("No of Moves Utilized: ",result)
    print("***************************************")
     
   


if __name__ == "__main__":
    main()

