// Chessboard and Queens

// Your task is to place eight queens on a chessboard so that no two queens are
// attacking each other. As an additional challenge, each square is either free
// or reserved, and you can only place queens on the free squares. However, the
// reserved squares do not prevent queens from attacking each other.

// How many possible ways are there to place the queens?

// Input
// The input has eight lines, and each of them has eight characters. Each square
// is either free (.) or reserved (*).

// Output
// Print one integer: the number of ways you can place the queens.

// Example
// Input:

// ........
// ........
// ..*.....
// ........
// ........
// .....**.
// ...*....
// ........
// Output:

// 65

#include <bits/stdc++.h>

using namespace std;

char arr[8][8];
bool col[8];
bool diag1[15];
bool diag2[15];

int rec(int i) {
  if (i >= 8) {
    return 1;
  }
  int count = 0;
  for (int j = 0; j < 8; j++) {
    if (arr[i][j] == '*') {
      continue;
    }
    if (col[j] || diag1[i + j] || diag2[i - j + 7]) {
      continue;
    }
    col[j] = true;
    diag1[i + j] = true;
    diag2[i - j + 7] = true;
    count += rec(i + 1);
    col[j] = false;
    diag1[i + j] = false;
    diag2[i - j + 7] = false;
  }
  return count;
}

int main() {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      cin >> arr[i][j];
    }
  }
  cout << rec(0);

  return 0;
}