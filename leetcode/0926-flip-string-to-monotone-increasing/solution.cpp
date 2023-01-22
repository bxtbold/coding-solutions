class Solution {
public:
    /**
     * RUNTIME: 27 ms (76.96%)
     * MEMORY: 11.1 MB (82.3%)
    */
    int minFlipsMonoIncr(string s) {
        size_t n = s.size();
        int cnt0 = 0, cnt1 = 0;
        for (char i : s) {
            if (i == '0') {
                cnt0++;
                }
            }
        int answer = n - cnt0;
        for (char i : s) {
            if (i == '0') {
                cnt0--;
            }
            else {
                answer = min(answer, cnt1 + cnt0);
                cnt1++;
            }
        }
        return answer;
    }
};
