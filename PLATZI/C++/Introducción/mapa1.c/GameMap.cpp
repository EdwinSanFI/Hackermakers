#include "GameMap.h"
#include "Player.h"

using namespace std;

GameMap::GameMap()
{
    PlayerCell = NULL;
}

void GameMap::Draw ()
{
    for (int i = 0, i < 15; i = i + 1)
    {
        for (int p = 0, p < 10; p = p + 1)
        {
            cout << 0;
        }
        cout << cells[i][p].id;
    }
}

void GameMap::SetPlayerCell(int PlayerX, int PlayerY)
{
    if (PlayerCell != NULL)
    {
        PlayerCell->id = 0;
    }

    PlayerCell = &cells[PlayerX][PlayerY];
    PlayerCell->id = 3;
    //cout << "Las coordenadas del jugador estan en: "<< Player X << "," << PlayerY;
}
