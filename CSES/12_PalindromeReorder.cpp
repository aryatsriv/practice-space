// Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).
// Input
// The only input line has a string of length n consisting of characters A–Z.
// Output
// Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".
// Constraints
//
// 1 \le n \le 10^6
//
// Example
// Input:
// AAAACACBA
//
// Output:
// AACABACAA
//



#include<bits/stdc++.h>

using namespace std;

int main(){
	string s;
	cin>>s;
	vector<int> cache(26,0);

	for(char c:s){
		cache[c-'A']+=1;
	}
	bool isOddFound=false;
	vector<char> res1;
	vector<char> res2;
	char mid;


	for(int i=0;i<cache.capacity();i++){
		if(cache[i]==0){
			continue;
		}

		if(cache[i]%2==0){
			for(int j=0;j<cache[i];j+=2){
				res1.push_back('A'+i);
			}
		}
		else if(cache[i]%2==1 && isOddFound==false){
			for(int j=1;j<cache[i];j+=2){
				res1.push_back('A'+i);
			}
			isOddFound=true;
			mid='A'+i;
		}
		else if(cache[i]%2==1){
			cout<<"NO SOLUTION";
			return 0;
		}
	}

	cout<<string(res1.begin(),res1.end());
	if(isOddFound){
		cout<<mid;
	}
	reverse(res1.begin(),res1.end());
	cout<<string(res1.begin(),res1.end());
	return 0;
}
