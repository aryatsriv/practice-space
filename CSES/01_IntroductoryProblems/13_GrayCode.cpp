// Gray Code
// A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).
// Your task is to create a Gray code for a given length n.
// Input
// The only input line has an integer n.
// Output
// Print 2^n lines that describe the Gray code. You can print any valid solution.
// Constraints
//
// 1 \le n \le 16
//
// Example
// Input:
// 2
//
// Output:
// 00
// 01
// 11
// 10


#include<bits/stdc++.h>

using namespace std;

vector<string> rec(int n){
	if (n==1){
		return {"0","1"};
	}
	vector<string> a=rec(n-1);
	vector<string> b=a;
	reverse(b.begin(),b.end());
	for(string &s:a){
		s="0"+s;
	}
	for(string &s:b){
		s="1"+s;
	}
	a.insert(a.end(),b.begin(),b.end());
	return a;
}

int main(){
	int n;
	cin>>n;
	vector<string> res=rec(n);
	for(string s:res){
		cout<<s<<endl;
	}
	return 0;
}
