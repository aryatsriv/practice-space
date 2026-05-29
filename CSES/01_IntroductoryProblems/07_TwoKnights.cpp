// Two Knights
//
// Your task is to count for k=1,2,\ldots,n the number of ways two knights can be placed on a k \times k chessboard so that they do not attack each other.
// Input
// The only input line contains an integer n.
// Output
// Print n integers: the results.
// Constraints
//
// 1 \le n \le 10000
//
// Example
// Input:
// 8
//
// Output:
// 0
// 6
// 28
// 96
// 252
// 550
// 1056
// 1848

#include<iostream>

#define ll long long

using namespace std;

void solve(ll k){
	ll totalWays=(k*k)*((k*k)-1)/2;
	
	ll count=(k-2)*2*(k-1)*2;
	ll value=totalWays-count;
	cout<<value<<endl;
}

int main(){
	ll n;
	cin>>n;
	for(ll k=1;k<=n;k++){
		solve(k);
	}
	return 0;
}
