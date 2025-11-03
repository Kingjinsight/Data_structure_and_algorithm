# Here is undirected Graph is consist by dictionary and lists.
import undirected_graph
V = ['a','b','c','d','e','f','g','h'] 
E = [['b','e'], ['a','c'],['b','d','f','g','h'],['c','g'],['a','f','g'],['b','e','c'],['c','d','e','h'],['c','g']] 
graph = undirected_graph.Undirected_Graph(V,E)

class DFS():
    def __init__(self,G):
        self.visited = [False] * len(G.dictionary)
        self.stack = []
        self.test = []
        self.keys_list = list(G.dictionary.keys())
        for v in G.dictionary:
            index = self.keys_list.index(v)
            if self.visited[index] == False:
                self.dfsFromVertex(G,v)
    
    def dfsFromVertex(self,G,v):
        self.stack.append(v)
        while self.stack:
            print(self.stack)
            u = self.stack.pop()
            if self.visited[self.keys_list.index(u)] == False:
                self.visited[self.keys_list.index(u)] = True
                self.test.append(u)
                for w in G.dictionary[u]:
                    if self.visited[self.keys_list.index(w)] == False:
                        self.stack.append(w)



dfs1 = DFS(graph).test
print(dfs1)
