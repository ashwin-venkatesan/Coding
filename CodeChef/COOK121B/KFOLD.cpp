#include<iostream>
#include<string>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int k =0, n = 0;
        cin>>n>>k;
        string s = "";
        cin>>s;
        int len = s.length()/k;
        string fin = "";
        int z = 0;
        int o = 0;
        for(int i = 0; i<s.length();i++){
            if(s[i]=='0'){
                z++;
            }
            else{
                o++;
            }
        }

        int flag = 1;
        if(z%(n/k) ==0 && o%(n/k) == 0){
            int ol = o/(n/k);
            int zl = z/(n/k);
            flag = 1;
            string nk = "";
            while(zl!=0){
                nk+="0";
                zl--;
            }
            while(ol!=0){
                nk+="1";
                ol--;
            }

            string org = nk;
            reverse(nk.begin(),nk.end());
            cout<<org<<nk<<endl;
            int zim = 0;
            int nm = n/k;
            while(zim<nm){
                if(zim%2==0){
                    fin+=org;
                }
                else{
                    fin+=nk;
                }

                zim++;
            }
            cout<<fin<<endl;
        }
        else{
            flag = 0;
            cout<<"IMPOSSIBLE"<<endl;
        }


    }
    return 0;
}