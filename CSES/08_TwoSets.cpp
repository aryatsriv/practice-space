// Your task is to divide the numbers 1,2,\ldots,n into two sets of equal sum.
// Input
// The only input line contains an integer n.
// Output
// Print "YES", if the division is possible, and "NO" otherwise.
// After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.
// Constraints
//
// 1 \le n \le 10^6
//
// Example 1
// Input:
// 7
//
// Output:
// YES
// 4
// 1 2 4 7
// 3
// 3 5 6
// Example 2
// Input:
// 6
//
// Output:
// NO


#include<bits/stdc++.h>

using namespace std;

#define ll long long

int main(){
	ll n;
	cin>>n;
	ll A=0,B=0;
	vector<int> a,b;
	for(int i=n;i>0;i--){
		if (A>B){
			b.push_back(i);
			B+=i;
		}
		else{
			a.push_back(i);
			A+=i;
		}
	}

	if (A==B){
		cout<<"YES\n";
		cout<<a.size()<<"\n";
		for(int val:a){
			cout<<val<<" ";
		}
		cout<<"\n";
		cout<<b.size()<<"\n";
		for(int val:b){
			cout<<val<<" ";
		}
		cout<<" ";
	}
	else{
		cout<<"NO\n";
	}

}
