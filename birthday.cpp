#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

static int count;

class Edge
{
public:
    int node1;
    int node2;

    Edge(int node1, int node2)
    {
        this->node1 = node1;
        this->node2 = node2;
    }

    int get_next_node(int node)
    {
        if( node == this->node1 )
        {
            return this->node2;
        }
        return this->node1;
    }



};


class Node
{
public:
    int idx;
    bool visited;
    vector<Edge *> edges;

    Node()
    {
        this->idx = count;
        this->visited = false;
        count++;
    }

};

void printNodes(Node nodes[], int people)
{
    for(int i=0; i<people; i++)
    {
        cout<<nodes[i].idx<<" ";
    }
    cout<<endl;
}

void free_edges(vector<Edge *> edges)
{
    while(edges.size()>0)
    {
        free(edges[0]);
        edges.erase(edges.begin());
    }
}

void reset_nodes(Node nodes[], int people)
{
    for(int i=0; i<people; i++)
    {
        Node *temp = &nodes[i];
        temp->visited = false;
    }
}
void add_data(Node nodes[], int connections, vector<Edge*> &edges)
{
    int node1, node2;
    for( int i=0; i<connections; i++)
    {
        cin>>node1>>node2;
        Edge *e = new Edge(node1, node2);
        edges.push_back(e);
        nodes[node1].edges.push_back(e);
        nodes[node2].edges.push_back(e);
    }

}

bool BFS(Node nodes[], int people, int connections, Edge *bad_edge)
{
    vector<Node> queue;
    queue.push_back(nodes[0]);
    int visited_nodes = 0;
    nodes[0].visited = true;
    vector<Edge*> edges;
    while(queue.size()>0)
    {
        Node cur_node = queue[0];
        queue.erase(queue.begin());
        visited_nodes +=1;

        for(int i=0; i<cur_node.edges.size(); i++)
        {
            Edge *cur_edge = cur_node.edges[i];
            Node *next_node = &nodes[cur_edge->get_next_node(cur_node.idx)];
            if( !next_node->visited && cur_edge != bad_edge)
            {
                queue.push_back(*next_node);
                next_node->visited = true;
            }

        }
    }
    return visited_nodes == people;
}


string do_it()
{
    int people, connections;
    cin>>people>>connections;
    if( connections == 0 && people == 0 )
    {
        return "";
    }
    Node nodes[people] ={};
    vector<Edge*> edges;
    add_data(nodes, connections, edges);

    bool result;

    for(int i=0; i<edges.size(); i++)
    {
        result = BFS(nodes, people, connections, edges[i]);
        if( !result )
        {
            return "Yes";
            cout<<endl<<endl;
        }
        reset_nodes(nodes, people);

    }
    free_edges(edges);

    return "No";

}


int main()
{
    string ans = do_it();
    while(ans.length()!=0)
    {
        cout<<ans<<endl;
        count=0;
        ans=do_it();
    }

    return 0;
}