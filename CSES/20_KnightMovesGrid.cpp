// There is a knight on an n \times n chessboard. For each square, print the minimum number of moves the knight needs to do to reach the top-left corner.
// Input
// The only line has an integer n.
// Output
// Print the number of moves for each square.
// Constraints
//
// 4 \le n \le 1000
//
// Example
// Input:
// 8
//
// Output:
// 0 3 2 3 2 3 4 5
// 3 4 1 2 3 4 3 4
// 2 1 4 3 2 3 4 5
// 3 2 3 2 3 4 3 4
// 2 3 2 3 4 3 4 5
// 3 4 3 4 3 4 5 4
// 4 3 4 3 4 5 4 5
// 5 4 5 4 5 4 5 6

#include<bits/stdc++.h>
#include <cstdint>

using namespace std;

vector<pair<int,int>> dirs={{-2,-1},{-2,1},{-1,2},{-1,-2},{1,-2},{1,2},{2,-1},{2,1}};
void printres(vector<vector<int>> &dist,int n){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){

		}
		cout<<endl;
	}
}
int main(){
	int n;
	cin>>n;
	int count=0;
	vector<vector<int>> dist(n,vector<int>(n, INT32_MAX));
	queue<pair<int,int>> q;
	q.push({0,0});
	dist[0][0]=0;
	while(q.size()>0){
		//printres(dist,n);
		auto val=q.front();
		int val1=val.first;
		int val2=val.second;
		q.pop();
		for(auto dir:dirs){
			int m1=dir.first;
			int m2=dir.second;
			if(val1+m1>=0 && val2+m2>=0 && val1+m1<n && val2+m2<n){
				if((dist[val1+m1][val2+m2])>(dist[val1][val2]+1)){
					q.push({val1+m1,val2+m2});
					dist[val1+m1][val2+m2]=dist[val1][val2]+1;
				}
			}
		}
	}
	printres(dist,n);
	return 0;
}
