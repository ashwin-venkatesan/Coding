#include<iostream>
using namespace std;

int main() {
    int t, n, k, f[1000], fr[1000], ele, i, total, subtotal, no, m, mo;
    cin>>t;
    while(t--) {
        cin>>n>>k;
        for(i=0;i<=n;i++) {
            f[i] = 0;
            fr[i] = 0;
        }
        for(i=1;i<=n;i++) {
            cin>>ele;
            f[ele]++;
        }
        total = 0;
        m = 0;
        for(i=1;i<=n;i++) {
            fr[f[i]]++;
            if(m < f[i])
                m = f[i];
            if(f[i]>1)
                total += f[i];
        }
        total += k;
        // cout<<"subtotal: "<<total<<'\n';
        subtotal = total;
        no = 1;
        mo = m;
        do {
            // cout<<"m: "<<m<<'\n';
            // for(i=1;i<=m;i++)
            //     cout<<fr[i]<<" ";
            // cout<<endl;
            no++;
            subtotal = k * no;
            for(i=2;i<=m;i++){
                fr[i-1] += fr[i];
                fr[i] = 0;
                if(i > 2)
                    subtotal += (fr[i-1] * (i-1));
            }
            m--;
            // cout<<"subtotal: "<<subtotal<<'\n';
            if(total > subtotal)
                total = subtotal;
        } while(no < mo);

        cout<<total<<'\n';
    }
}