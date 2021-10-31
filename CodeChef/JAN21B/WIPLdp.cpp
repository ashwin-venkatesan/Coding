#include <bits/stdc++.h>
using namespace std;

long minDA(long arr[], int n, long tsum)
{
    bool table[n+1][tsum+1];
    for (long i = 0; i <= n; i++)
        table[i][0] = true;
    for (long i = 1; i <= tsum; i++)
        table[0][i] = false;
    for (long i=1; i<=n; i++)
    {
        for (long j=1; j<=tsum; j++)
        {
            table[i][j] = table[i-1][j];
            if (arr[i-1] <= j)
                table[i][j] |= table[i-1][j-arr[i-1]];
        }
    }
    long diff = INT_MAX;
    for (long j=tsum/2; j>=0; j--)
    {
        if (table[n][j] == true)
        {
            diff = tsum-2*j;
            break;
        }
    }
    return diff;
}

int main() {
	int t, n, k;
	long i, a[4000], tsum, idx, buf, bufsum;
	scanf("%d", &t);
	while(t--) {
		scanf("%d %d", &n, &k);
		for(i=0;i<n;i++) {
			scanf("%ld", &a[i]);
		}
        if(n == 1) {
            printf("-1\n");
            continue;
        }
		sort(a,a+n,greater<>());
		tsum = 0;
		idx = 0;
		while(tsum < 2*k && idx < n)
			tsum += a[idx++];
		if(idx == 1)
			tsum += a[idx++];
		if(tsum < 2*k) {
			printf("-1\n");
			continue;
		}
		buf = minDA(a,idx,tsum);
		long aff = (tsum - buf) / 2;
		if(aff >= k) {
			printf("%ld\n", idx);
			continue;
		}
		else {
			buf = k - aff;
		}
		bufsum = 0;
		while(bufsum < buf && idx < n)
			bufsum += a[idx++];
		if(bufsum < buf) {
			printf("-1\n");
			continue;
		}
		printf("%ld\n", idx);
	}
	return 0;
}