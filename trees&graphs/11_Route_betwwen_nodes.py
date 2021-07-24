from collections import defaultdict

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
        self.edges = []
  
    def generate_edges(self):    
        # for each node in graph
        for node in self.gdict:
            
            # for each neighbour node of a single node
            for neighbour in self.gdict[node]:
                
                # if edge exists then append
                self.edges.append((node, neighbour))
    
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

def find_route(g, start, end):
    # normal search
    queue = [start]
    visited = set([start])
    while len(queue)>0:
        current = queue.pop(0)
        for child in g[current]:
            if child not in visited:
                if child == end:
                    return True
                queue.append(child)
                visited.add(child)

    return False

def find_route_bi(g ,start, end):
    start_q = [start]
    end_q = [end]
    visited = set([start, end])
    while len(start_q)>0 and len(end_q):
        current1 = start_q.pop(0)
        current2 = end_q.pop(0)
        for child in g[current1]:
            if child in visited:
                return True
            start_q.append(child)
            visited.add(child)
        for child in g[current2]:
            if child in visited:
                return True
            end_q.append(child)
            visited.add(child)
    
    return False
 

            
            

g = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

print(find_route_bi(g, start = "a", end = "d"))

