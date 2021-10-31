#include <bits/stdc++.h> 
using namespace std; 

int main() { 
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
	unordered_set <int> xset;
	unordered_set <int> yset;
	int w,h,n,m,i,j,a[100000],b[100000],suma=0,sumb=0;
	cin>>w>>h>>n>>m;
	for(i=0;i<n;i++) {
		cin>>a[i];
	}
	for(i=0;i<n;i++) {
		cin>>b[i];
	}
	


	cout << "\nAll elements : "; 
	unordered_set<int> :: iterator itr; 
	for (itr = xset.begin(); itr != xset.end(); itr++) 
		cout << (*itr) << endl; 
} 
