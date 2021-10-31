#include <iostream>
using namespace std;

int main() {
    long int n = 0;
    cin>>n;
    long int h[n];

    for(long int i = 0; i<n; i++){
        cin>>h[i];
    }

    long int q = 0;
    cin>>q;
    string s = "";
    while(q--){
        long int w = 0;
        long int i = 0;
        cin>>s>>w>>i;
        long int sum = 0;
        if(s[1]=='a'){
            h[i-1]+=w;
        }

        else{
            for(long int z = w-1; z<i; z++){
                sum+=h[z];
            }
            cout<<sum<<endl;
            sum = 0;
        }
    }


    return 0;
}