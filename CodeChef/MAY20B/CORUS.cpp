#include<iostream>
using namespace std;

int main() {
  long t,n,q,c,i,j,cur,pending,temp;
  char s[100000];
  scanf("%ld", &t);
  while(t--) {
    scanf("%ld %ld",&n,&q);
    scanf("%s", &s);
    int iso[26] = {};
    for(i=0;i<n;i++) {
      iso[s[i] - 'a']++;
    }
    while(q--) {
      pending = 0;
      scanf("%ld", &c);
      if(c == 0){
        printf("%ld\n",n);
        continue;
      }
      for(i=0;i<26;i++) {
        temp = iso[i] - c;
        if(temp > 0)
          pending += temp;
      }
      printf("%ld\n",pending);
    }
  }
  return 0;
}