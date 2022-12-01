#include<iostream>

using namespace std;

long fibonacci(int a){
    if (a == 0){
        return 0;
    }
    else if (a == 1){
        return 1;
    }
    else{
        return (fibonacci(a-1)+fibonacci(a-2));
    }
}

int main(){
    int n;
    cout << "Hello adventurer, what's n?" << endl;
    cin >> n;
    cout << fibonacci(n);
}
