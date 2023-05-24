#include <stdio.h>
#include <stdbool.h>

#define MAX_NODES 100

// Depth-first search function
void dfs(int graph[][MAX_NODES], bool visited[], int curr_node, int num_nodes) {
    // Mark the current node as visited
    visited[curr_node] = true;
    printf("%d ", curr_node);

    // Recur for all the neighbors of the current node
    for (int i = 0; i < num_nodes; i++) {
        if (graph[curr_node][i] && !visited[i]) {
            dfs(graph, visited, i, num_nodes);
        }
    }
}

int main() {
    // Create the graph as an adjacency matrix
	int graph[MAX_NODES][MAX_NODES] = {
	  {0, 1, 1, 0, 0, 0, 0},
	  {1, 0, 0, 0, 0, 0, 0},
	  {1, 0, 0, 1, 1, 0, 0},
	  {0, 0, 1, 0, 0, 1, 0},
	  {0, 0, 1, 0, 0, 0, 1},
	  {0, 0, 0, 1, 0, 0, 0},
	  {0, 0, 0, 0, 1, 0, 0}
	};

    int num_nodes = 7;
    bool visited[MAX_NODES] = {false};

    // Print the graph
    printf("Graph as an adjacency matrix:\n");
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < num_nodes; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }

    // Perform DFS traversal starting from node 0
    printf("\nDFS traversal starting from node 0:\n");
    dfs(graph, visited, 0, num_nodes);

    return 0;
}
