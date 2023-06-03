from heapq import *
from itertools import combinations

# This solution models the problem as shortest path problem in a 
# matrix where the row is one string and the column is the other

# This code only works for 2 strings
# input format is followed, but limited to two strings only (k=2)

vocab_len = int(input())
vocab = input().split(', ')

k = int(input())
string_list = []
for i in range(0,k):
    string_list.append(input()) 

cc = int(input())

mc = list()
for i in range(0,vocab_len+1):
    mc.append(input().split())

#  mc format
#   0 1 2 3 4
#   A C T G -
# A 0       1
# C   0   * 1
# T     0   1
# G  *    0 1
# - 1 1 1 1 0


# node stores the current position in matrix as well as the 2 strings
class Node:
    def __init__(self, parent, pos, str1, str2, cost) -> None:
        self.parent = parent
        self.pos = pos
        self.str1 = [*str1] # horizontal
        self.str2 = [*str2] # vertical
        self.cost = cost

    def __lt__(self, nxt):
        return self.cost < nxt.cost

# this function returns a list of next positions
def succ(x):
    ls = []
    # heuristic can be added using a lowest pythagorean distance scheme
    # distance = (len(x.str1)-x.pos[0]) + (len(x.str2)-x.pos[1])
    distance = 0

    # diagonal move
    if (x.pos[0]<len(x.str1)) and (x.pos[1]< len(x.str2)):
        new_pos = list([x.pos[0]+1, x.pos[1]+1])
        ls.append(Node(x,new_pos,x.str1,x.str2,x.cost+2+distance))
        if (x.str1[x.pos[0]] == x.str2[x.pos[1]]):
            new_pos = list([x.pos[0]+1, x.pos[1]+1])
            ls.append(Node(x,new_pos,x.str1,x.str2,x.cost+distance))
    
    # horizontal move
    if x.pos[0] < len(x.str1):
        new_pos = list([x.pos[0]+1,x.pos[1]])
        new_cost = x.cost + 1 + distance
        ls.append(Node(x,new_pos,x.str1,x.str2,new_cost))

    # vertical move
    if x.pos[1] < len(x.str2):
        new_pos = list([x.pos[0],x.pos[1]+1])
        new_cost = x.cost + 1 + distance
        ls.append(Node(x,new_pos,x.str1,x.str2,new_cost))

    return ls

# priority queue for best first search
class priority_queue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        if not self.heap:
            return True
        else:
            return False

# function that returns the shortest path
def soln(nd):
    ls = []
    while nd.parent:
        ls.append(nd.pos)
        nd = nd.parent
    ls.append([0,0])
    ls.reverse()
    return ls

# utility function to find previous action
def comp(pos1, pos2):
    if pos1[1] == pos2[1]:
        return 1
    elif pos1[0] == pos2[0]:
        return 2
    else:
        return 3

# function to print the final conversioin
def output(str1, str2, path):
    str1 = [*str1]
    str2 = [*str2]
    cost = 0
    for idx, ele in enumerate(path):
        if idx < len(path)-1:
            if comp(path[idx],path[idx+1]) == 1:
                str2.insert(idx,'-')
                cost += 3
            if comp(path[idx],path[idx+1]) == 2:
                str1.insert(idx,'-')
                cost += 3

    string1 = ''.join(str1)
    string2 = ''.join(str2)

    print('conversion with lowest cost is:')
    print(string1)
    print(string2)
    print('cost of conversion:')
    print(cost) 

# search function 
# solve(horizontal,vertical)
def solve(str1, str2):
    pq = priority_queue()

    tini = [0,0]
    initial = tuple(x for x in tini)
    root = Node(None, initial, str1, str2, 0)
 
    pq.push(root)
  
    while not pq.empty():
        min = pq.pop()
        # If min is the answer node
        if min.pos[0] == len(min.str1) and min.pos[1] == len(min.str2):
            pt = soln(min)
            output(str1, str2, pt)
            return
  
        # Produce all possible children
        children = succ(min)
        for x in children:
            pq.push(x)

# string1 = str(input('Enter string 1\n'))
# string2 = str(input('Enter string 2\n'))
# print()


solve(string_list[0], string_list[1])
