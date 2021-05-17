#include <iostream>

using namespace std;

class Dog
{
public:
    string mBark;

    Dog(string Name, string BarkType)
    {
        mName = Name;
        mBark = BarkType;
    }

    string GetName() {
    return mName;
    }

    void SetName(string NewName)
    {
        mName = NewName;
    }

private:
    string mName;

};

int main ()
{
    Dog PerroUno("Woofers", "Berk");

    PerroUno.SetName("Poppy");

    cout << PerroUno.GetName() << endl;


    return 0;
}
