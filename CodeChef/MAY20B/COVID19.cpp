#include<iostream>
#include<climits>
using namespace std;

int main() {
  int t,n,a[8],i,j,min=INT_MAX,max=1,c;
  cin>>t;
  while(t--) {
    min=INT_MAX;
    max=1;
    cin>>n;
    for(i=0;i<n;i++)
      cin>>a[i];
    for(i=0;i<n;i++) {
      c = 1;
      for(j=i;j>0;j--){
        if(a[j-1] >= a[j] - 2) {
          c += 1;
        }
        else {
          break;
        }
      }
      for(j=i;j<n-1;j++) {
        if(a[j+1] <= a[j] + 2) {
          c += 1;
        }
        else {
          break;
        }
      }
      if(min > c) {
        min = c;
      }
      if(max < c) {
        max = c;
      }
    }
    cout<<min<<' '<<max<<'\n';
  }
  return 0;
}