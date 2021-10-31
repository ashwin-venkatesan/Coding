#include <iostream>
using namespace std;

int main() {
    long t, c, r, cc, cr;
    cin>>t;
    while(t--) {
        cin>>c>>r;
        cc = c / 9;
        cr = r / 9;
        if(c % 9)
            cc++;
        if(r % 9)
            cr++;
        if(cr <= cc)
            cout<<"1 "<<cr<<'\n';
        else
            cout<<"0 "<<cc<<'\n';
    }
}