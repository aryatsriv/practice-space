// CSES Problem Set
//                 Creating Strings
//
// Task
// Submit
// Results
// Statistics
// Tests
//
//
//
//
//
//
//
// CSES - Creating Strings
//
//
//
//
//
// Time limit: 1.00 s
// Memory limit: 512 MB
//
// Given a string, your task is to generate all different strings that can be created using its characters.
// Input
// The only input line has a string of length n. Each character is between a–z.
// Output
// First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.
// Constraints
//
// 1 \le n \le 8
//
// Example
// Input:
// aabac
//
// Output:
// 20
// aaabc
// aaacb
// aabac
// aabca
// aacab
// aacba
// abaac
// abaca
// abcaa
// acaab
// acaba
// acbaa
// baaac
// baaca
// bacaa
// bcaaa
// caaab
// caaba
// cabaa
// cbaaa


#include<bits/stdc++.h>

using namespace std;

int n;
vector<string> res;
int freq[26];

void build(string s){
	if(s.length()==n){
		res.push_back(s);
		return;
	}
	for(int i=0;i<26;i++){
		if(freq[i]>0){
			freq[i]--;
			build(s+char('a'+i));
			freq[i]++;
		}
	}
}

int main(){
	string inp;
	cin>>inp;
	n=inp.length();
	for(char c:inp){
		freq[c-'a']++;
	}
	build("");
	cout<<res.size()<<endl;
	for(string c:res){
		cout<<c<<endl;
	}
	return 0;
}
