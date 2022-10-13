#include<iostream>

using namespace std;

int main(){
    int a = 'A';
    cout<<a<<endl;

    char c;
    cout<<"Podaj jakieœ znaki: ";
    cin >> c;
    cout<<"Poda³eœ: "<<c;
    int ascii = c;
    cout<<endl<<"w ASCII: " <<ascii<<endl;

    c='4';
    int x = c - 48;
    ascii = c;

    cout<<"cyfra: " <<c<<" to w ASCII: " <<ascii<<endl;
    cout <<"po zmianie na liczbe: "<<x<<endl;
    c = 4;
    cout<<c<<endl;
    system("pause");
    return 0;

}
