#include <iostream>

using namespace std;

void quicksort(int l, int p, int tab[]){
    int i=l, j=p;
    int pivot=tab[(l+p)/2];
    do{
        while(tab[i]<pivot) i++;
        while(tab[j]>pivot) j--;
        if(i<=j){
            int tmp = tab[i];
            tab[i] = tab[j];
            tab[j] = tmp;
            i++;j--;    
        }
    }while(i<=j);
    if(l<j) quicksort(l,j,tab);
    if(i<p) quicksort(i,p,tab);
}
int main(){
    int tab[30];
    for(int i=0;i<30;i++) tab[i] = (rand() % 30) + 1;
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    cout << endl;
    int p = 0;
    int k = 30-1;
    quicksort(p,k,tab);
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
}