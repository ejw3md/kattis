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
        self.item_trail = 0
        self.pot = False
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
        if self.dist>dist:
            self.dist = dist
            self.item_trail=item
        elif self.dist == dist:
            if self.item_trail<item:
                self.item_trail = item
    def __lt__(self, other):
        if self.dist == other.dist:
            return self.item_trail > other.item_trail
        return self.dist < other.dist

                
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

def dijkstra(nodes, edges):
    pot_nodes = [nodes[0]]
    nodes[0].dist = 0
    nodes[0].item_trail = nodes[0].items
    while len(pot_nodes) != 0 and pot_nodes[0] != nodes[len(nodes)-1]:
        cur_node = heapq.heappop(pot_nodes)
        cur_node.visited = True
        for edge in cur_node.edges:
            next_node = edge.next_node(cur_node)
            if not next_node.visited:
                if next_node == nodes[len(nodes)-1]:
                    next_node.set_tot_dist(cur_node.dist + edge.d, cur_node.item_trail)
                else:
                    next_node.set_tot_dist(cur_node.dist + edge.d, cur_node.item_trail + next_node.items)
                if next_node.pot and len(pot_nodes)>50:
                    pot_nodes.pop()
                heapq.heappush(pot_nodes, next_node)
                next_node.pot = True

    if len(pot_nodes) != 0:
        return "" + str(pot_nodes[0].dist) + " " + str(pot_nodes[0].item_trail + nodes[len(nodes)-1].items)
    else:
        return "impossible"

        
nodes = []
edges = []
add_data(nodes, edges)
#print_edges(edges)
#edges = act_prim(nodes)
print(dijkstra(nodes, edges))