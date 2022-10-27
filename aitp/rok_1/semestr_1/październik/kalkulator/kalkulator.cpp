#include <iostream>

using namespace std;

int main(){

    string d,z;
    float a,b,w;

    while (true){
        cout << "Hello adventurer, what's number a?" << endl;
        cin >> a;
        cout << "What operation do you wish to execute? (+,-,*,/,!,^)" << endl;
        cin >> d;

        if (d != "!"){
            cout << "What's number b?" << endl;
            cin >> b;
        }


        if (d == "+"){
            cout << a + b << endl;
        }
        else if (d == "-"){
            cout << a - b << endl;
        }
        else if (d == "*"){
            cout << a * b << endl;
        }
        else if (d == "/"){
            cout << a / b << endl;
        }
        else if (d == "!"){
            if (a != float(int(a))){
                cout << "My dear friend, factorial's arguments must be integers" << endl;
            }
            else if (a == 0){
                cout << 1 << endl;
            }
            else{
                w = a;
                for (int i = 1; i < a; i++){
                    w *= i;
                }
                cout << w << endl;
            }
        }
        else if (d == "^"){
            if (b != float(int(b))){
                cout << "My dear friend, exponents must be integers" << endl;
            }
            else if (a == float(0) and b == float(0)){
                cout << "unmarked symbol" << endl;
            }
            else if (b == float(0)){
                cout << 1 << endl;
            }
            else{
                w = a;
                for (int i = 1; i < b; i++)
                    w *= a;
                cout << w << endl;
            }
        }
        else {
            cout << "My dear friend, that is not an operation" << endl;
        }

        cout << "Do you wish to continue your adventure? [y/n]" << endl;
        cin >> z;
        if (z != "y"){
            break;
        }
    }
    return 0;
}
//JDJDJDJDJD
