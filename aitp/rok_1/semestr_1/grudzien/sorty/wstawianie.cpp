#include <iostream>
#include<cstdlib>

using namespace std;

int sorting(int tab[], int n){
    int i;
    for (int k=1;k<n;k++){
        i=k;
        int temp=tab[i];
        while(i>0){
            if(temp<tab[i-1]){
                tab[i]=tab[i-1];
                tab[i-1]=temp;
            }
            i--;
        }
    }
    return 0;
}
int main(){
    int tab[30];
    for(int i=0;i<30;i++) tab[i] = (rand() % 30) + 1;
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    cout << endl;
    sorting(tab, 30);
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    return 0;
}
