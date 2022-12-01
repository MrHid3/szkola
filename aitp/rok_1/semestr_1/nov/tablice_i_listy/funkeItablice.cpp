#include<iostream>
#include<cstdlib>
using namespace std;
int main(){
    int n,sear,znal,minl,maxl; //naturalna wpisywana przez u¿ywkownika, liczba szukana, indeks liczby znalezionej, najmniejsza liczba z tablicy, najwiêksza liczba z tablicy
    cout << "Hello adventurer, what's n?" << endl;
    cin >> n;
    int liczby[n];
    for(int i=0;i<n;i++) liczby[i] = rand() % n + 1;
    cout << "So, which number do you wish to check for?" << endl;
    cin >> sear;
    for(int i=0;i<n;i++){
        if (liczby[i]==sear){
            znal = i;
            break;
        }
        else znal = -1;
    }
    cout << znal << endl;
    minl = n;
    maxl = 0;
    for(int i=0;i<n;i++){
        if(liczby[i]<minl) minl = liczby[i];
        if(liczby[i]>maxl) maxl = liczby[i];
    }
    cout << "The lowest of these numbers is " << minl << ", and the biggest is " << maxl << endl;
    for(int i=0;i<n;i++) cout << liczby[i] << " | "; //wypisanie tablicy aby sprawdziæ dzia³anie programu
}
