#include <iostream>

bool isEven(long long x) {
  if (x % 2 == 0) {
    return true;
  }
  return false;
}

long long pow(long long x, int n) {
  if (n == 0) {
    return 1;
  }
  if (n == 1) {
    return x;
  }
  if (isEven(x)) {
    return pow(x * x, n / 2);
  }
  else {
    // return pow(x * x, (n - 1) / 2) * x;
    return pow(x, n - 1) * x; // more efficient
  }
}

int main() {
  std::cout << pow(5, 3) << std::endl;
}