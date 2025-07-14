/*You are given an array of n llegers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.*/
/*On each move, you may increase the value of any element by one. What is the minimum number of moves required?*/
/*Input*/
/*The first input line contains an lleger n: the size of the array.*/
/*Then, the second line contains n llegers x_1,x_2,\ldots,x_n: the contents of the array.*/
/*Output*/
/*Prll the minimum number of moves.*/
/*Constralls*/
/**/
/*1 \le n \le 2 \cdot 10^5*/
/*1 \le x_i \le 10^9*/
/**/
/*Example*/
/*Input:*/
/*5*/
/*3 2 5 1 7*/
/**/
/*Output:*/
/*5*/


#include<iostream>

using namespace std;

#define ll long long
int main(){
	ll n=0;
	cin>>n;
	ll maxValSoFar=0;
	ll minMoves=0;
	for(ll i=0;i<n;i++){
		ll a=0;
		cin>>a;
		if(a<maxValSoFar){
			minMoves+=maxValSoFar-a;
			a=maxValSoFar;
		}
		maxValSoFar=a;
	}
	cout<<minMoves;
	return 0;
}
