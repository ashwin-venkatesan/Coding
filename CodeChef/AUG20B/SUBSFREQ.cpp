#include<iostream>
#include<math.h>
using namespace std;

int main() {
    int t;
    long n, i;
    const unsigned int M = 1000000007;
    cin>>t;
    while(t--) {
        cin>>n;
        for(i=0;i<n;i++)
            cin>>i;
        for(i=n;i>0;i--)
            cout<<pow(2,i-1)<<' ';
        cout<<'\n';
    } 
}