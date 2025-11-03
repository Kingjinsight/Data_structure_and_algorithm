# consist by linked lists
class Undirected_Graph():
    def __init__(self, V:list, E:list[list]):
        self.dictionary = {}
        for i in range(len(V)):
            self.dictionary[V[i]]=E[i]

V = ['a','b','c','d','e','f','g,','h'] 
E = [['b','e'], ['a','c'],['b','d','f','g','h'],['c','g'],['a','f','g'],['b','e','c'],['c','d','e','h'],['c','g']] 
