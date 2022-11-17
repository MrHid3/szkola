#include<iostream>
#include<algorithm>
#include<cstdlib>

using namespace std;


int main(){
    int tab[30];
    int sear;
    int min = 0;
    int max = 30;
    for(int i=0;i<30;i++) tab[i] = (rand() % 30) + 1;
    sort(tab, tab + 30);
    cout << "What number do you wish to search for?" << endl;
    cin >> sear << endl;
    while (sear != tab[(min+max)/2]){
        if(sear > (min+max)/2) min = (min+max)/2;
        else if(sear < (min+max)/2) max = (min+max)/2;
        else break;
        if(min>)
    }
    if (min!=max || ){
        cout << (min+max)/2;
    }
    else{
        cout << -1;
    }
    for(int i=0;i<30;i++){
        cout << tab[i] << " | ";
    }
    return 0;
}
