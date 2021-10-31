#include<iostream>
using namespace std;

int main() {
  int i, t, k, flag, row, col, j;
  cin>>t;
  while(t--) {
    cin>>k;
    flag = 0;
    for(i=0;i<8;i++) {
      for(j=0;j<8;j++) {
        if(i==0 && j==0) {
          cout<<"O";
          k--;
          continue;
        }
        if(k!=0 && flag==0) {
          cout<<".";
          k--;
          continue;
        }
        if(k==0 && flag==0) {
          row = i;
          col = j;
          if(col == 0) {
           row -= 1;
           col = 7;
          }
          cout<<"X";
          flag = 1;
          continue;
        }
        if(flag == 1) {
          if(j!=col && row == 0 && row == i)
            cout<<".";
          else if(j!=col)
            cout<<"X";
          else {
            cout<<"X";
            flag = 2;
          }
          continue;
        }
        if(flag == 2){
          cout<<".";
        }
      }
      cout<<"\n";
    }
  }
  return 0;
}