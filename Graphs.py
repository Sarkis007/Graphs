class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.visited = "no"

    def add_neighbor(self, data):
        if data not in self.neighbors:
            self.neighbors.append(data)



class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex


    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    def bfs(self, vert):
        q = list()
        vert.visited = 'yes'
        for v in vert.neighbors:
            q.append(v)
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.visited = 'yes'
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.visited == 'no':
                    q.append(v)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

    def printvisited(self):
        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].visited is "yes":
                print(key)

    def dfs(self, vert):
        vert.visited = 'yes'
        for v in vert.neighbors:
            if self.vertices[v].visited == "no":
                self.dfs(self.vertices[v])
        vert.visited = "yes"

def addpeople():

    g = Graph()
    while True:
        name1 = raw_input("please enter first person name")
        name1vert = Vertex(name1)
        g.add_vertex(name1vert)
        name2 = raw_input("please enter second person name")
        name2vert = Vertex(name2)
        g.add_vertex(name2vert)
        x = raw_input("Are they relatives ?")
        if x == "yes":
            g.add_edge(name1, name2)
        elif x == "no":
            pass
        y = raw_input("Do you want to add other people ?")
        if y == "no":
            g.print_graph()
            print "You see it WORKS :D"
            exit()
        else:
            pass







def main():
    print"Hi Satenik, what you want to check ?? "
    print "1- BFS"
    print "2- DFS"
    print "3- Adding people"
    print "please enter 1 , 2 or 3"
    x = raw_input()
    g = ""
    a = ""
    if x == "1" or x == "2":
        g = Graph()
        a = Vertex('1')
        b = Vertex('2')
        c = Vertex('3')
        d = Vertex('4')
        e = Vertex('5')

        g.add_vertex(a)
        g.add_vertex(b)
        g.add_vertex(c)
        g.add_vertex(d)
        g.add_vertex(e)

        g.add_edge('1', '2')
        g.add_edge('3', '2')
        g.add_edge('1', '3')
        g.add_edge('1', '5')
    if x == "2":
        g.dfs(a)
        g.printvisited()
        print "You see it WORKS :D"

    elif x == "1":
        g.bfs(a)
        g.printvisited()
        print "You see it WORKS :D"

    elif x == "3":
        addpeople()
        print "You see it WORKS :D"

main()