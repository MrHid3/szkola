#include<iostream>


using namespace std;


long long silnia(int n){
    if (n == 1){
        return 1;
    }
    else{
        if (n-1!=1){
            return n*silnia(n-1);
        }
        else {
            return n;
        }
    }
}

int main(){
    int n;
    cout << "Hello adventurer, what's n?" << endl;
    cin >> n;
    cout << silnia(n);
    return 0;
}
