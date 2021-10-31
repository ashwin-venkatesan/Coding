#include<iostream>
#include<math.h>
using namespace std;

int main() {
  int t;
  long n, s[100000], i, diff;
  cin>>t;
  while(t--) {
    cin>>n;
    diff = 0;
    for (i = 0; i < n; i++)
    {
      cin>>s[i];
    }
    for (i = 1; i < n; i++)
    {
      diff += abs(s[i] - s[i-1]) - 1;
    }
    cout<<diff<<endl;
  }
  return 0;
}