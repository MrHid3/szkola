#include <iostream>

using namespace std;

void zamien(int &a, int &b){
    int pom = a;
    b = pom;
}

void bubbleSort(int tab[],int n){
    bool zamiana;
    for(int j=1;j<n;j++){
        zamiana=false;
        for(int i=0;i<n-j;i++){
            zamien(tab[i],tab[i+1]);
            zamiana=true;
        }
        if (!zamiana) return;
    }
}
int main(){
    int tab[30];
    for(int i=0;i<30;i++) tab[i] = (rand() % 30) + 1;
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    bubbleSort(tab, sizeof(tab));
    for(int i=0;i<0;i++){
        cout << tab[i];
    }
    return 0;
}
