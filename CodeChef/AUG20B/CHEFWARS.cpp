#include <iostream>
using namespace std;

int main() {
    long t, p, h;
    cin>>t;
    while(t--) {
        cin>>h>>p;
        while(p!=0) {
            h -= p;
            p /= 2;
            if(h<=0) 
                break;
        }
        if(h<=0) {
            cout<<"1\n";
        }
        else {
            cout<<"0\n";
        }
    }
}