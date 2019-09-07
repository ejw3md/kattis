import heapq

class Edge:
    def __init__(self, d, node1, node2):
        self.d = d
        self.node1 = node1
        self.node2 = node2
        self.added = False
    def next_node(self, cur_node):
        if cur_node == self.node1:
            return self.node2
        return self.node1
    def sum_items(self):
        return self.node1.items+self.node2.items
    def __lt__(self, other):
        if self.d == other.d:
            return self.sum_items() > other.sum_items()
        return self.d < other.d
    def __str__(self):
        return "distance: " + str(self.d) + " total items: " + str(self.sum_items())
def print_edges(edges):
    for i in range(len(edges)):
        print(edges[i])

def insertion(edges, new):
    inserted = False
    for i in range(len(edges)):
        if not new > edges[i]:
            inserted = True
            edges.insert(i, new)
            break
    if not inserted:
        edges.append(new)
class Node:
    def __init__(self, items, idx):
        self.items = items
        self.edges = []
        self.idx = idx
        self.prev = None
        self.dist = 100000000000000
        self.visited = False
        self.item_trail = items
    def add_edge(self, edge):
        self.edges.append(edge)
    def __lt__(self, other):
        if self.dist == other.dist:
            return self.item_trail>other.item_trail
        return self.dist<other.dist
    def has_one_edge(self):
        return len(self.edges) == 1
    def remove(self, edge):
        for i in range(len(self.edges)):
            if edge == self.edges[i]:
                self.edges.pop(i)
                break
    def add_edges_from_node(self, edges):
        for edge in self.edges:
            if not edge.added:
                edge.added = True
                heapq.heappush(edges, (edge, self))
    def set_tot_dist(self, dist, item):
        if self.dist == dist:
            self.item_trail=item+self.items
        elif self.dist>dist:
            self.dist = dist
            self.item_trail = item+self.items
    def __lt__(self, other):
        if self.dist == other.dist:
            return self.item_trail > other.item_trail
        return self.dist < other.dist
    def __str__(self):
        return "idx: " + str(self.idx) + " distance: " + str(self.dist) + " item_trail: " + str(self.item_trail)
def print_nodes(nodes):
    for node in nodes:
        print(node)
def add_data(nodes, edges):
    num_nodes = int(input())
    items = input().split()
    num_edges = int(input())
    for i in range(len(items)):
        nodes.append(Node(int(items[i]), i))
    for edge in range(num_edges):
        node1, node2, d = [int(x) for x in input().split()]
        e = Edge(d, nodes[node1-1], nodes[node2-1])
        nodes[node1-1].add_edge(e)
        nodes[node2-1].add_edge(e)

def prim(nodes):
    nodes_visited = [nodes[0]]
    nodes[0].visited = True
    cur_node = nodes[0]
    pos_edges = []
    min_tree = []
    cur_node.add_edges_from_node(pos_edges)
    while len(nodes_visited) != len(nodes):
        print("hellO")
        print_edges(pos_edges)
        new_edge, cur_node = heapq.heappop(pos_edges)
        print(new_edge)
        next_node = new_edge.next_node(cur_node)
        while next_node.visited:
            print("hsldfj")
            new_edge, next_node = heapq.heappop(pos_edges)
        new_edge.added = True
        next_node = new_edge.next_node(cur_node)
        next_node.visited = True
        heapq.heappush(min_tree, new_edge)
        nodes_visited.append(next_node)
        next_node.add_edges_from_node(pos_edges)
    return min_tree

def act_prim(nodes):
    nodes[0].visited = True
    nodes_visited = 1
    pos_edges = []
    min_tree = []
    cur_node =  nodes[0]
    cur_node.add_edges_from_node(pos_edges)
    while(nodes_visited != len(nodes)):
        new_edge, from_node = heapq.heappop(pos_edges)
        new_node = new_edge.next_node(from_node)
        while new_node.visited:
            new_edge, from_node = heapq.heappop(pos_edges)
        new_node.visited = True
        min_tree.append(new_edge)
        new_node.add_edges_from_node(pos_edges)
        nodes_visited+=1
    return min_tree
def print_order(nodes):
    while len(nodes)!=0:
        print(heapq.heappop(nodes))
def dijkstra(nodes, edges):
    pot_nodes = [nodes[0]]
    nodes[0].dist = 0
    while len(pot_nodes) != 0 and pot_nodes[0] != nodes[len(nodes)-1]:
        cur_node = heapq.heappop(pot_nodes)
        cur_node.visited = True
        for edge in cur_node.edges:
            next_node = edge.next_node(cur_node)
            if not next_node.visited:
                next_node.set_tot_dist(cur_node.dist + edge.d, cur_node.item_trail)
                if next_node not in pot_nodes:
                    heapq.heappush(pot_nodes, next_node)
    if len(pot_nodes) ==0:
        return -1
    return ( pot_nodes[0].dist, pot_nodes[0].item_trail)


nodes = []
edges = []
add_data(nodes, edges)
#print_edges(edges)
#edges = act_prim(nodes)
ans = dijkstra(nodes, edges)
if ans == -1:
    print("impossible")
else:
    print("%d %d" % (ans[0], ans[1]))
