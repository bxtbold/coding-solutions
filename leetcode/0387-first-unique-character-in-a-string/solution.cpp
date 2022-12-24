class Solution {
public:
    /**
     * RUNTIME: 47 ms (78.17%)
     * MEMORY: 10.8 MB (46.38%)
    */
    int firstUniqChar(string s) {
        unordered_map<char, int> hashmap;
        for (char each : s) {
            ++hashmap[each];
        }
        for (int i = 0; i < s.size(); i++) {
            if (hashmap[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};
