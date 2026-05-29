// Two Sets
//
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

#include<iostream>
#include<vector>

#define int long long

using namespace std;

void solve(int n){
	vector<int> a;
	vector<int> b;
	int aSum=0,bSum=0;
	
	for(int i=n;i>0;i--){
		if(aSum<=bSum){
			aSum+=i;
			a.push_back(i);
		}
		else{
			bSum+=i;
			b.push_back(i);
		}
	}

	if(aSum!=bSum){
		cout<<"NO";
		return;
	}
	cout<<"YES"<<endl;
	cout<<a.size()<<endl;
	for(int x : a){
		cout<<x<<" ";
	}
	cout<<endl;
	cout<<b.size()<<endl;
	for(int x : b){
		cout<<x<<" ";
	}
	cout<<endl;
}

int32_t main(){
	int n;
	cin>>n;
	solve(n);
	return 0;
}
