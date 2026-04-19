// Missing Number
//
// You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
// Input
// The first input line contains an integer n.
// The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
// Output
// Print the missing number.
// Constraints
//
// 2 \le n \le 2 \cdot 10^5
//
// Example
// Input:
// 5
// 2 3 1 5
//
// Output:
// 4

#include<bits/stdc++.h>

using namespace std;

int main(){
	
	int n;
	cin>>n;
	int i=1;
	int res=0;
	while (i<n){
		int temp=0;
		cin>>temp;
		res=res^i^temp;
		i+=1;
	}

	res=res^n;
	
	cout<<res;
	return 0;
}

