#include <iostream>

using namespace std;

void DrawMap(int HeroPos, char GameMap[5]) {
    for(int i = 0; i < 5; i++) {
        if (i != HeroPos)
        {
            cout << map[i];
        } else {
            cout << 'H';
        }

    }
}

int main () {
    int HeroPos = 0;
    bool isGameOver = false;
    char Input = '';
    char GameMap[5] = {'1', '1','1', '1','1'};

    while (isGameOver == false)
    {
        cin >> Input;

        if(Input == 'd')
        {
            HeroPos = HeroPos + 1;
        } else if(Input == 'a') {
            HeroPos = HeroPos - 1;
        } else if(Input == 'p') {
            isGameOver = true;
        }

        DrawMap(HeroPos, GameMap);
    }




    return 0;
}
