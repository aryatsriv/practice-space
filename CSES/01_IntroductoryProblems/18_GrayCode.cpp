// Gray Code

// A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
// Your task is to create a Gray code for a given length n.
// Input
// The only input line has an integer n.
// Output
// Print 2^n lines that describe the Gray code. You can print any valid solution.
// Constraints

// 1 \le n \le 16

// Example
// Input:
// 2

// Output:
// 00
// 01
// 11
// 10


#include<bits/stdc++.h>
 
using namespace std;
 
void tests(){
	int n,a,b;
	cin>>n>>a>>b;
	if(n<0 || n<(a+b)){
		cout<<"NO"<<endl;
		return;
	}
	
	int ties=n-(a+b);
	n=n-ties;
	if(n>0 && (a==n || b==n)){
		cout<<"NO"<<endl;
		return;
	}
	cout<<"YES"<<endl;
	//1st particpant
	for(int i=1;i<=n+ties;i++){
		cout<<i<<" ";
	}
	cout<<endl;
	//2nd participant
	for(int i=1;i<=n;i++){
		int x=i+a;
		if(x>n){
			x=x-n;
		}
		cout<<x<<" ";
 
	}
	for(int i=n+1;i<=n+ties;i++){
		cout<<i<<" ";
	}
	cout<<endl;
	
}
 
int main(){
	int n=0;
	cin>>n;
	while(n>0){
		tests();
		n=n-1;
	}
	return 0;
