#include <iostream>
#include <fstream>

using namespace std;

int main () {

    ofstream MyFile("GameData.txt");
    string PlayerName = "";

    if(MyFile.is_open())
    {
        MyFile << "Hola Platzi !" << endl;
        MyFile << "Mi nombre es: " << endl;

        cout << "Introduce el nombre de tu heroe:" << endl;
        cin >> PlayerName;
        MyFile << PlayerName;
    }

    MyFile.close();

    ifstream MyFileRead("GameData.txt");
    string line;
    string NombreDelHeroe = "";
    int Renglon = 0;

    if(MyFileRead.is_open())
    {
        while(getline(MyFileRead,line) ) {

            if (Renglon == 2) {
                NombreDelHeroe = line;
            }

            Renglon = Renglon + 1;
        }
    } else {
        cout << "No logre abrir el archivo" << endl;
    }

    cout << "Bienvenida a tu aventura: " << endl;
    cout << NombreDelHeroe << endl;

    return 0;
}
