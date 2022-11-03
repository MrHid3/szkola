#include <iostream>

using namespace std;

int nwd(int a, int b){
    if (b != 0){
        return nwd(b,a%b);
    }
    return a;
}

int main(){
    int a,b;
    cout << "Hello adventurer, what's number a?" << endl;
    cin >> a;
    cout << "And b?" << endl;
    cin >> b;
    cout << nwd(a,b);
    return 0;
}
