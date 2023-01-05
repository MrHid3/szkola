#include <iostream>

using namespace std;

void merge(int start, int middle, int end, int tab[], int t[]){
    int i = start;
    int j = middle+1;
    int k = start;
    while(j <= end && i <= middle){
        if(t[i] < t[j]){
            tab[k] = t[i];
            i++;
        }
        else{
            tab[k] = t[j];
            j++;
        }
        k++;

        while(i <= middle){
            tab[k] = t[i];
            i++;
            k++;
        }
    }
}

void mergesort(int start, int end, int tab[], int t[]){
    int middle;
    if(start != end){
        middle = (start+end)/2;
        mergesort(start, middle, tab, t);
        mergesort(middle + 1, end, tab, t);
        merge(start, middle, end, tab, t);
    }
}



int main(){
    int tab[30];
    int t[30];
    for(int i=0;i<30;i++) t[i] = (rand() % 30) + 1;
    for(int i=0;i<30;i++) cout << t[i] << " | ";
    cout << endl;
    mergesort(0,29,tab,t);
    for(int i=0;i<30;i++) cout << tab[i] << " | ";
    int tak;
    cin >> tak;
    return 0;
}
