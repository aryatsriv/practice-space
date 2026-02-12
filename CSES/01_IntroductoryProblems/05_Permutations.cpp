// Time limit: 1.00 s
// Memory limit: 512 MB
//
// A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.
// Given n, construct a beautiful permutation if such a permutation exists.
// Input
// The only input line contains an integer n.
// Output
// Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
// Constraints
//
// 1 \le n \le 10^6
//
// Example 1
// Input:
// 5
//
// Output:
// 4 2 5 3 1
// Example 2
// Input:
// 3
//
// Output:
// NO SOLUTION

#include<bits/stdc++.h>

#define ll long long 
using namespace std;

int main(){
	ll inp=0;
	cin>>inp;
	if(inp==3 || inp==2){
		cout<<"NO SOLUTION";
		return 0;
	}
	ll val=inp-1;
	while(val>0){
		cout<<val<<" ";
		val-=2;
	}
	val=inp;
	while(val>0){
		cout<<val<<" ";
		val-=2;
	}
	return 0;
	
}
