#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cout<<"Podaj a:";
    cin>>a;
    cout<<endl<<"Podaj b:";
    cin>>b;
    if(a==0){
        cout<<b<<endl;
        exit;
    }
    if(b==0){
        cout<<a<<endl;
        exit;
    }
    while(a!=b){
        if(a>b){
            a-=b;
        }
        else{
            b-=a;
        }
        }
    cout<<a;
    return 0;
}
