#include <stdio.h>
#include <stdlib.h>
#define LENGTH 6
struct node {
    int index;
    int cost;
    int h;
    int visited;
    int parent;
};

int graph[LENGTH][LENGTH] = {
    { 10, 1, 2, -1, -1, -1},//0
    { 1, 8, -1, 2, -1, -1},//1
    { 2, -1, 8, 1, -1, -1},//2
    { -1, 2, 1, 5, 3, -1},//3
    { -1, -1, -1, 3, 3, 1},//4
    { -1, -1, -1, -1, 1, 0},//5
};

struct node list[LENGTH];

void moveNodeToStart(int index) {
    struct node temp = list[index];
    int i;
    for ( i = index; i > 0; i--) list[i] = list[i-1];
    list[0] = temp;
}
int returnMinF_Value_Index(){
    int min = 100000,i;
    int minI = -1;
    for( i =0;i<LENGTH;i++){
        if(list[i].index == -1 || list[i].visited == 1) continue;
        if(list[i].cost + list[i].h < min){
            minI = i;
            min = list[i].cost + list[i].h;
        }
    }
    return minI;
}
int includes(int index){
	int i;
    for( i =0;i<LENGTH;i++) if(list[i].index == index) return i;
    return -1;
}
int returnFirstNegativeIndex(){
	int i;
    for( i =0;i<LENGTH;i++) if(list[i].index == -1) return i;
    return -1;
}

void Astar(int s,int e){
    list[0].index = s;
    list[0].cost = 0;
    list[0].h = graph[0][0];
    list[0].visited = 0;
    while (1){
        if(list[0].index == e) break;
        int minF = returnMinF_Value_Index();
        moveNodeToStart(minF);
        list[0].visited = 1;
        int i;
        for(i =0;i<LENGTH;i++){
            if(graph[list[0].index][i] == -1 || list[0].index == i) continue;
            int indexOfI = includes(i);
            if(indexOfI == -1){
                int curr = returnFirstNegativeIndex();
                list[curr].index = i;
                list[curr].cost = list[0].cost + graph[list[0].index][i];
                list[curr].parent = list[0].index;
            }else{
                if(list[indexOfI].cost > list[0].cost + graph[list[0].index][i]){
                    list[indexOfI].cost = list[0].cost + graph[list[0].index][i];
                    list[indexOfI].parent = list[0].index;
                }
            }
        }
    }
    int currIndex = e;
    while (currIndex != s){
        int listIndex = includes(currIndex);
        printf("%d\t",list[listIndex].index);
        currIndex = list[listIndex].parent;
    }
    int listIndex = includes(s);
    int endIndex = includes(e);
    printf("%d\tCOST=%d\t\n",list[listIndex].index,list[endIndex].cost);
}
void main(){
    int startI = 0, endI = 5,i;
    printf("\n");
    printf("Graph Representation:\n");
    for (i = 0; i < LENGTH; i++) {
        for (int j = 0; j < LENGTH; j++) {
            printf("%2d ", graph[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    printf("Path:\n");
    for (i = 0; i < LENGTH; i++) {
        list[i].index = -1;
        list[i].cost = 0;
        list[i].h = 0;
        list[i].visited = 0;
        list[i].parent = -1;
    }
    Astar(startI,endI);
    printf("\n");
}
