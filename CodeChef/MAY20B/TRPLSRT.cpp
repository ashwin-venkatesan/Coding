#include<iostream>
using namespace std;

int main() {
  int t;
  long n,i,j,k,temp,first,second,third,count,sorted,waste;
  scanf("%d", &t);
  while(t--) {
    scanf("%ld %ld", &n, &waste);
    count= 0;
    long a[n],ans[n][3];
    for (i = 0; i < n; i++) {
      scanf("%ld", &a[i]);
    }
    long limit=n/2;
    if(limit>waste){
      limit=waste;
    }
    for (i = 0, j = 0; i < limit; i++) {
      first = j;
      if(a[first] == first+1) {
        // cout<<"Equal Case: "<<a[first]<<" : "<<first + 1<<endl<<endl;
        i--;
        j++;
        if(j == n) {
          break;
        }
        continue;
      }
      second = a[first] - 1;
      if(first+1 == a[second]) {
        int tval = 0, flag = 0;
        for(third = first + 1; third < n; third++)
          if(a[third] - 1 != third && third != second) {
            tval = third;
            if(a[third] == a[a[third]-1]) {
              flag = 1;
              break;
            }            
          }
        if(flag == 0) {
          third = tval;
        }
        if(third == n) {
          break;
        }
      }
      else {
        third = a[second] - 1;
        if(a[third] == j + 1)
          j++;
      }
      
      ans[count][0] = first + 1;
      ans[count][1] = second + 1;
      ans[count++][2] = third + 1;
      // cout<<"val: "<<a[first]<<" : "<<a[second]<<" : "<<a[third]<<endl;
      // cout<<"pos: "<<first<<" : "<<second<<" : "<<third<<endl;
      temp = a[first];
      a[first] = a[third];
      a[third] = a[second];
      a[second] = temp;
      
      // for(int c=0;c<n;c++) 
      //   cout<<a[c]<<" ";
      // cout<<endl<<endl;
    }
    sorted = 1;
    for(i=0;i<n;i++) {
      if(a[i] != i+1) {
        sorted = 0;
        break;
      }
    }
    if(sorted == 1) {
      printf("%ld\n", count);
      for(i=0;i<count;i++)
        printf("%ld %ld %ld\n", ans[i][0], ans[i][1], ans[i][2]);
    }
    else {
      printf("-1\n");
    }
  }
  return 0;
}