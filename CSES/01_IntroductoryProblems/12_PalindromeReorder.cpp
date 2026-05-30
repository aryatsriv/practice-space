// Palindrome Reorder

// Given a string, your task is to reorder its letters in such a way that it
// becomes a palindrome (i.e., it reads the same forwards and backwards). Input
// The only input line has a string of length n consisting of characters A–Z.
// Output
// Print a palindrome consisting of the characters of the original string. You
// may print any valid solution. If there are no solutions, print "NO SOLUTION".
// Constraints

// 1 \le n \le 10^6

// Example
// Input:
// AAAACACBA

// Output:
// AACABACAA

#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;
  cin >> s;
  int cache[26] = {0};

  for (char c : s) {
    cache[c - 'A'] += 1;
  }

  bool oddFound = false;
  for (int val : cache) {
    if (val % 2 != 0 && oddFound) {
      cout << "NO SOLUTION";
      return 0;
    }
    if (val % 2 != 0) {
      oddFound = true;
    }
  }
  vector<string> a(0);
  vector<string> b(0);
  string odd = "";
  for (int i = 0; i < 26; i++) {
    if (cache[i] % 2 == 0 && cache[i] > 0) {
      a.push_back(string(cache[i] / 2, i + 'A'));
      b.push_back(string(cache[i] / 2, i + 'A'));
    }
    if (cache[i] % 2 == 1) {
      odd = string(cache[i], i + 'A');
    }
  }
  string res = "";
  for (string c : a) {
    res += c;
  }
  res += odd;
  for (int i = b.size() - 1; i >= 0; i--) {
    res += b[i];
  }

  cout << res;

  return 0;
}