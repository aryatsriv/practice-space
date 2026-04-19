// Permutations
//
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

using namespace std;

int main(){
	int n;
	cin>>n;
	if(n==3 || n==2){
		cout<<"NO SOLUTION";
		return 0;
	}
	int val=n-1;
	while(val>0){
		cout<<val<<" ";
		val=val-2;
	}
	val=n;
	while(val>0){
		cout<<val<<" ";
		val=val-2;
	}

	return 0;
}
