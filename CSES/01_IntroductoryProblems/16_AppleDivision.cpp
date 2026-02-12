// Apple Division
// Time limit: 1.00 s
// Memory limit: 512 MB
//
// There are n apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.
// Input
// The first input line has an integer n: the number of apples.
// The next line has n integers p_1,p_2,\dots,p_n: the weight of each apple.
// Output
// Print one integer: the minimum difference between the weights of the groups.
// Constraints
//
// 1 \le n \le 20
// 1 \le p_i \le 10^9
//
// Example
// Input:
// 5
// 3 2 7 4 1
//
// Output:
// 1
//
// Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).


#include<bits/stdc++.h>
#define ll long long


using namespace std;
vector<ll> inp;
ll leftSum, rightSum;
ll minVal;

void findMinDifference(int i){
	if (i==inp.size()){
		minVal=min(minVal,abs(rightSum-leftSum));
		return;
	}
	leftSum+=inp[i];
	findMinDifference(i+1);
	leftSum-=inp[i];
	rightSum+=inp[i];
	findMinDifference(i+1);
	rightSum-=inp[i];
}



int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int val;
		cin>>val;
		inp.push_back(val);
	}
	minVal=*max_element(inp.begin(),inp.end());
	findMinDifference(0);
	cout<<minVal;
	return 0;
}
