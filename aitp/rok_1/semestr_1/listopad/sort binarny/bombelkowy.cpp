#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;

int main(){
    int tab[30];
    int temp;
    for(int i=0;i<30;i++) tab[i] = (rand() % 30) + 1;
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    cout << endl;
    for(int i=0; i < 30-1; i++) for(int j=0; j<30-i; j++) if (tab[j] > tab[j+1]){
                temp = tab[j];
                tab[j] = tab[j+1];
                tab[j+1] = temp;
            }
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    return 0;
}
