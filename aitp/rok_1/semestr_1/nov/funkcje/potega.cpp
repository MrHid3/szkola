#include<iostream>

using namespace std;

long potega(int a, int b){
    if (b!=0){
        return a*potega(a,b-1);
    }
    else {
        return 1;
    }
}

int main(){
    int a,b;
    cout << "Hello adventurer, what's a?" << endl;
    cin >> a;
    cout << "And b?" << endl;
    cin >> b;
    cout << potega(a,b);
}
