// Repetitions
// You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
// Input
// The only input line contains a string of n characters.
// Output
// Print one integer: the length of the longest repetition.
// Constraints
//
// 1 \le n \le 10^6
//
// Example
// Input:
// ATTCGGGA
//
// Output:
// 3

#include<bits/stdc++.h>

using namespace std;

int main(){
	string s;
	cin>>s;
	int i=1;
	int max_count=1;
	int count=1;
	while(i<s.size()){
		count=s[i]==s[i-1]? count+1:1;
		max_count=max(count,max_count);
		i+=1;
	}
	cout<<max_count;
	return 0;

}
