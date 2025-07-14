/*A permutation of integers 1,2,\ldots,n is called beautiful if there are no adjacent elements whose difference is 1.*/
/*Given n, construct a beautiful permutation if such a permutation exists.*/
/*Input*/
/*The only input line contains an integer n.*/
/*Output*/
/*Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".*/
/*Constraints*/
/**/
/*1 \le n \le 10^6*/
/**/
/*Example 1*/
/*Input:*/
/*5*/
/**/
/*Output:*/
/*4 2 5 3 1*/
/*Example 2*/
/*Input:*/
/*3*/
/**/
/*Output:*/
/*NO SOLUTION*/


#include<iostream>
#include<vector>
using namespace std;


//better approach
void permutation(int N)
{
    // Check if N is 2 or 3, as a beautiful permutation is
    // not possible for these cases
    if (N == 2 || N == 3) {
        cout << "NO SOLUTION\n";
        return;
    }

    // Output all even numbers first
    for (int i = 2; i <= N; i = i + 2) {
    
        // Print even numbers with a step of 2
        cout << i << " ";
    }

    // Output all odd numbers next
    for (int i = 1; i <= N; i = i + 2) {
    
        // Print odd numbers with a step of 2
        cout << i << " ";
    }
}

//my approach- although this solution works one thing i missed was that i thought that my code should account for "no solution" on higher number, but it is not possible. No solution would only be there for 2 and 3 on all the higher number their would be a solution.
int main(){
	int n=0;
	cin>>n;
	vector<int> res;
	int val=n-1;
	for(int i=0;i<n;i++){
		if(val<=0){
			val=n;
		}
		res.push_back(val);
		val=val-2;
		if(i==0){
			continue;
		}
		if(abs(res[i]-res[i-1])<=1){
			cout<<"NO SOLUTION";
			return 0;
		}
	}
	for(int num: res){
		cout<<num<<" ";
	}
	return 0;
}
