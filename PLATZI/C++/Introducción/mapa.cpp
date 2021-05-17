#include <iostream>

using namespace std;

void DrawMap(int HeroPosX, int HeroPosY, char GameMap[5][5])
{
    for(int i = 0; i < 5; i++) {
            for(int p = 0; p < 5; p++) {
                if (i != HeroPosY)
                    {
                        cout << GameMap[p][i];
                    } else {
                        if(p != HeroPosX){
                            cout << GameMap[p][i];
                        } else{
                            cout << 'H';
                        }

                    }
            }
            cout << endl;
    }
}

int main () {
    int HeroPosX = 1;
    int HeroPosY = 1;
    bool isGameOver = false;
    char Input = ' ';
    char GameMap[5][5] = {
        {'1', '1','1', '1','1'},
        {'1', '1','1', '1','1'},
        {'1', '1','1', '1','1'},
        {'1', '1','1', '1','1'},
        {'1', '1','1', '1','1'}
    };

    DrawMap(HeroPosX, HeroPosY, GameMap);

    while (isGameOver == false)
    {
        cin >> Input;

        if(Input == 'd')
        {
            HeroPosX = HeroPosX + 1;
        } else if(Input == 'a') {
            HeroPosX = HeroPosX - 1;
        } else if(Input == 'p') {
            isGameOver = true;
        }

        DrawMap(HeroPosX, HeroPosY, GameMap);
    }




    return 0;
}
