class Solution {
public:
    /**
     * RUNTIME: 0 ms (100%)
     * MEMORY: 6 MB (11.10%)
    */
    int reverse(int x) {
        int answer = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (answer > INT_MAX / 10 || (answer == INT_MAX / 10 && pop > 7)) {
                return 0;
            }
            if (answer < INT_MIN / 10 || (answer == INT_MIN / 10 && pop < -8)) {
                return 0;
            }
            answer = answer * 10 + pop;
        }
        return answer;
    }
};
