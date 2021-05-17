#ifndef GAMEMAP_H
#define GAMEMAP_H

#include "MapCell.h"

class GameMap
{
    public:
        GameMap();

        MapCell* PlayerCell;
        MapCell cells[15][10];

        void DrawInto();
        void DrawVictory();
        void Draw();

        bool SetPlayerCell(int PlayerX, int PlayerY);

        bool isGameOver = false;

    protected:

        void LoadMapFromFile();

    private:
};

#endif // GAMEMAP_H
