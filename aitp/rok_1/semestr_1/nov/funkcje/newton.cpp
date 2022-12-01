#include<iostream>

using namespace std;

int newton(int n, int K){
    if(K > n){
        return 0;
    }
    if (K==0 || n==0){
        return 1;
    }
    return newton(n - 1, K - 1)+ newton(n - 1, K);
}

int main(){
    cout << newton(5,2);
}
