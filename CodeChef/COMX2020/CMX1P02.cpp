#include <iostream>
using namespace std;

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a%b);
}
int lcm(int a[], int n) {
  int res = 1, i;
  for (i = 0; i < n; i++) {
    res = res*a[i]/gcd(res, a[i]);
  }
  return res;
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n = 0, n1 =0;
        long lcmans;
        int r = 0;
        cin>>n;
        int a[n];
        for(int i = 0;i<n;i++){
            cin>>a[i];
        }
        cin>>r;
        lcmans = lcm(a,n);
        cout<<lcmans+r<<endl;
    }

    return 0;
}