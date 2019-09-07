import heapq

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.dist = -1
        self.edges = []
        self.visited = False
        self.pot = False
    def set_dist(self, new_dist, heap):
        if new_dist > self.dist:
            self.dist = new_dist
    def __lt__(self, other):
        return self.dist > other.dist
class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    def get_next_node(self, node):
        if self.node1 == node:
            return self.node2
        return self.node1
def add_data():
    num_nodes, num_edges = [ int(x) for x in input().split()]
    nodes = []
    edges = []
    for i in range(num_nodes):
        nodes.append(Node(i))
    for i in range(num_edges):
        node1, node2, weight = input().split()
        edges.append(Edge(nodes[int(node1)], nodes[int(node2)], float(weight)))
        nodes[int(node1)].edges.append(edges[i])
        nodes[int(node2)].edges.append(edges[i])
    return (nodes, edges)
def print_order(nodes):
    heap = []
    for node in nodes:
        heapq.heappush(heap, node)
    while len(heap) != 0:
        node = heapq.heappop(heap)
        print(node.dist) 
def dijkstra(nodes, edges):
    last_node = nodes[len(nodes)-1]
    cur_node = nodes[0]
    cur_node.dist = 1
    pot_nodes = []
    pot_nodes.append(cur_node)
    while len(pot_nodes) != 0 and pot_nodes[0] != last_node:
        cur_node = heapq.heappop(pot_nodes)
        cur_node.visited = True
        for edge in cur_node.edges:
            new_node = edge.get_next_node(cur_node)
            if not new_node.visited:
                new_node.set_dist(edge.weight * cur_node.dist, pot_nodes)
                heapq.heappush(pot_nodes, new_node)
    return last_node.dist
if __name__ == "__main__":
    nodes, edges = add_data()
    while len(nodes) != 0 and len(edges) != 0:
        print("%.4f" % dijkstra(nodes, edges))
        nodes, edges = add_data()