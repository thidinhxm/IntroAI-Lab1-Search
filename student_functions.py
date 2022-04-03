from queue import PriorityQueue, Queue
import queue
import numpy as np


def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
    path=[]
    visited={}
    visited[start]= start

    stack = [start]
    while True:
        if len(stack) == 0:
            return visited, path
        node = stack.pop()
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                visited[i] = node
                stack.insert(0, i)
                
    
    cur = end
    while cur != start:
        path.append(cur)
        cur = visited[cur]
    path.append(start)
    path.reverse()

    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    visited[start]= start
    queue = Queue()
    queue.put(start)
 
    while True:
        if queue.empty():
            return visited, path

        node = queue.get()
        if node == end:
            break
        for i in range(len(matrix[node])):
            if matrix[node][i] != 0 and i not in visited:
                visited[i] = node
                queue.put(i)
    
    cur = end
    while cur != start:
        path.append(cur)
        cur = visited[cur]
    path.append(start)
    path.reverse()
    return visited, path
    

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:  
    path=[]
    visited={}
    visited[start]= start
    queue = PriorityQueue() # PriorityQueue is a queue that sorts items by a given key (cost) function.
    queue.put((0, start))
    closed = []
    while True:
        if queue.empty(): # if queue is empty, no path is found
            return visited, path

        node = queue.get() # get the node with the lowest cost
        # print('GET', node)
        if (node[1] in closed): # if node is in closed list, ignore it
            continue

        closed.append(node[1]) # add node to closed list
        if node[1] == end: # if node is the end node, break
            break
        for i in range(len(matrix[node[1]])):
            if matrix[node[1]][i] != 0: # if node has adjacent nodes
                if i not in closed: # if adjacent node is not in closed list
                    check = True # check if can add adjacent node to queue
                    for item in queue.queue:
                        if item[1] == i and item[0] < node[0] + matrix[node[1]][i]: # if adjacent node is in queue and cost is lower than current cost
                            check = False
                            break
                    if check == True:
                        queue.put((node[0] + matrix[node[1]][i], i)) # add adjacent node to queue
                        # print('PUT', (node[0] + matrix[node[1]][i], i))
                        visited[i] = node[1]
            # print('visited', visited)
    
    cur = end
    while cur != start:
        path.append(cur)
        cur = visited[cur]
    path.append(start)
    path.reverse()
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}

    queue = PriorityQueue() # h = edge weights
    queue.put((0, start))
    visited[start]= start

    while True:
        if queue.empty():
            return visited, path

        node = queue.get()
        # print('GET', node)
        if node[1] == end:
            break
        for i in range(len(matrix[node[1]])):
            if matrix[node[1]][i] != 0 and i not in visited:
                visited[i] = node[1]
                queue.put((matrix[node[1]][i], i))
                # print('PUT', (matrix[node[1]][i], i))
            # print('visited', visited)
    cur = end
    while cur != start:
        path.append(cur)
        cur = visited[cur]
    path.append(start)
    path.reverse()

    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

# references
# https://gist.github.com/professormahi/cff4bfeaece05966e688658127bf41f3
# https://stackoverflow.com/questions/46223338/check-if-element-exists-in-priorityqueue-of-tuples
# https://likegeeks.com/python-priority-queue/
# https://en.wikipedia.org/wiki/Best-first_search