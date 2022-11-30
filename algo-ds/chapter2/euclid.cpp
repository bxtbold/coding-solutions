#include <iostream>


long long GCD(long long m, long long n) {
/**
 * Big-O => O(logN)
**/
  std::cout << "The common largest divisor of ";
  std::cout << m << " and " << n;
  while (n != 0) {
    long long rem = m % n;
    m = n;
    n = rem;
  }
  std::cout << " is " << m << std::endl;
  return m;
}


int main() {
  GCD(1590, 1989);
}