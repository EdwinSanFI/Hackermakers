#include <stdio.h>

void DrawMap(int HeroPos, char gameMap[5]) {
    for(int i = 0; i < 5; i++) {
        if (i != HeroPos)
        {
            printf("%char", gameMap);
        } else {
            printf("H");
        }
        
    }
}

int main () {
    int i; 
    int HeroPos = 0;
    bool isGameOver = false;
    char Input = ' ';
    char map[5] = {'1', '1','1', '1','1'};

    for (i = 0; i < 5; i++)
    {
        printf("%char", map);
    }
    
}