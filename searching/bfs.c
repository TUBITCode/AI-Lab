#include <stdio.h>

#define MAX_NODES 100

// Perform BFS traversal of the graph
void bfs(int graph[][MAX_NODES], int num_nodes, int start) {
    // Initialize a queue to store nodes to visit
    int queue[MAX_NODES];
    int front = 0, rear = 0;
    
    // Initialize an array to keep track of visited nodes
    int visited[MAX_NODES] = { 0 };
    
    // Enqueue the starting node and mark it as visited
    queue[rear++] = start;
    visited[start] = 1;
    
    // Continue until all nodes have been visited
    while (front < rear) {
        // Dequeue the next node to visit
        int current = queue[front++];
        
        // Print the current node
        printf("%d ", current);
        
        // Enqueue all unvisited neighbors of the current node
        for (int i = 0; i < num_nodes; i++) {
            if (graph[current][i] && !visited[i]) {
                queue[rear++] = i;
                visited[i] = 1;
            }
        }
    }
}

int main() {
    // Define the graph as an adjacency matrix
    int num_nodes = 7;
	int graph[MAX_NODES][MAX_NODES] = {
	  {0, 1, 1, 0, 0, 0, 0},
	  {1, 0, 0, 0, 0, 0, 0},
	  {1, 0, 0, 1, 1, 0, 0},
	  {0, 0, 1, 0, 0, 1, 0},
	  {0, 0, 1, 0, 0, 0, 1},
	  {0, 0, 0, 1, 0, 0, 0},
	  {0, 0, 0, 0, 1, 0, 0}
	};
	
    // Print the graph
    printf("Graph representation as an adjacency matrix:\n");
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < num_nodes; j++) {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
    
    // Perform BFS traversal starting from node 0
    printf("\nBFS traversal starting from node 0:\n");
    bfs(graph, num_nodes, 0);
    
    return 0;
}
