/*You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.*/
/*Input*/
/*The only input line contains a string of n characters.*/
/*Output*/
/*Print one integer: the length of the longest repetition.*/
/*Constraints*/
/**/
/*1 \le n \le 10^6*/
/**/
/*Example*/
/*Input:*/
/*ATTCGGGA*/
/**/
/*Output:*/
/*3*/


#include<iostream>

using namespace std; 

int main(){
	string s="";
	cin>>s;
	int i=0;
	int j=0;
	int n=s.size();
	int maxCount=0;
	while(j<n){
		int i=j+1;
		while(i<n && s[i]==s[j]){
			i+=1;
		}
		maxCount=max(maxCount,i-j);
		j=i;
	}
	cout<<maxCount;
	return 0;
}

