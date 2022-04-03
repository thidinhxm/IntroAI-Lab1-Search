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
    queue = PriorityQueue()
    queue.put((0, start))
    closed = []
    while True:
        if queue.empty():
            return visited, path

        node = queue.get()
        print('GET', node)
        if (node[1] in closed):
            continue
        closed.append(node[1])
        if node[1] == end:
            break
        for i in range(len(matrix[node[1]])):
            if matrix[node[1]][i] != 0:
                if i not in closed:
                    visited[i] = node[1]
                    queue.put((matrix[node[1]][i] + node[0], i))
                    print('PUT', (matrix[node[1]][i] + node[0], i))
                elif matrix[node[1]][i] + node[0] < queue.queue[-1][0]:
                    queue.put((matrix[node[1]][i] + node[0], i))
                    print('PUT', (matrix[node[1]][i] + node[0], i))
    
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

