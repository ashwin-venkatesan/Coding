#include<iostream>
using namespace std;

long numsum(long a) {
  long temp = a, sum = 0;
  while(temp != 0) {
    sum += temp % 10;
    temp /= 10;
  }
  return sum;
}

int main() {
  int t,n,i,cp,mp ;
  long a,b;
  cin>>t;
  while(t--) {
    cp = 0; mp = 0;
    cin>>n;
    for (i = 0; i < n; i++)
    {
      cin>>a>>b;
      a = numsum(a);
      b = numsum(b);
      if(a >= b)
        cp += 1;
      if(b >= a)
        mp += 1;
    }
    if(cp > mp)
      cout<<"0 "<<cp<<endl;
    else if(mp > cp)
      cout<<"1 "<<mp<<endl;
    else
      cout<<"2 "<<cp<<endl;
  }
  return 0;
}