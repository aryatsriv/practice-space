// Apple Division

// There are n apples with known weights. Your task is to divide the apples into
// two groups so that the difference between the weights of the groups is
// minimal. Input The first input line has an integer n: the number of apples.
// The next line has n integers p_1,p_2,\dots,p_n: the weight of each apple.
// Output
// Print one integer: the minimum difference between the weights of the groups.
// Constraints

// 1 \le n \le 20
// 1 \le p_i \le 10^9

// Example
// Input:
// 5
// 3 2 7 4 1

// Output:
// 1

// Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has
// weights 1 and 7 (total weight 8).

#include <bits/stdc++.h>
#include <numeric>
#define int long long
using namespace std;

int n;
int min_val = 0;
vector<int> nums;

void rec(int i, int a_sum, int b_sum) {
  if (i == n) {
    min_val = min(min_val, abs(a_sum - b_sum));
    return;
  }
  rec(i + 1, a_sum + nums[i], b_sum);
  rec(i + 1, a_sum, b_sum + nums[i]);
}

int32_t main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int temp;
    cin >> temp;
    nums.push_back(temp);
  }

  min_val = accumulate(nums.begin(), nums.end(), 0ll);
  rec(0, 0, 0);
  cout << min_val;
}
