# Here is undirected Graph is consist by dictionary and lists.
import undirected_graph
V = ['a','b','c','d','e','f','g','h'] 
E = [['b','e'], ['a','c'],['b','d','f','g','h'],['c','g'],['a','f','g'],['b','e','c'],['c','d','e','h'],['c','g']] 
graph = undirected_graph.Undirected_Graph(V,E)

class BFS():
    def __init__(self,G):
        self.visited = [False] * len(G.dictionary)
        self.queue = []
        self.test = []
        self.keys_list = list(G.dictionary.keys())
        for v in G.dictionary:
            index = self.keys_list.index(v)
            if self.visited[index] == False:
                self.bfsFromVertex(G,v)
    
    def bfsFromVertex(self,G,v):
        self.visited[self.keys_list.index(v)] = True
        self.queue.append(v)
        while self.queue:
            v = self.queue.pop(0)
            self.test.append(v)
            for w in G.dictionary[v]:
                if self.visited[self.keys_list.index(w)] == False:
                    self.visited[self.keys_list.index(w)] = True
                    self.queue.append(w)



bfs1 = BFS(graph).test
print(bfs1)
