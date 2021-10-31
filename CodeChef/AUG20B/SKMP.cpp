#include <iostream>
#include <string.h>
using namespace std;

int main() {
  int t;
  cin>>t;
  while(t--){
      string s1 = "";
      string s2 = "";
      cin>>s1;
      cin>>s2;
      int l1 = s1.length();
      int l2 = s2.length();
      
      //cout<<s1<<endl<<s2<<endl<<l1<<endl<<l2<<endl;
      
      int txt[26] = {0};
      int pattern[26] = {0};
      
      for(int i=0;i<l1;i++){
        int a = (int)(s1[i]);
        //cout<<s1[i]<<endl;
        //cout<<(int)(a);
        txt[a-97]++;
    }
    
    for(int j=0;j<l2;j++){
      int b = (int)(s2[j]);
      pattern[b-97]++;
    }
    char first = s2[0];
    char second = s2[1];
    //cout<<first<<endl;
    string final = "";
    for(int i = 0; i<26; i++){
        s1[i]-=s2[i];
      
    }   
    for(int i=0;i<26;i++){
       
      if((char)(i+97)==first && (int)(first)>(int)(second)){
          for(int d=0;d<l2;d++){
              final+=s2[d];
              txt[((int)(s2[i])) - 97]--;
              
          }
      }
      else if(s1[i]==first && (int)(txt[i])<=(int)(second)){
          while(txt[i]!=0){
              final+=(char)(i+97);
              txt[i]--;
           }
          for(int d=0;d<l2;d++){
              final+=s2[d];
              txt[((int)(s2[i])) - 97]--;
              pattern[((int)(s2[i])) - 97]--;
          }
      }
      
    
          while(txt[i]!=0){
              final+=(char)(i+97);
                  final+=(char)(i+97);
                  txt[i]--;
              }
         
      
      
    }
    
    cout<<final;
    
  }
  return 0;
}