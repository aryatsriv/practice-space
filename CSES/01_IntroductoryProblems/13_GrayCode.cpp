// Gray Code

// A Gray code is a list of all 2^n bit strings of length n, where any two
// successive strings differ in exactly one bit (i.e., their Hamming distance is
// one). Your task is to create a Gray code for a given length n. Input The only
// input line has an integer n. Output Print 2^n lines that describe the Gray
// code. You can print any valid solution. Constraints

// 1 \le n \le 16

// Example
// Input:
// 2

// Output:
// 00
// 01
// 11
// 10

#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  auto res = vector<string>();
  res.push_back("0");
  res.push_back("1");
  for (int i = 2; i <= n; i++) {
    vector<string> curr;
    for (string val : res) {
      curr.push_back("0" + val);
    }
    for (int i = res.size() - 1; i >= 0; i--) {
      curr.push_back("1" + res[i]);
    }

    res = curr;
  }
  for (auto val : res) {
    cout << val << endl;
  }
  return 0;
}