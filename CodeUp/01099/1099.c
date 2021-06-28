#include <stdio.h>

int main(){
    int maze[10][10], row = 1, col = 1;

    for(int i = 0; i < 10; i ++){
        for(int j = 0; j < 10; j ++){
            scanf("%d", &maze[i][j]);
        }
    }

    while(1){
        if(maze[row][col] == 2 || maze[row + 1][col] == 1 && maze[row][col + 1] == 1){
            maze[row][col] = 9;
            break;
        }

        maze[row][col] = 9;

        if(maze[row][col + 1] != 1) col += 1;
        else row += 1;
    }

    for(int i = 0; i < 10; i ++){
        for(int j = 0; j < 10; j ++){
            printf("%d ", maze[i][j]);
        }
        printf("\n");
    }

    return 0;
}