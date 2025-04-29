#include<bits/stdc++.h>
#define ll long long
using namespace std;


void find_sum(vector<int> &arr, int n)
{
    vector<int> max_prefix(n);
    for(int i=0;i<n;i++)
    {
        if (i==0)
            max_prefix[i]=arr[i];
        else
            max_prefix[i]=max(max_prefix[i-1],arr[i]);
    }
    ll sum_v=0;
    // cout<<"yo";
    for(int j=n-1;j>=0;j--)
    {
        if(j==0)
            cout<<sum_v+static_cast<long long>(arr[j])<<" ";
        else{
            ll using_sum=sum_v;
            if(max_prefix[j-1]>=arr[j])
                using_sum+=static_cast<long long>(max_prefix[j-1]);
            else
                using_sum+=static_cast<long long>(arr[j]);
            cout<<using_sum<<" ";
            sum_v+=static_cast<long long>(arr[j]);
        }
    }
    cout<<endl;

}

void solve(){
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    find_sum(arr,n);

}

int main(){
    int t;
    cin>>t;
    while(t)
    {
        solve();
        t--;
    }
}