// Mex Grid Construction
// Your task is to construct an n \times n grid where each square has the
// smallest nonnegative integer that does not appear to the left on the same row
// or above on the same column.
// Input
// The only line has an integer n.
// Output
// Print the grid according to the example.
// Constraints
//
// 1 \le n \le 100
//
// Example
// Input:
// 5
//
// Output:
// 0 1 2 3 4
// 1 0 3 2 5
// 2 3 0 1 6
// 3 2 1 0 7
// 4 5 6 7 0

#include <bits/stdc++.h>

using namespace std;

void using_set(int &n, vector<vector<int>> &res) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      set<int> cache;
      for (int k = 0; k < i; k++) {
        cache.insert(res[k][j]);
      }
      for (int k = 0; k < j; k++) {
        cache.insert(res[i][k]);
      }
      int x = 0;
      while (cache.count(x)) {
        x++;
      }
      res[i][j] = x;
    }
  }
}

void using_xor(int n,vector<vector<int>> &res){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			res[i][j]=i^j;
		}
	}
}


int main() {
  int n = 0;
  cin >> n;
  vector<vector<int>> res(n, vector<int>(n));
  //solved_using_set(n, res);

  using_xor(n, res);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << res[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}
