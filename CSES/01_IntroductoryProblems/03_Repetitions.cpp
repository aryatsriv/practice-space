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
	string text="";
	cin>>text;
	int i=0;
	int n=text.size();
	int maxVal=0;
	while(i<n){
		int j=i;
		while(j<n && text[j]==text[i]){
			j+=1;
		}
		maxVal=max(maxVal,j-i);
		i=j;
	}
	cout<<maxVal;
	return 0;
}
