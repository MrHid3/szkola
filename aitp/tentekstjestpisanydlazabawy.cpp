#include<iostream>

using namespace std;

int main (){
    int ile;
    bool flaga=true;
    do{
        cout<<"Ten tekst jest pisany dla zabawy"<<endl;
        if(flaga){
            cout<<"ile razy powinienem wypisaæ ten tekst?";
            cin >> ile;
            flaga=false;
        }
    ile--;
    } while(ile>=0);

    return 0;
}
