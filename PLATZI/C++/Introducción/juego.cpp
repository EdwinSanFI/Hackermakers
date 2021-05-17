#include <iostream>
#include "Player.h"

using namespace std;

int main()
{
    bool isGameOver = false;

    Player Hero;

    cout << "Inicia el juego!!!" << endl;

    while(isGameOver == false)
    {
        Hero.CallInput();
    }

    return 0;
}
