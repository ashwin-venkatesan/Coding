#include<iostream>
using namespace std;

int main() {
    long t,n,k,a,i,temp, roud,flag;
    cin>>t;
    while(t--) {
        cin>>n>>k;
        temp = 0;
        roud = 1;
        flag = 0;
        for(i=0;i<n;i++) {
            cin>>a;
            if(a > k) {
                flag = 1;
                break;
            }
            if(temp + a > k) {
                temp = 0;
                roud++;
            }
            temp += a;
        }
        if(flag == 1) {
            cout<<"-1\n";
        }
        else
            cout<<roud<<'\n';
    }
    return 0;
}