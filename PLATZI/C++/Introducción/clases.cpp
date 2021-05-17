#include <iostream>

using namespace std;

class cat {
      public:
    string Name;

    cat()
    {
        Name = "guapo";
    }
    cat(string iName)
    {
        Name = iName;
    }

    void Meow ()
    {
        cout << Name << " Dice meow" << endl;
    }

};

int main()
{
    cat MyFirstKytty;
    cat MySecondKytty("Toriel");

    MyFirstKytty.Meow();

    for (int i = 0; i < 3; i++)
    {
        MySecondKytty.Meow();
    }

    return 0;
}
