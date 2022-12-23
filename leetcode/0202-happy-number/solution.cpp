class Solution {
public:
    /**
     * RUNTIME: 0 ms (100%)
     * MEMORY: 6.2 MB (39.70%)
    */
    bool isHappy(int n) {
        if (n == 1) { return true; }
        std::unordered_map<int, int> hashset;
        int sum;
        while (true) {
            if (n < 10) {
                n *= n;
            }
            else {
                sum = 0;
                while (true) {
                    unsigned tmp = (n % 10) * (n % 10);
                    sum += tmp;
                    if (n / 10 == 0) {
                        break;
                    }
                    n = n / 10;
                }
                n = sum;
                if (n == 1) { return true; }
            }
            if (hashset.find(n) == hashset.end() ) {
                hashset[n] = 1;
            }
            else {
                return false;
            }
        }
        return false;
    }
};

int main() {
    Solution a;
    std::cout << a.isHappy(19);
    return -1;
}